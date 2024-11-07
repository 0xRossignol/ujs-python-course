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


print('------------student1-----------')
s1 = Student('jack', 18, 'male',
             'class1', 114514,
             {
                 'English': 99,
                 'Chinese': 97,
                 'Math': 100})
s1.print_info()

print('------------student2-----------')
s2 = Student('lucy', 19, 'female',
             'class2', 114554,
             {
                 'English': 92,
                 'Chinese': 91,
                 'Math': 16})
s2.print_info()

print('------------teacher1-----------')
t1 = Teacher('Mike', 56, 'male',
             'computer', 541,
             ['intro of cs', 'math for cs', 'cs graph'], 8555)
t1.print_info()