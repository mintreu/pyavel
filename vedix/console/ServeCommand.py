# vedix/commands/ServeCommand.py

import uvicorn
from bootstrap.app import app
from vedix.config import config

class ServeCommand:
    @staticmethod
    def register(subparsers):
        parser = subparsers.add_parser("serve", help="Run the application server")
        parser.add_argument("--host", default=config.get("host", "127.0.0.1"))
        parser.add_argument("--port", type=int, default=config.get("port", 8000))
        parser.set_defaults(func=ServeCommand.run)

    @staticmethod
    def run(args):
        uvicorn.run(app, host=args.host, port=args.port)
