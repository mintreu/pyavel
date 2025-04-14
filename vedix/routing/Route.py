# vedix/routing/Route.py

from vedix.http.Response import Response
from jinja2 import Environment, FileSystemLoader
import os

class Route:
    routes = {
        'GET': {},
        'POST': {},
    }

    @classmethod
    def get(cls, path, handler):
        cls.routes['GET'][path] = handler

    @classmethod
    def post(cls, path, handler):
        cls.routes['POST'][path] = handler

    @classmethod
    def match(cls, method, path):
        return cls.routes.get(method, {}).get(path)