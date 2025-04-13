from fastapi import Request

class AuthMiddleware:
    async def handle(self, request: Request, call_next):
        """Middleware logic before reaching the endpoint"""
        dd('sadf')
        if not request.cookies.get("user_token"):
            from fastapi.responses import JSONResponse
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        return await call_next(request)  # Proceed to the actual route handler