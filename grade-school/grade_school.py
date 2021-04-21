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
