import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from bootstrap.app import Application

def test_all_providers():
    success = True

    print("\n🧪 [Testing Providers]")

    for provider_class in Application.providers:
        try:
            # Pass the Application container to the provider's constructor
            provider = provider_class(Application)
            provider.register()  # Call register without passing the container
            provider.boot()      # Call boot without passing the container
            print(f"✅ {provider_class.__name__} registered and booted.")
        except Exception as e:
            success = False
            print(f"❌ Error in {provider_class.__name__}: {e}")

    if success:
        print("✅ All providers loaded successfully.\n")
    else:
        print("❗ Some providers failed.\n")

if __name__ == "__main__":
    test_all_providers()
