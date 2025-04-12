# routes/user_routes.py
from bramha.route import Router
from app.controllers.UserController import UserController

user = UserController()

Router.get("/login", user.login)
Router.get("/register", user.register)
Router.get("/dashboard", user.dashboard)
Router.post("/login", user.do_login)
Router.delete("/logout", user.logout)
