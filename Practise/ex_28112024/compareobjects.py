class Computer:

    def __init__(self):
        self.name = "Prathyusha"
        self.age = 30
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1=Computer()
c2=Computer()
#c1.age = 35
if c1.compare(c2):
    print("They are same",c1.age,c2.age)
else:
    print("They are different",c1.age,c2.age)