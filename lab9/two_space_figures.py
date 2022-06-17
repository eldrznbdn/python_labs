from abc import ABC, abstractmethod


class TwoDimensionalFigure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

