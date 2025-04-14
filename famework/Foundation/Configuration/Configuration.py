import os
import json
import importlib.util

def load_config(root_dir):
    """
    Loads all configuration files inside the `config/` directory and ensures all values are stored properly.
    """
    config_dir = os.path.join(root_dir, "config")
    all_config = {}

    if not os.path.exists(config_dir):
        print("[X] Config directory not found! Default settings will be used.")
        return {}

    # Load JSON config (settings.json)
    json_config_path = os.path.join(config_dir, "settings.json")
    if os.path.exists(json_config_path):
        with open(json_config_path, "r") as json_file:
            try:
                json_data = json.load(json_file)
                all_config["settings"] = json_data  # Store as-is
                print("[*] Loaded settings.json")
            except json.JSONDecodeError:
                print("[X] Error parsing settings.json. Check JSON formatting.")

    # Load Python-based configs dynamically
    for filename in os.listdir(config_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            config_name = filename[:-3]  # Remove ".py" extension
            config_path = os.path.join(config_dir, filename)

            try:
                spec = importlib.util.spec_from_file_location(config_name, config_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "CONFIG"):  # Ensure CONFIG is present
                    config_data = module.CONFIG

                    # If CONFIG is a list, store it as is
                    if isinstance(config_data, (dict, list)):
                        all_config[config_name] = config_data
                    else:
                        print(f"[X] Invalid CONFIG format in {config_name}.py. Must be dict or list.")

                    print(f"[*] Loaded {config_name}.py")

            except Exception as e:
                print(f"[X] Error loading {config_name}.py: {e}")

    print("[OK] All configurations loaded successfully!")
    return all_config