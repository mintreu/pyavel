# from famework.routing import Route
#
# from app.Http.Controllers.BlogController import BlogController
# from app.Http.Controllers.UserController import UserController
# from app.Http.Middlewares.AuthMiddleware import AuthMiddleware
#
#
# user = UserController()
# blog = BlogController()
#
# # routing.get("/login", user.login)
# # routing.get("/register", user.register).name('register')
# # routing.get("/dashboard", user.dashboard).middleware(AuthMiddleware())
# # routing.get("/blog/view/{url: url}", blog.view)
# # routing.get("/blog/read/{id: id}", blog.read)
#
#
# Route.get("/login", user.login)
# Route.post("/register", user.register).name("register")
# Route.put("/profile/update", user.update)
# Route.delete("/user/{id: id}", user.delete).middleware(AuthMiddleware())
# Route.any("/debug", blog.debug)  # Will be registered for all HTTP methods
# # routing.get("/secure", user.dashboard).middleware(AuthMiddleware()).signed().name("secure.post")
# Route.get("/secure", user.dashboard).middleware(AuthMiddleware()).signed().name("secure.post")
#
#
#
# Route.get("/user/check/{name: name}", user.read).middleware(AuthMiddleware())
#


from app.Http.Controllers import HomeController
from vedix.routing import Route

# Defining Routes
Route.get("/", HomeController.index)
Route.get("/about", HomeController.about)
