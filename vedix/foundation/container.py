# vedix/foundation/container.py

import inspect

class Container:
    def __init__(self):
        self.bindings = {}
        self.providers = []  # ✅ add this line

    def bind(self, key, cls):
        self.bindings[key] = cls

    def make(self, cls):
        cls_or_factory = self.bindings.get(cls, cls)

        if callable(cls_or_factory) and not inspect.isclass(cls_or_factory):
            return cls_or_factory(self)

        constructor = inspect.signature(cls_or_factory.__init__)
        parameters = list(constructor.parameters.values())[1:]  # skip 'self'

        dependencies = []
        for param in parameters:
            if param.annotation != inspect.Parameter.empty:
                dependency = self.make(param.annotation)
                dependencies.append(dependency)
            elif param.default != inspect.Parameter.empty:
                # ✅ Use default value (don’t raise error)
                continue
            else:
                raise ValueError(f"Cannot resolve dependency '{param.name}' for {cls_or_factory.__name__}")

        return cls_or_factory(*dependencies)
