class Person:
     def __init__(self, name, age):
         self.name = name
         self.age =age

     def get_name(self):
         return self.name
     def set_name(self):
         self.name = "Prathyusha"
         return self.name

p1 = Person("Prat", 30)
print(p1.get_name())
print(p1.age)
print(p1.set_name())
print(p1.get_name())