class Student:

    count=0
    def __init__(self,name,id):
        self.name=name
        self.id=id
        Student.count+=1
        print("count:",Student.count)

    def display(self):
        print(self.id,self.name)

# getattr

s1=Student("raj",4)
s2=Student("jiya",6)
s3=Student("sita",56)

print(getattr(s1,'name'))
print(s1.name)

# setattr
# s1.id=10
setattr(s1,'id',10)
print(s1.id)


# hasattr
print(hasattr(s1,'id'))
print(hasattr(s2,'age'))


# delattr
delattr(s2,'id')
# print(s2.id)
print(hasattr(s3,'id'))

print(s1.__dict__)
print(s1.__module__)
print(s1.__doc__)
