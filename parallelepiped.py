from three_space_figures import ThreeDimensionalFigure


class Parallelepiped(ThreeDimensionalFigure):
    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        return self.length * self.width * self.height

    def surface_area(self) -> float:
        return 4 * self.length * self.width + 2 * self.width * self.height