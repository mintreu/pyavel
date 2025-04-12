import os
import builtins
import inspect
import bramha.helpers
from bramha.karigar import main  # Import main from karigar

# Assign root directory (Parent of `bramha/`)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def load_helpers():
    """
    Registers all helper functions globally into Python's builtins.
    Automatically adds every function defined in `bramha.helpers`.
    """
    for name, func in inspect.getmembers(bramha.helpers, inspect.isfunction):
        builtins.__dict__[name] = func  # Add each function dynamically
    print("[*] Global helper functions registered!")



def run_karigar():
    """
    Bridge function to run the karigar main function.
    Future modifications or pre-processing steps can be added here.
    """
    main()  # Execute main from karigar

def initialize_framework():
    """
    Initializes the Pyavel framework by resolving paths, classes, controllers, models, DB, views, cache, etc.
    """
    print("[*] Initializing Pyavel framework via bootstrap...")


    # Register global helpers
    load_helpers()

    dd('hello');

    # Autoload dependencies safely without cyclic imports
    from bramha.autoloader import load_dependencies
    load_dependencies(ROOT_DIR)

    # Load configurations
    from bramha.configuration import load_config
    load_config(ROOT_DIR)

    # Register routes dynamically
    from bramha.route import Router
    Router.register_routes()

    # Initialize core kernel
    from bramha.kernel import Kernel
    Kernel.boot()

    print("[OK] Framework initialized successfully!")