from abc import ABC, abstractmethod

class GeomFigure(ABC):
    @abstractmethod
    def square(self):
        pass