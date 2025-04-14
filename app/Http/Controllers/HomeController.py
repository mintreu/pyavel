from vedix.http.Request import Request
from vedix.http.Response import Response

class HomeController:
    def index(self, request: Request) -> Response:
        return Response("Welcome to the Home Page!")

    def about(self, request: Request) -> Response:
        return Response("About Us!")
