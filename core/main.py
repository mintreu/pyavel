#!/usr/bin/env python3
import os
import sys

def ensure_root():
    caller_file = os.path.abspath(sys.argv[0])

    if not caller_file.endswith(os.path.join("public", "main.py")):
        # Fix the root manually (we are being run directly, not from public/main.py)
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        sys.path.insert(0, project_root)

ensure_root()



from bramha.bootstrap import initialize_framework

def start_framework():
    """
    Starts the Pyavel framework by calling `initialize_framework()` from bootstrap.
    This method ensures all necessary components are loaded.
    """
    initialize_framework()  # Load everything via bootstrap.py

if __name__ == "__main__":
    start_framework()