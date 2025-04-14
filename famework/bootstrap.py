import inspect
import os
import re
from fastapi import FastAPI, Depends
from functools import wraps

from famework import routing
from famework.routing import Route

# Assign root directory (Parent of famework/)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Convert `{id: id}` to `{id}` for FastAPI compatibility
def convert_path(path):
    return re.sub(r'{(\w+):\s*\w+}', r'{\1}', path)

# Wrap handler to safely attach metadata
from inspect import iscoroutinefunction

def wrap_handler(handler, sign_route=False, route_name=None):
    if iscoroutinefunction(handler):
        @wraps(handler)
        async def wrapper(*args, **kwargs):
            return await handler(*args, **kwargs)
    else:
        @wraps(handler)
        def wrapper(*args, **kwargs):
            return handler(*args, **kwargs)

    wrapper.__sign_route__ = sign_route
    wrapper.__route_name__ = route_name
    return wrapper


# Dynamically register all routes to FastAPI
def register_fastapi_routes(app, all_routes):
    for route in all_routes:
        middleware = route.get("middleware")
        deps = [Depends(middleware)] if middleware else []

        method = route.get("method")
        path = convert_path(route.get("path"))
        handler = route.get("handler")
        route_name = route.get("name")
        sign_route = route.get("sign_route", False)

        wrapped_handler = wrap_handler(handler, sign_route, route_name)

        route_params = {
            "dependencies": deps,
        }

        if route_name:
            route_params["name"] = route_name

        # If method is "ANY", register all supported methods
        if method == "ANY":
            for m in ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]:
                getattr(app, m.lower())(path, **route_params)(wrapped_handler)
        else:
            method_func = getattr(app, method.lower(), None)
            if method_func:
                method_func(path, **route_params)(wrapped_handler)


# Main Function Called From main.py
def initialize_framework() -> FastAPI:
    """
    Initializes the famework famework and returns a FastAPI app instance.
    """
    print("[*] Initializing famework famework via bootstrap...")

    # Load configurations
    from famework.Foundation.Configuration.Configuration import load_config
    all_configs = load_config(ROOT_DIR)

    # Store in builtins for global access if needed
    import builtins
    builtins.configs = all_configs

    # Load helper methods and pass the config
    import famework.Foundation.helpers
    famework.Foundation.helpers.load_helpers(ROOT_DIR, all_configs)

    # Register all helper functions into builtins
    for name, func in inspect.getmembers(famework.Foundation.helpers, inspect.isfunction):
        builtins.__dict__[name] = func

    print("[*] Global helper functions registered!")

    # Prepare FastAPI app
    app = FastAPI()

    # Register Laravel-style routes
    Route.register_routes(ROOT_DIR)
    all_routes = Route.getAllRoutes()
    register_fastapi_routes(app, all_routes)

    print("[OK] Framework initialized successfully!")
    return app


class App:
    pass