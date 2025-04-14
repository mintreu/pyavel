# vedix/providers/RouteServiceProvider.py

from vedix.support.service_provider import ServiceProvider
from vedix.routing.Route import Route

class RouteServiceProvider(ServiceProvider):
    def __init__(self, app):
        super().__init__(app)
        self.app = app  # Ensure 'app' is passed and assigned to 'self.app'

    def boot(self):
        Route.get('/', lambda request: { 'view': 'home.html', 'data': { 'title': 'Welcome to Pyavel' } })
        Route.get('/api/hello', lambda request: 'Hello from API!')
