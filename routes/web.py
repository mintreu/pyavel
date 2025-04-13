from app.Http.Controllers.BlogController import BlogController
from app.Http.Controllers.UserController import UserController
from app.Http.Middlewares.AuthMiddleware import AuthMiddleware
from bramha.Route.Route import Route

user = UserController()
blog = BlogController()

# Route.get("/login", user.login)
# Route.get("/register", user.register).name('register')
# Route.get("/dashboard", user.dashboard).middleware(AuthMiddleware())
# Route.get("/blog/view/{url: url}", blog.view)
# Route.get("/blog/read/{id: id}", blog.read)


Route.get("/login", user.login)
Route.post("/register", user.register).name("register")
Route.put("/profile/update", user.update)
Route.delete("/user/{id: id}", user.delete).middleware(AuthMiddleware())
Route.any("/debug", blog.debug)  # Will be registered for all HTTP methods
# Route.get("/secure", user.dashboard).middleware(AuthMiddleware()).signed().name("secure.post")
Route.get("/secure", user.dashboard).middleware(AuthMiddleware()).signed().name("secure.post")



Route.get("/user/check/{name: name}", user.read).middleware(AuthMiddleware())




