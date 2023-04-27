

from abc import ABC, abstractmethod


class Filter(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def filter_trajectories(self, trajectories, key, arguments):
        pass

    @property
    def filtered_trajectories(self):
        pass
