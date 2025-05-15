from abc import ABC, abstractmethod

class FileSystemElement(ABC):
    @abstractmethod
    def display(self, indent=""):
        pass

    @abstractmethod
    def get_size(self):
        pass