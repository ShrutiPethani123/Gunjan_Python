"""
-> immutable and ordered

"""
t=(1,4,5,"java",'python','royal')
print(t)
print(type(t))

# t[2]=45
# print(t)

t1=(1,2,4,1,6,2,7,8)
print(len(t))
print(len(t1))
print(max(t1))
print(min(t1))
print(sorted(t1))
print(sorted(t1,reverse=True))

print(t1.count(2))
print(t1.index(8))

t3=('apple','banana','kiwi','Mango','orange')

box1,box2,box3,box4,box5=t3
print(box1)
print(box2)
print(box3)
print(box4)
print(box5)

box1 , box2 , *box3 = t3

print(box1) #1st
print(box2) #2nd
print(box3) #all other

*box1 , box2 , box3 = t3
print(box1) #all other
print(box2) #2nd last
print(box3) #last

box1 , *box2 , box3 = t3
print(box1) #1st
print(box2) #all other
print(box3) #last

l1=list(t3)
l1.append("Grapes")
t3=tuple(l1)
print(t3)