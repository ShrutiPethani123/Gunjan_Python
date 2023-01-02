# Function
# use - code reusability

"""
with r.t with arg
with r.t without arg
withot r.t with arg
withot r.t without arg


"""

def display():
    print("HELLO!!")

def display2(name):
    print("Hello My name is ",name)

def add(a,b):
    return a+b

def factorial():
    n=int(input("Enter a no:"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

display()
display2("shruti")
display2("Gunjan")
print(add(3,4))
print(factorial())

# Arbitary argument 

def studentName(*name):
    # print("Name of student is: " , name[0])
    for i in name:
        print("Name of student is: ",i)

studentName("ajay",'jaya')
studentName("ram",'sita','laxman','ravan')

# Keyword argument

def fullName(fname,lname,mname):
    print(f"{fname} - {mname} - {lname}")

fullName(fname="joy",mname="roy",lname="abc")

# Default Argument

def my_counrty(con="india"):
    print("My Country name is ",con)

my_counrty()
my_counrty('canada')


# 2.

def student_details(name,id,dep="IT"):
    print(name , " ", dep , " ", id)

student_details("Gunjan",25)
student_details("ram",60,"CP")


# Arbitary Keyword argument
# **

def details(**key):
    print("Name of student is",key["name"]," and age is ",key['age'])

details(name="ram",age=50)


# passing list in argument

vegetable=['potato','lemon','tomato']

def print_list(veg):
    for i in veg:
        print(i, end=" ")

print_list(vegetable)


# blank function
def fun():
    pass


fun()