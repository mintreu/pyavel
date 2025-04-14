# vedix/http/Request.py
from fastapi import Request as FastApiRequest
from starlette.requests import Request as StarletteRequest

class Request:

    def __init__(self, method, path, headers=None, query=None, body=None):
        self.method = method.upper()
        self.path = path
        self.headers = headers or {}
        self.query = query or {}
        self.body = body

    @staticmethod
    def capture(fastapi_request: StarletteRequest = None):
        """
        Capture request details from FastApi (or mock CLI/Tests)
        """
        if fastapi_request:
            return Request(
                method=fastapi_request.method,
                path=fastapi_request.url.path,
                headers=dict(fastapi_request.headers),
                query=dict(fastapi_request.query_params),
                body=None # For now; parse body if needed
            )
        return Request("Get", "/") # default fallback