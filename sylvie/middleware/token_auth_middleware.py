from channels.db import  database_sync_to_async

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
        
        query_string = scope["query_string"].decode()
        token = self.get_token_from_query_string(query_string)
        
        if token:
            # Try to authenticate user with the token
            scope["user"] = await get_user(token)
        else:
            scope["user"] = AnonymousUser()
                
        return await self.app(scope, receive, send)
    
    def get_token_from_query_string(self, query_string):
        # Parse query string and retrieve token
        try:
            params = dict(param.split("=") for param in query_string.split("&"))
            return params.get("token")
        except (ValueError, KeyError):
            return None
