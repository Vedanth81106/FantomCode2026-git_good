from abc import ABC, abstractmethod
from fastapi import Request
from typing import Any

class BaseExtractor(ABC):
    @abstractmethod
    async def extract(self, request: Request) -> Any:
        pass