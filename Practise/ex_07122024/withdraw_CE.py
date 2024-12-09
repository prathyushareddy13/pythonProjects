import time

class LowBalanceException(Exception):
    pass
class AttemptErrorException(Exception):
    pass
attempts = 1
def withdraw():
    global attempts
    saved_pin = 1234
    balance = 10000
    pin = int(input("Enter your pin:"))
    if pin == saved_pin:
        try:
            amt = float(input("Enter the amount - "))
            temp_bal = balance-amt
            if temp_bal<1000:
                raise LowBalanceException("Insufficient Amount")
            balance = balance-amt
            print("Your current balance is,", balance)
        except Exception as var:
            print(var)
    else:
        ans = input("Wrong PIN!, Do you want to try again? (Y/N)")
        if ans.lower() == "y":
            attempts+=1
            try:
                if attempts == 3:
                    raise AttemptErrorException("You have used all 3 attempts,your account is locked!")

            except Exception as var:
                print(var)
                time.sleep(3600) #to lock the account for an hour

            else:
                withdraw()
        else:
            print("Thankyou")
            return
withdraw()




