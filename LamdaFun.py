def fun(a):
    return a+5

"""
variable = lambda argument : return 

"""
y = lambda a:a+5

print(fun(6))
print(y(6))

z = lambda a,b :a*b
print(z(2,3))

t = lambda a,b,c : a+c+b
print(t(1,2,3))

def my_fun(a):
    return lambda b : b*a

c = my_fun(4)
print(c(5))

def power(b):
    return lambda c:c**b

d=power(4)
print(d(3))