#!/usr/bin/env python3
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Ensure Python recognizes pyavel/ and its subdirectories
sys.path.insert(0, project_root)

from core.main import start_framework  # Import the method from core/main.py

if __name__ == "__main__":
    start_framework()  # Call the core execution method