# vedix/console/KarigarKernel.py

import argparse
from vedix.commands.ServeCommand import ServeCommand
from vedix.commands.MakeController import MakeController
from vedix.commands.MakeModel import MakeModel
from vedix.commands.MakeMiddleware import MakeMiddleware

class KarigarKernel:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Karigar CLI")
        subparsers = self.parser.add_subparsers(dest="command")

        # Registering commands
        ServeCommand.register(subparsers)
        MakeController.register(subparsers)
        MakeModel.register(subparsers)
        MakeMiddleware.register(subparsers)

    def handle(self):
        args = self.parser.parse_args()
        if not hasattr(args, 'func'):
            self.parser.print_help()
        else:
            args.func(args)
