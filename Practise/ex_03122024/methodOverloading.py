class Math:

    def add(self,a=0,b=0):
        return a+b
    def add(self, a=0,b=0,c=0):
        return a+b+c

class Math_child(Math):

    def sub(self,a,b):
        return a-b

m1 = Math_child()
print(m1.add(1,2,3))
print(m1.add(1,4))
print(m1.sub(4,2))