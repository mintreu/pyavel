import json
import pprint
import builtins

def load_helpers(root_dir, PROJECT_CONFIGS):
    """
    Initializes global variables for helpers and prepares shared config access.
    """
    builtins.__CONFIGS__ = PROJECT_CONFIGS
    print("[*] Global helper functions loaded!")

def config(key=None, default=None):
    """
    Access configuration values using dot notation.
    Example: config("app.debug") → True
    """
    CONFIGS = getattr(builtins, "__CONFIGS__", {})

    if key is None:
        return CONFIGS

    keys = key.split(".")
    value = CONFIGS

    try:
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return default

def dump(*args):
    pp = pprint.PrettyPrinter(indent=2)
    for arg in args:
        print("→")
        pp.pprint(arg)

def dd(*args):
    pp = pprint.PrettyPrinter(indent=2)
    for arg in args:
        print("→")
        pp.pprint(arg)
    exit()


def is_dev():
    return config("server.env", "production") == "development"

def is_prod():
    return config("server.env", "development") == "production"
