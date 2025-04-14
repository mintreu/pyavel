# vedix/middleware/logger.py

def log_request_middleware(request):
    print(f"[Logger] {request.method} {request.path}")
    return request