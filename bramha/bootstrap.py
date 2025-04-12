import inspect
import os
# Assign root directory (Parent of bramha/)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def initialize_framework():
    """
    Initializes the Pyavel framework by resolving paths, classes, controllers, models, DB, views, cache, etc.
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

    # Use the config() shortcut now
    dd(builtins.__CONFIGS__)  # This will print the entire configuration object and exit.

    dd(config("app.app_name"))  # → 'Pyavel'

    # Register routes dynamically
    from bramha.route import Router
    Router.register_routes()

    # Initialize core kernel
    from bramha.kernel import Kernel
    Kernel.boot()

    print("[OK] Framework initialized successfully!")
