class Person:

    def __init__(self, name: str, age: int, sex: str):
        self.name = name
        self.age = age
        self.sex = sex

    def print_info(self):
        print("name: " + self.name +
              "\nage: " + str(self.age) +
              '\nsex: ' + self.sex)


class Student(Person):
    count: int = 100

    def __init__(self, name: str, age: int,
                 sex: str, classes: str, student_id: int, score: dict):
        super().__init__(name, age, sex)
        self.classes = classes
        self.student_id = student_id
        self.score = score
        Student.count += 1

    def print_info(self):
        super().print_info()
        print("classes: " + self.classes +
              "\nstudent_id: " + str(self.student_id) +
              "\nscore: " + str(self.score) +
              '\ntotal: ' + str(self.count))


class Teacher(Person):

    def __init__(self,
                 name: str, age: int, sex: str,
                 department: str, teacher_id: int, course: list, salary: int):
        super().__init__(name, age, sex)
        self.department = department
        self.teacher_id = teacher_id
        self.course = course
        self.salary = salary

    def print_info(self):
        super().print_info()
        print('department: ' + self.department +
              '\nteacher_id: ' + str(self.teacher_id) +
              '\ncourse: ' + str(self.course) +
              '\nsalary: ' + str(self.salary))


class StuTeacher(Student, Teacher):
    def __init__(self, name: str, age: int, sex: str,
                 classes: str, student_id: int, score: dict,
                 department: str, teacher_id: int, course: list, salary: int):
        # 调用 Person 的构造函数
        Person.__init__(self, name, age, sex)
        # 初始化 Student 和 Teacher 的特有属性
        self.classes = classes
        self.student_id = student_id
        self.score = score
        self.department = department
        self.teacher_id = teacher_id
        self.course = course
        self.salary = salary
        Student.count += 1

    def print_info(self):
        print("TeachingAssistant Information:")
        Person.print_info(self)
        print("classes: " + self.classes +
              "\nstudent_id: " + str(self.student_id) +
              "\nscore: " + str(self.score) +
              "\ndepartment: " + self.department +
              "\nteacher_id: " + str(self.teacher_id) +
              "\ncourse: " + str(self.course) +
              "\nsalary: " + str(self.salary) +
              '\ntotal: ' + str(self.count))


ta = StuTeacher(
    name="Alex", age=25, sex="Male",
    classes="Math 101", student_id=12345, score={"Math": 95, "Science": 88},
    department="Mathematics", teacher_id=67890, course=["Algebra", "Calculus"], salary=5000
)

ta.print_info()
