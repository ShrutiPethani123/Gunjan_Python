from abc import ABC , abstractmethod
class RBI(ABC):

    @abstractmethod
    def getRateOfIntrest(self):
        pass

    def disp(self):
        print("RBI class")

class ICICI(RBI):
    
    def methodICICI(self):
        print("ICICI")

    def getRateOfIntrest(self):
        print("7%")

class HDFC(RBI):

    def getRateOfIntrest(self):
        print("8%")
    


obj = ICICI()
obj.methodICICI()
obj.getRateOfIntrest()

obj2 = HDFC()
obj2.getRateOfIntrest()
obj2.disp()


# obj3 = RBI()
# obj3.getRateOfIntrest()


# We can't write abstract method in non abstract class.
# but we can write abstract and non abstract(Concreate method) method in abstract class
# We can't create object of abstract class.
# abstract method do not have body.