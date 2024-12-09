class Car :

    def doors(self):
        print("It has Four doors")

    def wheels(self):
        print("It has four wheels")

class Hyundai(Car):
    def color(self):
        print("it is a red color Hyundai car")

    def model(self):
        print("Grand I10")

obj1 = Car()
obj1.doors()

obj_child = Hyundai()
obj_child.color()
obj_child.model()
obj1.doors()

