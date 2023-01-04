class Student:
   
    def __init__(self,age):
        print("first")
    def __init__(self):
        print("second")
        self.age=70


s1=Student(80)
# s2=Student(100)
print(s1.age)
# print(s2.age)