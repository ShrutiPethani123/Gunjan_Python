class Test:


    def __init__(self):
        self. b=30
        self.__x=45  # __ -> private
    

    def disp(self):
        print("Hello..",self.b)
        print("Hyy",self.__x)


class Test2(Test):

    def msg(self):
        print(self.b)
        print(self.__x)

t = Test()
t.disp()
# print(t.a)
# print(t.__x)
print(t.b)
t2 = Test2()
t2.msg()