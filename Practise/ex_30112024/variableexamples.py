a = 10

class  ExVariables:
    b = "Prathyusha"

    def local_var(self):
        c=20
        print(c)
        print(self.b)
        global a
        #a = "Global" #you can access global variable in this way or by using global keyword
        print(a)

v1 = ExVariables()
v1.local_var()


