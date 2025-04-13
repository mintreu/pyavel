from fastapi import Request, HTTPException, status

class AuthMiddleware:
    def __init__(self):
        pass

    def __call__(self, request: Request):
        print("AuthMiddleware called!")

        # EXAMPLE AUTH CHECK:
        auth_header = request.headers.get("Authorization")

        if not auth_header or auth_header != "Bearer super-secret-token":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
            )

        # Optionally attach user info to request.state
        request.state.user = {"id": 1, "name": "Test User"}

        return True
