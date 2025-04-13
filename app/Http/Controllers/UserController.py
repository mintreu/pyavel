# app/Controllers/UserController.py
from fastapi.responses import JSONResponse

class UserController:
    def login(self):
        return JSONResponse({"message": "Login page"})

    def register(self):
        return JSONResponse({"message": "Register page"})

    def dashboard(self):
        return JSONResponse({"message": "User dashboard"})

    def do_login(self):
        return JSONResponse({"message": "Logging in..."})

    def logout(self):
        return JSONResponse({"message": "Logged out"})
