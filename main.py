class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grades_lector(self, lector, courses, grades):
        if isinstance(lector, Lecturer) and courses in lector.courses_attached and courses in self.courses_in_progress:
            if courses in lector.grades_lector:
                lector.grades_lector[courses] += [grades]
            else:
                lector.grades_lector[courses] = [grades]
        else:
            return "Ошибка"

    def __str__(self):
        print("Имя: Ruoy")
        print("Фамилия: Eman")
        print("Средняя оценка за домашние задания: 9.9")
        print("Курсы в процессе изучения: Python, Git")
        print("Завершенные курсы: Введение в программирование")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades_lector = {}
        super().__init__(name, surname)

    def __str__(self):
        print("Имя: Some")
        print("Фамилия: Buddy")
        print("Средняя оценка за домашние задания: 9.9")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        print("Имя: Some")
        print("Фамилия: Buddy")


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_lector = Lecturer("Александр", "Логинов")
best_lector.courses_attached += ['Python']

best_student.grades_lector(best_lector, 'Python', 10)
print(best_lector.grades_lector)

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
best_student.__str__()
