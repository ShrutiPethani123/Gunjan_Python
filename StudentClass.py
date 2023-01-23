class Student:

    count=0
    def __init__(self,name,id):
        self.name=name
        self.id=id
        Student.count+=1
        print("count:",Student.count)

    def display(self):
        print(self.id,self.name)

s1=Student("raj",4)
s2=Student("jiya",6)
s3=Student("sita",56)

s1.display()
s2.display()

print(s1.count)