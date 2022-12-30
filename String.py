"""

-> string is a Ordered and immutable

"""

str="Hello World"
print(str)
print(type(str))

"""
Element    Index
H           0
e           1
l           2
l           3
O           4
            5

d           10


"""
print(str[0])
print(str[10])
print(str[-1])

"""
element    neg Index
H       -11
e       -10
l       -9
l       -8
o       -7
        -6
w       -5
o       -4
r       -3
l       -2
d       -1


"""
print(str[-8])
print(str[-3])
print(str[-6])

"""
    Take one index from user and print that index character.
"""

"""
slicing of string

1. [start:end]
2. [start:end:step]
3. [start: ]
4. [: end]
5. [ : ]

"""

str = "Python Programming"
#      0123456789       17

print(len(str))
print(str[0:5]) #Pytho -> start to end-1
print(str[12:16])
print(str[3:89])
print(str[1:3:5])
print(str[3:17:3])
print(str[-13:-1])
print(str[1:14:-1])
print(str[:])
print(str[0:])
print(str[3:])
print(str[ : :-1])
print(str)
print(str[: 6])
print(str[-12:-3:4])
print(str[-12:-3:2])
print(str[-12:3:-2])
print(str[: : -2])


"""
string Methods

"""

"""
Task:

1. Take one string from user and make one new string contain first  , middle and last character

Gunjan
new string - Gnn


2. Take one string from user and make one new string contain middle 3 character

Hello 
elo

3. Arrange string characters such that lowercase letters should come first

PyThon
yhonPT

4. Count all letters, digits, and special symbols from a given string

35125135#%$#$#^yfgshf

5.Create a mixed String using the following rules

Take two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, 
then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. 
Any leftover chars go at the end of the result.

ABC
XYZ

AZBYCX

6.find all occurrences of a substring in a given string by ignoring the case

str1 = "Welcome to India. INDIA is awesome"

India count = 2 


"""

