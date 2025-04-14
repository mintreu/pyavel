# vedix/routing/Router.py

from vedix.routing.Route import Route
from vedix.http.Request import Request
from vedix.http.Response import Response
from jinja2 import Environment, FileSystemLoader

class Router:
    def __init__(self, view_env=None):
        self.env = view_env or Environment(loader=FileSystemLoader('resources/views'))

    def dispatch(self, request: Request):
        handler = Route.match(request.method, request.path)
        if handler:
            result = handler(request)
            if isinstance(result, str):
                return Response(result)
            elif isinstance(result, dict) and 'view' in result:
                template = self.env.get_template(result['view'])
                return Response(template.render(result.get('data', {})), content_type='text/html')
            else:
                return Response(result)
        return Response("404 Not Found", status=404)
