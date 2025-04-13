# bramha/Route/Route.py
import os
import importlib.util
from typing import List, Dict


class RouteManager:
    routes = []

    def __init__(self):
        self.local_routes = []

    def _add_route(self, method, path, handler):
        route = {
            "method": method,
            "path": path,
            "handler": handler,
            "name": None,
            "middleware": None,
            "parameters": self.extract_parameters(path),
            "sign_route": False  # default is False
        }
        self.local_routes.append(route)
        return self

    def get(self, path, handler):
        return self._add_route("GET", path, handler)

    def post(self, path, handler):
        return self._add_route("POST", path, handler)

    def put(self, path, handler):
        return self._add_route("PUT", path, handler)

    def patch(self, path, handler):
        return self._add_route("PATCH", path, handler)

    def delete(self, path, handler):
        return self._add_route("DELETE", path, handler)

    def options(self, path, handler):
        return self._add_route("OPTIONS", path, handler)

    def any(self, path, handler):
        for method in ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]:
            self._add_route(method, path, handler)
        return self

    def name(self, route_name):
        self.local_routes[-1]["name"] = route_name
        return self

    def signed(self):
        self.local_routes[-1]["sign_route"] = True
        return self

    def unsigned(self):
        self.local_routes[-1]["sign_route"] = False
        return self

    def middleware(self, middleware_class):
        self.local_routes[-1]["middleware"] = middleware_class
        return self

    def register_routes(self, root_dir):
        routes_dir = os.path.join(root_dir, "routes")
        for filename in os.listdir(routes_dir):
            if filename.endswith(".py"):
                filepath = os.path.join(routes_dir, filename)
                spec = importlib.util.spec_from_file_location("dynamic_routes", filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
        self.routes.extend(self.local_routes)

    def getAllRoutes(self) -> List[Dict]:
        return self.routes

    def extract_parameters(self, path):
        import re
        return re.findall(r'{(\w+):\s*\w+}', path)


# Global Route Singleton
Route = RouteManager()
