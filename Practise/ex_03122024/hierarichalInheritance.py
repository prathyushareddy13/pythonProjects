class Prabha:

    def house(self):
        print("2 houses")
    def bike(self):
        print("2 bikes")
    def educ(self):
        print("Commerce")

class Prat(Prabha):

    def house_me(self):
        print(1)
    def bike_me(self):
        print(1)
    def educ(self):
        print("B.Tech")

class Bro(Prabha):

    def house_bro(self):
        print(1)

    def bike_bro(self):
        print(1)

    def edu_bro(self):
        print("B.Tech")

me2 = Prat()
bro = Bro()
bro.bike_bro()
bro.house()
me2.educ() #if same method is defined in both parent and child class, child class method will be executed
me2.house()