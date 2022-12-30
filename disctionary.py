"""
key:value
-> unordered
-> mutable

"""
disc={
    'a':"apple",
    'b':"banana",
    'm':"Mango",
    'k':'kiwi'
}

print(disc)
print(type(disc))

print(disc['a'])
print(disc['b'])
print(disc['m'])
print(disc['k'])

print(disc.get('a'))
print(disc.items())
print(disc.keys())
print(disc.values())
print(disc.pop('m'))
# print(disc.pop('h'))#error if key not present
# print(disc['h'])
print(disc.get('j'))
print(disc.popitem())
print(disc)
print(disc.setdefault('c','coconut45'))
print(disc)
print(disc.setdefault('c','coconut'))
print(disc)
disc.update({'c':'coconut','m':'mango'});
print(disc)

d={
    1:'java',
    2:'python',
    1:'cpp'
}
print(d)

d={
    '&':'java',
    '*':'python',
    '^':'cpp'
}
print(d)