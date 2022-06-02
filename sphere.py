from three_space_figures import ThreeDimensionalFigure
from math import pi

class Sphere(ThreeDimensionalFigure):
    def __init__(self, radius: int):
        self.radius = radius

    def volume(self) -> float:
        return (4 / 3) * pi * self.radius ** 3

    def surface_area(self) -> float:
        return 4 * pi * self.radius ** 2

