from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from parallelepiped import Parallelepiped
from dot import Dot
from segment import LineSegment


def main():
    cir = Circle(6)
    print(cir.area())

    rect = Rectangle(5, 8)
    print(rect.area())

    sphere = Sphere(3)
    print(sphere.volume())
    print(sphere.surface_area())

    parallelepiped = Parallelepiped(2, 4, 6)
    print(parallelepiped.volume())
    print(parallelepiped.surface_area())

    point1 = Dot(1, 4, 3)
    point2 = Dot(0, 2, 5)
    print(point1.x, point1.y, point1.z)
    print(point2.x, point2.y, point2.z)
    line = LineSegment(0, 9)
    print(line.length())


if __name__ == '__main__':
    main()
