class Home:

    def __init__(self):
        self.father = "Rakesh"
        self.__child = "Sid"

    def my_family(self, is_auth):
        print(self.father)
        #print(self.__child)
        self.__doorlock()
        if is_auth:
            print("access provided")
        else:
            print("denied")

    def __doorlock(self):
        print("confidential")



fam = Home()
fam.my_family(False)
#print(fam.father)

