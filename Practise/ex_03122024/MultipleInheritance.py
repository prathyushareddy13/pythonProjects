class Dad :

    def name(self):
        print("Prabhkar Reddy")
    def height(self):
        print(5.7)
    def like_eat(self):
        print("Biriyani")

class Mom:

    def sur_name(self):
        print("Chennam Reddy")
    def siblings(self):
        print(3)
    def like_eat(self):
        print("Butter Naan")

class me(Dad,Mom):

    def my_name(self):
        print("Prathyusha")

me_obj = me()
me_obj.name() #dad class
me_obj.sur_name() #mom class
me_obj.my_name() # self
me_obj.like_eat() # if same method is defined in both the classes, it will call the first inherited class method
