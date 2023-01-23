"""
-> Inheritance

Parent (super) (base)
|
child (sub) (derived)
 
use: code reusability


Types:

1. single level
2. Multi level
3. Multipal
4. Hyrarchical
5. Hybrid

"""

"""
1. Single level

A
|
B

2. Multi level

A
|
B
|
C

3. Multipal Inheritance

A   B
\   /
  C

4. Hyrarchical

     A
    / \
   B   C
"""

# class Animal:

#     def speak(self):
#         print("Animal....")

# class Cat(Animal):

#     def weep(self):
#         print("cat......")

# class kittle(Cat):

#     def run(self):
#         print("Kittle...")


# k=kittle()
# k.run()
# k.weep()
# k.speak()


# c = Cat()
# c.weep()
# c.speak()

# a = Animal()
# a.speak()
# # a.weep()

class Animal:

    def speak(self):
        print("Animal....")

class Dog(Animal):

    def bark(self):
        print("Dog")

class Cat(Animal):

    def weep(self):
        print("cat")


a=Animal()
a.speak()
# a.bark()
# a.weep()

d=Dog()
d.speak()
d.bark()
# d.weep()

print(issubclass(Cat,Animal))
print(issubclass(Cat,Dog))

print(isinstance(d,Dog))
print(isinstance(d,Cat))


class Father:

    def car(self):
        print("Father class")

class Mother:

    def activa(self):
        print("Mother class")

    def car(self):
        print("Mother car")

    
class Son(Mother,Father):

    def book(self):
        print("Child class")

class GrandSon(Son):

    def toy(self):
        print("Grand son class")

s= Son()
s.car()
s.activa()
s.book()


g = GrandSon()
g.car()
g.activa()
g.book()
g.toy()