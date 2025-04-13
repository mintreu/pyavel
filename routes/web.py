# routes/user_routes.py
from app.Http.Controllers.UserController import UserController
from app.Http.Middlewares.AuthMiddleware import AuthMiddleware
from bramha.Route import Router


user = UserController()

Router.get("/login", user.login)
Router.get("/register", user.register)
# Router.get("/dashboard", user.dashboard)
# Router.post("/login", user.do_login)
# Router.delete("/logout", user.logout)
#
#
# Router.get("/dashboard", user.dashboard)  # No middleware required
Router.get("/dashboard", user.dashboard).middleware(AuthMiddleware)  # With middleware