# vedix/http/Response.py
from fastapi.responses import JSONResponse,HTMLResponse,PlainTextResponse
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

class Response:
    env = Environment(
        loader=FileSystemLoader(os.path.join(os.getcwd(), "resources/views")),
        autoescape=select_autoescape(['html',"xml"])
    )


    def __init__(self, content,status=200, headers=None, content_type="text/html", is_view=False, context=None):
        self.content = content
        self.status = status
        self.headers = headers or {}
        self.content_type = content_type
        self.is_view = is_view,
        self.context = context or {}

    def send(self):
        if self.is_view:
            try:
                template = self.env.get_template(self.content)
                rendered = template.render(**self.context)
                return HTMLResponse(content=rendered, status_code=self.status, headers=self.headers)
            except Exception as e:
                return PlainTextResponse(f"Template error: {e}", status_code=500)

        if self.content_type == "application/json":
            return JSONResponse(content=self.content, status_code=self.status, headers=self.headers)
        elif self.content_type == "text/plain":
            return PlainTextResponse(content=self.content,status_code=self.status,headers=self.headers)
        else:
            return HTMLResponse(content=self.content,status_code=self.status,headers=self.headers)

