from math import sqrt


class LineSegment:
    def __init__(self, begin: int, end: int):
        self.begin = begin
        self.end = end

    def length(self) -> float:
        return sqrt(self.end - self.begin)

