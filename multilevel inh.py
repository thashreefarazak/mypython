class School:
    def open(self):
        print("school open")
class Class1(School):
    def started(self):
        print("class started")
class Student(Class1):
    def present(self):
        print("students presented")
obj=Student()
obj.started()
obj.present()
obj.open()