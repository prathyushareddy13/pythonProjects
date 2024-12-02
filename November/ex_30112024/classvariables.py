class Person:

    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name

prat = Person("Prat")
rakesh = Person("Rakesh")
#print(prat.walk())
#print(rakesh.walk())

print("Who is walking -->", prat.walk())
print("Who is walking -->", rakesh.walk())