# vedix/commands/MakeController.py

import os
from vedix.utils.stub_loader import render_stub

class MakeController:
    @staticmethod
    def register(subparsers):
        parser = subparsers.add_parser("make:controller", help="Create a new controller")
        parser.add_argument("name")
        parser.set_defaults(func=MakeController.run)

    @staticmethod
    def run(args):
        path = f"app/Http/Controllers/{args.name}.py"
        content = render_stub("controller.stub", {"class": args.name})
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
        print(f"✅ Controller created: {path}")
