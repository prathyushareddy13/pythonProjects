class Dog:
    name = None
    breed = None
    color = None

    def dog_name(self):
        print(" is my name")
    def dog_breed(self):
        print("Poodle")
    def dog_color(self):
        print(" is my color ")

rony = Dog()
rony.name = "Rony"
print(rony.name, end ="")
rony.dog_name()
rony.color = "Brown"
print(rony.color, end="")
rony.dog_color()






