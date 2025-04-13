from fastapi import Request

class UserController:
    async def login(self, request: Request):
        return {"message": "Login successful"}

    def register(self, request: Request):
        return {"message": "Register successful"}

    def update(self, request: Request):
        return {"message": "Update successful"}

    def delete(self, request: Request):
        return {"message": "Delete successful"}

    async def dashboard(self, request: Request):
        return {"message": "Dashboard"}

    async def read(self, request: Request, name: str):
        # Just prints the name from the URL
        return {"message": f"User check for: {name}"}
