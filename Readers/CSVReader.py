

from abc import ABC, abstractmethod


# Parent class for file readers
class CSVReader(ABC):
    def __init__(self, csv_path):
        self.__csv_path = csv_path  # File path

    @abstractmethod
    def set_csv_data(self, csv_path):
        pass

    @property
    def csv_data(self):
        return self.__csv_data

    @abstractmethod
    def process_data(self):
        pass
