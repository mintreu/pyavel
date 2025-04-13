from fastapi import Request

class BlogController:
    def view(self, request: Request):
        # Your login logic here
        return {"message": "Login successful"}

    def read(self, request: Request):
        # Your register logic here
        return {"message": "Register successful"}

    def debug(self, request: Request):
        # Your register logic here
        return {"message": "Register successful"}