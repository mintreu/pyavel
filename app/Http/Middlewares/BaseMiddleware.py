from fastapi import Request
from abc import ABC, abstractmethod

class BaseMiddleware(ABC):
    @abstractmethod
    async def handle(self, request: Request, *args, **kwargs):
        """
        This method should be implemented by any subclass that needs middleware logic.
        """
        pass
