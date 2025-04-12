#!/usr/bin/env python3
import sys
import os


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure Python recognizes pyavel/ and its subdirectories
sys.path.insert(0, project_root)


# Print the default working directory
print(f"[*] Python's default working directory: {os.getcwd()}")

# Print working directory and Python's module search paths
print(f"[*] Python's default working directory: {os.getcwd()}")
print(f"[*] Python's module search paths:\n{sys.path}")



from core.main import start_framework  # Import the method from core/main.py

if __name__ == "__main__":
    start_framework()  # Call the core execution method