class Gf:

    def live(self):
        print("Village")
    def occupation(self):
        print("Farmer")

class Father(Gf):

    def place(self):
        print("Nellore")
    def f_occu(self):
        print("Business")

class Me(Father):

    def stay(self):
        print("Bangalore")
    def work(self):
        print("Software")

me1 = Me() #can access all three classes
me1.live()
me1.f_occu()
me1.work()

f1 = Father() #father can access only self and GF classes
f1.occupation()
f1.place()