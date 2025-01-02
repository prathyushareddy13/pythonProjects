def fun():
    global a  # you can declare global variable inside the function also directly and access outside
    a= 123
    print(a)
fun()
print(a)


x=100

def cool():
    x=200
    print(x)
cool()
print(x) #directly accessing global variable

y='Prat'

def name():
    global y
    y='Reddy' #to chane the value of global variable, and once we declare and change it will be changed everywhere
    z='Sid'
    print(y,z)
name()
print(y)

