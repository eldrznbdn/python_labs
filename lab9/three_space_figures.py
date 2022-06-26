from abc import ABC, abstractmethod


class ThreeDimensionalFigure(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass
