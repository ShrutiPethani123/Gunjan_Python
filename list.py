"""
-> sequence of element
-> all elements have order
-> mutable

"""

l1=[1,2,3,'java','python']
print(l1)

print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
# print(l1[5]) -> list index out of range

print(l1[-1])
print(l1[-2])
print(l1[-3])
print(l1[-4])
print(l1[-5])

print("------------------------------------")
print(type(l1))
print(len(l1))

l2=[22,3,1,51,7,2,8,12,90,45,27]
print(max(l2))
print(min(l2))
print(sum(l2))
print(len(l2))
print(sorted(l2))
print(sorted(l2 ,reverse=True))

l2.sort()
print(l2)

l3=['india','Usa','pakistan','china','canada']

print(max(l3))
print(min(l3))
# print(sum(l3))  -> invalid for string element
print(sorted(l3))

l3.append(2)
print(l3)

l4 = l3.copy()
print(l4)

l5=l3
print(l5)

print(id(l3))
print(id(l4))
print(id(l5))

print(l3 is l4)
print(l3 is l5)

l3.clear()
print(l3)
print(l5)
print(l4)

l7=[1,2,3]
l4.append(l7)
print(l4)

l4.extend(l7)
print(l4)

print(l4.index('pakistan'))
print(l4.index('Usa'))

del l4[2]
print(l4)

# del l4
# print(l4)

l4.remove(3) #element
print(l4)

print(l4.pop(3))
print(l4)

# l4.remove(3) #element
# print(l4)

# print(l4.pop(33))
# print(l4)

l4.reverse()
print(l4)

l2.sort(reverse=True)
print(l2)

print(l2.count(2))
print(l2.index(27))

l2.insert(5,100)
print(l2)


"""
1.Take 5 element from user and add all element in list.
2.Take one list and find maximum and minimum from list.
3.Take one list and find sum and average of all list element.
4. Make a Python program that generates a list of powers of base that is given by user upto the power
 given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
5. Add 10 numbers into the list, reverse that list

6. Remove duplicate element from list.
7. print list after removing even number.
8. find the position of maximum element from list.
9. find occurence of user given input.
10. add 10 numbers in list and add odd element into odd list and even element into even list.
11. find occurence of all element in list.

    1 2 5 1 6 4 2 3 1

    1 - 3 times
    2 - 2 times
    5 - 1 
    6 - 1
    4 - 1
    3 - 1



"""



