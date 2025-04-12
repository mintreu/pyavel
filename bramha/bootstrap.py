import inspect
import os
from fastapi import FastAPI

# Assign root directory (Parent of bramha/)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Main Function Called From main.py
def initialize_framework() -> FastAPI:
    """
    Initializes the Pyavel framework and returns a FastAPI app instance.
    """
    print("[*] Initializing Pyavel framework via bootstrap...")

    # Load configurations
    from bramha.configuration import load_config
    all_configs = load_config(ROOT_DIR)

    # Store in builtins for global access if needed
    import builtins
    builtins.configs = all_configs

    # Load helper methods and pass the config
    import bramha.helpers
    bramha.helpers.load_helpers(ROOT_DIR, all_configs)

    # Register all helper functions into builtins
    for name, func in inspect.getmembers(bramha.helpers, inspect.isfunction):
        builtins.__dict__[name] = func

    print("[*] Global helper functions registered!")

    # # Initialize core kernel
    # from bramha.kernel import Kernel
    # Kernel.boot()

    # Prepare FastAPI app
    app = FastAPI()

    # Register routes dynamically
    from bramha.route import Router
    Router.register_routes()

    # Register Laravel-style routes to FastAPI
    for method, path, handler in Router.registered_routes:
        if method == "GET":
            app.get(path)(handler)
        elif method == "POST":
            app.post(path)(handler)
        elif method == "PUT":
            app.put(path)(handler)
        elif method == "DELETE":
            app.delete(path)(handler)
        else:
            print(f"[X] Unsupported HTTP method: {method} for path: {path}")

    print("[OK] Framework initialized successfully!")
    return app
