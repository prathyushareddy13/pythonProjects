class Bank:

    def __init__(self,account,balance):
        self.__account = account
        self.balance = balance

    def add_money(self,amount):
        self.balance = self.balance+ amount

    def check_bal(self):
        print("Total money in the account -", self.balance)

    def show_acc_num(self,is_auth): #to access the private variables define a method and call it
        if is_auth:
            print("Original account number:", self.__account)
        else:
            print("Not allowed")

    def change_acc_num(self,num_change):
        self.__account = num_change
        print("Modified account number", self.__account)

prat = Bank(45635464765, 100)
prat.show_acc_num(True)
prat.add_money(200)
prat.check_bal()
prat.change_acc_num(123456789)


