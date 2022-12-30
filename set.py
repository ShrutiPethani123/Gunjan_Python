"""
set -> mutable , unordered
-> No duplicates
"""

# set={1,2,4,1,2,3}
# print(set)
# print(type(set))
# print(len(set))
# print(max(set))
# print(min(set))
# print(sum(set))
# print(sorted(set))

# s1={2,3,1,4,6}
# s2={3,1,8,9,5,7}

# s3=s1.intersection(s2) # 1 , 3
# print(s3)

# # s1.intersection_update(s2)
# # print(s1)

# s3=s1.union(s2) # {2,3,1,4,6,8,9,5,7}
# print(s3)

# s3=s1.difference(s2)
# print(s3)

# # s1.difference_update(s2)
# # print(s1)

# s4=s1.symmetric_difference(s2)
# print(s4)

# # s1.symmetric_difference_update(s2)
# # print(s1)

# print(s1.isdisjoint(s2))

# s1={1,2,3}
# s2={1,2,3,4,5,6}
# print(s1.issubset(s2))
# print(s2.issuperset(s1))


# s1.update(s2)
# print(s1)

# s1.add(56)
# print(s1)

# print(s1.pop())
# print(s1)

# s1.remove(4)
# print(s1)

# s1.discard(6)
# print(s1)

# # s1.remove(4)
# # print(s1)

# s1.discard(6)
# print(s1)

# # s1.clear()
# # print(s1)
# print(s1)
# s3={1,2,3}
# s3=s1.copy()
# print(s3)

# print(id(s3))
# print(id(s1))



# s1.update(s2)
# print(s1)
# print(id(s2))
# print(id(s1))

l=[1,2,3,1,2,5,6,1,4,7]
print(l)
s6=set(l)
print(s6)
l=list(s6)
print(l)
