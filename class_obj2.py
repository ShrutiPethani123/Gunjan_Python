class Student:
   
   
    # def __init__(self):
    #     print("second")
    #     self.age=70
    def __init__(self,age,name):
        self.age=age
        self.name=name
        print(self.name , self.age)

    def __init__(self,age):
        print("first")


s1=Student(80,"raj")
# s2=Student(100)
print(s1.age)
# print(s2.age)