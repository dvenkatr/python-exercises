'''
# Bonus points to deal with mutable data structures

In accordance with the Python philosophy, I have prefixed an underscore 
to the data member to indicate that it is private.

https://docs.python.org/3/tutorial/classes.html#tut-private
https://stackoverflow.com/questions/2064202/private-members-in-python
'''

from collections import defaultdict

class School:
    def __init__(self) -> None:
        self._students = defaultdict(list)

    def add_student(self, name : str, grade : int) -> None:
        self._students[grade].append(name)

    def roster(self) -> list:
        return [student for grade, students in sorted(self._students.items()) for student in sorted(students)]

    def grade(self, grade_number : int) -> list:
            return sorted(self._students[grade_number])
