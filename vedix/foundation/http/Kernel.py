# vedix/foundation/http/Kernel.py

from vedix.http.Request import Request
from vedix.http.Response import Response
from vedix.routing.Router import Router
from vedix.support.service_provider import ServiceProviderRegistry

class Kernel:
    def __init__(self, container):
        self.container = container
        self.router = container.make(Router)
        self.providers = []

    def bootstrap(self):
        self.register_providers()
        self.boot_providers()

    def register_providers(self):
        # Ensure correct passing of container as 'app'
        for provider_class in self.container.providers:
            provider = provider_class(self.container)  # Pass the container as the 'app'
            self.providers.append(provider)
            provider.register()  # Call register without passing container since it's available in the provider instance

    def boot_providers(self):
        for provider in self.providers:
            provider.boot()  # Call boot without passing container

    def handle(self, request: Request):
        try:
            # Match route and execute handler
            response = self.router.dispatch(request)
        except Exception as e:
            response = Response(str(e), status=500)
        return response

    def terminate(self, request: Request, response: Response):
        print("Cleaning up request...")
