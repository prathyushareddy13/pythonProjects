
from dotenv import load_dotenv
import os

class Login:

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def cred_check(self):
        if self.email == "prathyusha.reddy13@gmail.com" and self.password == "pass123":
            print("Login Successful!!")
        else:
            print("Please check your login credentials")

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

p1 = Login(email,password)
p1.cred_check()


#p1 = Login("prathyusha.reddy@gmail.com","pass123")
#p1.cred_check()