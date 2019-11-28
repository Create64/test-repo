students = []


class Student:
    school_name = "S P"

    def __init__(self, name, student_id=321):
        self.name = name
        self.student_id = student_id
        students.append(student)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "S H"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "_HS"


james = HighSchoolStudent("james")
print(james.get_name_capitalize())