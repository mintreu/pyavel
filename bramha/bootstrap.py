import os
from bramha.karigar import main  # Import main from karigar

# Assign root directory (Parent of `bramha/`)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

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

    # Autoload dependencies safely without cyclic imports
    from bramha.autoloader import load_dependencies
    load_dependencies(ROOT_DIR)

    # Load configurations
    from config.settings import load_config
    load_config()

    # Register routes dynamically
    from bramha.route import Router
    Router.register_routes()

    # Initialize core kernel
    from bramha.kernel import Kernel
    Kernel.boot()

    print("[OK] Framework initialized successfully!")