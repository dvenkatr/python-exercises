plant_dict = {
    'C' : 'Clover',
    'G' : 'Grass',
    'R' : 'Radishes',
    'V' : 'Violets'
}

default_students = ['Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry']


class Garden:

    def __init__(self, diagram : str, students : list = default_students) -> list :
        self.diagram = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student) * 2 # Find index of the student among all the students
        plant_string = self.diagram[0][index : index + 2] + self.diagram[1][index : index + 2] # String representing the student's plants
        return [plant_dict[plant] for plant in plant_string] # List representing plant names
