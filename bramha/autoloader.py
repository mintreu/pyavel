import os
import sys
import importlib.util


def load_dependencies(root_path):
    """
    Autoloads packages from vendor/, controllers, models, and other app logic dynamically.
    """
    print("[*] Autoloading dependencies...")

    # ───── Load Vendor Packages ─────
    vendor_path = os.path.join(root_path, "vendor")
    if os.path.exists(vendor_path):
        sys.path.append(vendor_path)
        print("[OK] Vendor packages loaded.")

    # ───── Load Application Modules Recursively (app/*) ─────
    app_path = os.path.join(root_path, "app")
    load_recursive_modules(app_path, "app")

    # ───── Load Future Database Modules Recursively (database/*) ─────
    database_path = os.path.join(root_path, "database")
    if os.path.exists(database_path):  # Ensure database folder exists before loading
        load_recursive_modules(database_path, "database")

    print("[OK] All dependencies successfully loaded!")


def load_recursive_modules(directory, package_name):
    """
    Recursively scans directories and dynamically imports all Python files inside.
    This allows automatic loading of deeply nested controllers, models, and other framework components.
    """
    if not os.path.exists(directory):
        print(f"[!] Skipping {package_name}: Directory '{directory}' not found.")
        return

    for root, _, files in os.walk(directory):
        relative_package = package_name + "." + root.replace(directory, "").replace(os.sep, ".").strip(
            ".")  # Construct package name

        for filename in files:
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"{relative_package}.{filename[:-3]}" if relative_package else f"{package_name}.{filename[:-3]}"  # Remove .py extension

                try:
                    spec = importlib.util.spec_from_file_location(module_name, os.path.join(root, filename))
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    print(f"[OK] Loaded module: {module_name}")
                except Exception as e:
                    print(f"[X] Error loading {module_name}: {e}")