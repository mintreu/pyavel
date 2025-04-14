# vedix/support/provider_loader.py

import importlib.util
import inspect
import os
from vedix.support.service_provider import ServiceProvider


def discover_providers(directory: str, module_prefix: str):
    discovered = []

    for filename in os.listdir(directory):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            full_module_name = f"{module_prefix}.{module_name}"

            spec = importlib.util.find_spec(full_module_name)
            if spec is None:
                continue

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, ServiceProvider) and obj is not ServiceProvider:
                    discovered.append(obj)

    return discovered
