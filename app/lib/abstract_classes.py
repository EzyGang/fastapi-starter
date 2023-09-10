from abc import ABC, abstractmethod
from typing import Any


class AbstractUseCase(ABC):
    @abstractmethod
    async def execute(self) -> Any:
        ...
