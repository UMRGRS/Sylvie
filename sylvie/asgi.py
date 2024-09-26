"""
ASGI config for sylvie project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from apps.machines import routing as machines_routing

from .middleware.token_auth_middleware import TokenAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sylvie.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": 
        TokenAuthMiddleware(URLRouter(machines_routing.websocket_urlpatterns))
})