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
    def __init__(self, student: Student):
        self.left = None
        self.right = None
        self.student = student

    def insert_by_rating(self, student: Student):
        if self.student:
            if student.rating < self.student.rating:
                if self.left is None:
                    self.left = Node(student)
                else:
                    self.left.insert_by_rating(student)
            elif student.rating > self.student.rating:
                if self.right is None:
                    self.right = Node(student)
                else:
                    self.right.insert_by_rating(student)
            else:
                self.student = student


