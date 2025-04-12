# ⚡ Pyavel - The Laravel-Inspired Python Framework  
> _Powered by **Bramha**, the creator of structure and flow._

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-yellow.svg)](https://python.org)

Official Repository: [github.com/mintreu/pyavel](https://github.com/mintreu/pyavel)

---

### 🚀 Introduction

**Pyavel** is a modern, lightweight Python framework inspired by **Laravel**. It gives you structure, flexibility, and power — without the overhead.  
Built for developers who want to code fast, stay organized, and love Laravel-style architecture.

---

### 🧠 Philosophy

> **“Pyavel is not just a framework — it's Bramha, the code creator.”**  
Just like Laravel in PHP, Pyavel helps you manage routes, controllers, helpers, and services in Python — all structured in a modular, readable, and extensible way.

---

### 📦 Features

- ⚙️ Laravel-style routing & controller system  
- 🔁 Custom autoloader (no repeated imports)  
- 🧱 MVC-style architecture (Models, Views, Controllers)  
- 🌱 Bootstrap loader for global config, helpers, and startup  
- 🔧 Global helper support (`dd()`, `greet()`, `now()` etc.)  
- ⚡ Lightweight and ready for CLI or HTTP extensions  
- 🧩 Plugin and service-provider architecture (planned)  

---

### 📁 Project Structure

```
pyavel/
├── main.py                 # Clean entry point
├── bootstrap.py            # Global loader (autoload, config, helpers)
├── autoloader.py           # Adds all necessary paths
├── helpers.py              # Global helper functions (dd, config, etc.)
├── config/
│   └── settings.json       # Your app settings and ENV info
├── app/
│   ├── controllers/        # Laravel-style controllers
│   ├── models/             # Optional models
│   └── services/           # Reusable service classes
├── core/
│   └── router.py           # Mini-router to resolve and call controllers
└── vendor/                 # External or local packages
```

---

### 🚀 Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/mintreu/pyavel.git
cd pyavel
```

#### 2. Run the App

```bash
python main.py
```

#### 3. Add a Route in `bootstrap.py`

```python
from core.router import Router
from app.controllers.UserController import UserController

Router.add("/login", UserController().login)
```

---

### 💻 Example Controller

```python
# app/controllers/UserController.py

class UserController:
    def login(self):
        return "User login successful"

    def logout(self):
        return "User logged out"
```

---

### ⚡ Global Helpers (like Laravel)

```python
dd("Debug this quickly")
print(greet("Krishzzi"))   # → Hello, Krishzzi
```

> No need to import — just call them from anywhere after `bootstrap`.

---

### 📚 Roadmap

- [ ] Built-in HTTP support (FastAPI or Flask integration)  
- [ ] Middleware pipeline  
- [ ] Artisan-like CLI tool  
- [ ] `.env` support & auto loader  
- [ ] View/template system (Jinja2-based)  
- [ ] Auto route loader from file (like Laravel routes/web.php)  
- [ ] Plugin & service providers  

---

### 🧘 Powered By Bramha

Pyavel is powered by **Bramha**, the creative essence. It helps developers start from *nothing*, and bring **structured flow** to life — cleanly, modularly, and predictably.

---

### 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

### 👨‍💻 Developed & Maintained by [@krishzzi](https://github.com/krishzzi)  
Inspired by Laravel, built for Python lovers.
