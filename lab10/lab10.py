class Student:
    def __init__(self, surname, name, group, date_of_birth, rating):
        self.surname = surname
        self.name = name
        self.group = group
        self.date_of_birth = date_of_birth
        self.rating = rating

    def __str__(self):
        return f"Student(surname : {self.surname},name : {self.name},group : {self.group}," \
               f"date_of_birth : {self.date_of_birth},rating : {self.rating})"


class Node:
    def __init__(self, data: Student):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data: Student):
        if self.data:
            if data.rating < self.data.rating:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif self.data.rating < data.rating:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_by_rating(self, rating: int):
        if self.left:
            self.left.print()
        if self.data and self.data.rating > rating:
            print(self.data)
        if self.right:
            self.right.print()

    def remove_by_group(self, group: str):
        if self.data and self.data.group == group:
            left = self.left
            right = self.right
            if left:
                self.data = left.data
                self.left = left.left
                self.right = left.right
                if right:
                    self.insert(right)
            elif right:
                self.data = right.data
                self.right = right.right
                self.right = right.left

        else:
            if self.left:
                self.left.remove_by_group(group)
            if self.right:
                self.right.remove_by_group(group)

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()


def main():
    first = Student("Petya", "Harry", "IP - 21", 1994, 87)
    second = Student("Nicolenco", "vasiliy", "KI - 11", 1995, 95)
    third = Student("Markus", "Valeriy", "IP - 23", 1993, 90)

    root = Node(first)
    root.insert(second)
    root.insert(third)
    root.print()
    root.print_by_rating(88)
    root.remove_by_group("KI-11")
    root.print()


if __name__ == "__main__":
    main()


