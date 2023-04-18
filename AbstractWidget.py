

from abc import ABC, abstractmethod


class AbstractWidget(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def layout(self):
        pass