import sys
import os

# ─── Colors ─────────────────────────────────────────────
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
CYAN = "\033[96m"

# ─── Entry ──────────────────────────────────────────────
def main():
    args = sys.argv[1:]

    if not args:
        print(f"{BOLD}{BLUE}Pyavel CLI - Karigar 🛠️{RESET}")
        print(f"{CYAN}Usage:{RESET} karigar <command> [options]")
        return

    command = args[0]

    if command == "list":
        print(f"{YELLOW}Available commands:{RESET}")
        print(f"  {GREEN}make:controller <Name>{RESET}")
        print(f"  {GREEN}make:model <Name>{RESET}")
        print(f"  {GREEN}make:service <Name>{RESET}")
    elif command == "make:controller" and len(args) == 2:
        name = args[1]
        make_stub(name, "controller")
    elif command == "make:model" and len(args) == 2:
        name = args[1]
        make_stub(name, "model")
    elif command == "make:service" and len(args) == 2:
        name = args[1]
        make_stub(name, "service")
    else:
        print(f"{RED}❌ Unknown command:{RESET} {command}")

# ─── Generator ──────────────────────────────────────────
def make_stub(name, type_):
    folder = {
        "controller": "app/controllers",
        "model": "app/models",
        "service": "app/services"
    }.get(type_)

    if not folder:
        print(f"{RED}Invalid type.{RESET}")
        return

    os.makedirs(folder, exist_ok=True)
    full_path = os.path.abspath(os.path.join(folder, f"{name}.py"))

    if os.path.exists(full_path):
        print(f"{YELLOW}[!] {type_.capitalize()} '{name}' already exists at:{RESET} {full_path}")
        return

    template = f"""class {name}:
    def __init__(self):
        pass
"""

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(template)

    print(f"{GREEN}[✔] {type_.capitalize()} created:{RESET} {full_path}")
