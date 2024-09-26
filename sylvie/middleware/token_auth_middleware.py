from channels.db import  database_sync_to_async
from channels.exceptions import DenyConnection

from knox.auth import  TokenAuthentication

from django.contrib.auth.models import AnonymousUser
from django.db import  close_old_connections

from rest_framework.exceptions import  AuthenticationFailed

@database_sync_to_async
def get_user (token):
    try:
        user, token = TokenAuthentication().authenticate_credentials(token.encode('ascii'))
        close_old_connections()
        return user
    except AuthenticationFailed as e:
        return AnonymousUser()

class TokenAuthMiddleware:
    def __init__(self, app):
        self.app = app
        
    async def __call__(self, scope, receive, send):
        scope['user'] = AnonymousUser()
        headers = dict(scope['headers'])
        if b'authorization' in headers:
            # Get authorization token from headers
            token = headers[b'authorization'].decode()
            token_name, token = token.split()
            # If token matches the required prefix, authenticate the user
            if token_name == 'Bearer' and len(token):
                scope['user'] = await get_user(token)
                
        return await self.app(scope, receive, send)