# #!/usr/bin/env python3
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

# from core.main import start_framework
#
# if __name__ == "__main__":
#     start_framework()





# public/main.py

from bootstrap.app import Application
from vedix.foundation.http.Kernel import Kernel
from vedix.http.Request import Request

kernel = Application.make(Kernel)
kernel.bootstrap()

request = Request.capture()
response = kernel.handle(request)
response.send()
kernel.terminate(request, response)
