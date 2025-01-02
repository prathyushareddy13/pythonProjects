def sum1(a,b):
    return a+b
print(sum1(10,20)) #positional arguments

def subt(c,d):
    return c-d
print(subt(d=20, c=40)) #keyword arguments

def default_args(a=10,b=30):
    return a+b
print(default_args(100,200))

def act(a,b=20,c=4):
    return a+b+c
print(act(10))
print(act(10,10))
print(act(b=5,c=10,a=15))
print(act(3,6,c=5))
#print(act(10,b=30,40))# invalid syntax. Positional args should be before keyword args
