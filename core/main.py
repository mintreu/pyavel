#!/usr/bin/env python3
import os
import sys
import importlib.util

from bramha.Helpers import config, is_prod, is_dev

def ensure_root():
    caller_file = os.path.abspath(sys.argv[0])
    if not caller_file.endswith(os.path.join("public", "main.py")):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        sys.path.insert(0, project_root)

ensure_root()

from bramha.bootstrap import initialize_framework

# ✅ Export app for uvicorn
app = initialize_framework()

def start_framework():
    """
    Starts the Pyavel framework and launches the FastAPI server using config-based host and port.
    """
    host = config("server.host", "127.0.0.1")
    port = int(config("server.port", 8000))
    env = config("server.env", "production")

    import uvicorn

    # Dynamically build module path like: 'yourproject.core.main:app'
    module_path = __name__ + ":app"

    uvicorn.run(module_path, host=host, port=port, reload=is_prod())
