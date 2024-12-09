class Our_cars:

    def dad_car(self):
        print("Dad has Swift Dzire")
    def my_car(self):
        print("Daughter has Grand I10")
    def son_car(self):
        print("Son has Tiago car")

class my_car1(Our_cars):
    def my_car(self):
        print("Daughter has Range Rover")

my_obj = my_car1()
my_obj.my_car()