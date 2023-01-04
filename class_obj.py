class Test:
     #instance variable
    # x=0
    # y=0
    # optional

    # def __init__(self):
    #     self.x=50
    #     self.y=60

    # def __init__(s): 
    #     s.x=45
    #     s.y=90

    def __init__(self,name , age):
        print("Constructor called!!")
        self.name=name
        self.age=age

    def __str__(self) :
        return f"{self.name}({self.age})"
        # pass
        
    
    def display(abc):
        print(abc.name , abc.age)

    
    
        

# t=Test() #object
# print(t.x)
# print(t.y)

# t1 = Test()
# print(t1.y)

t3 = Test("jay",20)
t3.display()
t3.age=50
t3.display()

# del t3
# t3.display()

print(t3)