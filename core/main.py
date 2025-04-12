#!/usr/bin/env python3

from bramha.bootstrap import initialize_framework

def start_framework():
    """
    Starts the Pyavel framework by calling `initialize_framework()` from bootstrap.
    This method ensures all necessary components are loaded.
    """
    print("[*] Starting Pyavel framework...")
    initialize_framework()  # Load everything via bootstrap.py

if __name__ == "__main__":
    start_framework()