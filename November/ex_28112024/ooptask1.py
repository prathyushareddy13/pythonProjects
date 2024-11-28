class PyATB:
    name = None
    age = None
    gender = None
    place = None
    role = None

    def __init__(self, name,age,gender):
        self.name = name
        self.gender = gender
        self.age = age

    def print_stud_info(self):
        print(f"My name is {self.name}, My age is {self.age}, MY gender is {self.gender}")


p1 = PyATB("Prathyusha",25,"Female")
p2 = PyATB("Ajit",34,"Male")
p3 = PyATB("Sai",30,"Male")
#print(p1.name)
p1.print_stud_info()
p2.print_stud_info()
p3.print_stud_info()
