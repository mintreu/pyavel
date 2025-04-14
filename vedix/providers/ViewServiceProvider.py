# vedix/providers/ViewServiceProvider.py

from vedix.support.service_provider import ServiceProvider
from jinja2 import Environment, FileSystemLoader

class ViewServiceProvider(ServiceProvider):
    def __init__(self, app):
        super().__init__(app)
        self.app = app  # Ensure 'app' is passed and assigned to 'self.app'

    def register(self):
        env = Environment(loader=FileSystemLoader('resources/views'))
        self.app.bind('view', env)
