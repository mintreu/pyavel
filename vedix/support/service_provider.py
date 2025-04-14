# vedix/support/service_provider.py


class ServiceProvider:
    def __init__(self, app=None):
        self.app = app

    def register(self, app=None):
        pass

    def boot(self, app=None):
        pass


class ServiceProviderRegistry:
    def __init__(self):
        self.providers = []

    def register(self, provider):
        self.providers.append(provider)

    def boot(self):
        for provider in self.providers:
            provider.register()
            provider.boot()
