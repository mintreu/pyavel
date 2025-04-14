# bootstrap/app.py

import os
from vedix.foundation.container import Container
from vedix.foundation.http.Kernel import Kernel
from vedix.support.provider_loader import discover_providers
from config.providers import ENABLED_PROVIDERS

# ──────────────────────────────────────────────────────────────
# ✅ 1. Create the Global Application Container (DI System)
# ──────────────────────────────────────────────────────────────

# This acts like Laravel's IoC container (App::make)
Application = Container()

# Let the container resolve itself when asked
Application.bind(Container, lambda: Application)

# Register the HTTP Kernel (Request/Response pipeline)
Application.bind(Kernel, lambda container: Kernel(container))


# ──────────────────────────────────────────────────────────────
# ✅ 2. Auto-Discover Core and User Service Providers
# ──────────────────────────────────────────────────────────────

# Discover core framework-level providers from vedix/providers
core_providers = discover_providers("vedix/providers", "vedix.providers")

# Discover app-specific or override providers from app/Providers
user_providers = discover_providers("app/Providers", "app.Providers")


# Merge and filter providers
all_providers = core_providers + user_providers

for provider in all_providers:
    fqcn = f"{provider.__module__}.{provider.__name__}"
    if ENABLED_PROVIDERS.get(fqcn, True):  # Default is enabled
        Application.providers.append(provider)

# Merge all discovered providers into Application
#Application.providers.extend(core_providers + user_providers)


# ──────────────────────────────────────────────────────────────
# ✅ 3. Bind Manually Required Services (if needed)
# ──────────────────────────────────────────────────────────────

# This is an example of aliasing 'view_env' to jinja2 env via 'view'
# So user can do app.make('view_env') anywhere
Application.bind('view_env', lambda container: container.make('view'))


# ──────────────────────────────────────────────────────────────
# 🧪 4. Debug: Print Discovered Providers
# ──────────────────────────────────────────────────────────────

print("\n🔍 [Service Provider Discovery]")
for provider in core_providers:
    print(f"✔️ Core Provider: {provider.__module__}.{provider.__name__}")
for provider in user_providers:
    print(f"✔️ App Provider : {provider.__module__}.{provider.__name__}")
print("✅ Provider discovery complete.\n")

