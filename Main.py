class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def aver_grade_s(self):
        result = 0
        if len(self.grades) != 0:
            for i in self.grades.values():
                result += sum(i)
            return result / len(self.grades)
        else:
            return 0

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self.aver_grade_s()}\n'
                  f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result

# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

    def __eq__(self, buddy):
        if isinstance(buddy, Student):
            return self.aver_grade_s() == buddy.aver_grade_s()
        else:
            return 'Неверное сравнение'

    def __lt__(self, buddy):
        if isinstance(buddy, Student):
            return self.aver_grade_s() < buddy.aver_grade_s()
        else:
            return 'Неверное сравнение'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def aver_grade_l(self):
        result = 0
        if len(self.grades) != 0:
            for i in self.grades.values():
                result += sum(i)
            return result / len(self.grades)
        else:
            return 'Нет оценок'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.aver_grade_l()}'
        return result

    def __eq__(self, colleague):
        if isinstance(colleague, Lecturer):
            return self.aver_grade_l() == colleague.aver_grade_l()
        else:
            return 'Неверное сравнение'

    def __lt__(self, colleague):
        if isinstance(colleague, Lecturer):
            return self.aver_grade_l() < colleague.aver_grade_l()
        else:
            return 'Неверное сравнение'


class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# .courses_in_progress += ['Python']

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)


def aver_students_course(students: list, course: str):
    num = 0
    num_2 = 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            for i in student.grades.get(course):
                num += i
                num_2 += 1
    return num/num_2


def aver_lecturer_course(lecturers: list, course: str):
    num = 0
    num_2 = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            for i in lecturer.grades.get(course):
                num += i
                num_2 += 1
    return num/num_2


student_1 = Student('Ivan', 'Ivanov', 'male')
student_2 = Student('Olga', 'Olgina', 'female')

# Все курсы: Black Magic, Necromancy, Voodoo, Poison crafting, Demonology, History of Heavy Metal, Blood sucking

student_1.finished_courses += ['Black Magic', 'Necromancy', 'Demonology']
student_1.courses_in_progress = ['Voodoo', 'Poison crafting', 'History of Heavy Metal']

student_2.finished_courses += ['Black Magic', 'Voodoo', 'Demonology']
student_2.courses_in_progress = ['Poison crafting', 'Demonology', 'Blood sucking']

lecturer_1 = Lecturer('Petr', 'Petrov')
lecturer_1.courses_attached = ['History of Heavy Metal', 'Necromancy', 'Demonology', 'Black Magic']
lecturer_2 = Lecturer('Fyodr', 'Fyodorov')
lecturer_2.courses_attached = ['Voodoo', 'Poison crafting', 'Blood sucking', 'Demonology']

reviewer_1 = Reviewer('Danila', 'Danilov')
reviewer_1.courses_attached = ['Necromancy', 'Poison crafting', 'History of Heavy Metal']
reviewer_2 = Reviewer('Alisa', 'Alisenko')
reviewer_2.courses_attached = ['Black Magic', 'Voodoo', 'Demonology', 'Blood sucking']



# print(student_1.grades)
# print(student_2.grades)
# print(reviewer_1.courses_attached)
# print(student_1.courses_in_progress)
# print(lecturer_1.grades)
# print(lecturer_1.courses_attached)
# print(student_1)
# print(student_1.grades.values())
# print(student_1.aver_grade_s())
# print(lecturer_1.aver_grade_l())

student_1.rate_lec(lecturer_1, 'Demonology', 8)
student_1.rate_lec(lecturer_2, 'Demonology', 6)
student_2.rate_lec(lecturer_1, 'Demonology', 8)
student_2.rate_lec(lecturer_2, 'Demonology', 7)

reviewer_1.rate_st(student_1, 'Poison crafting', 9)
reviewer_2.rate_st(student_1, 'Voodoo', 10)

print(student_1)
print(lecturer_1)
print(reviewer_1)

print(student_1 > student_2)
print(lecturer_1 < lecturer_2)

print(aver_students_course([student_1, student_2], 'Voodoo'))

print(aver_lecturer_course([lecturer_1, lecturer_2], 'Demonology'))