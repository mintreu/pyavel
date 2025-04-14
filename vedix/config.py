# vedix/config.py

import json
import os

def config():
    config_path = os.path.join("config", "app.json")
    if os.path.exists(config_path):
        with open(config_path) as f:
            return json.load(f)
    return {}
