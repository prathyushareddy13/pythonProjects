
month = input("Enter the month:")
month = month.lower()

match month:
    case month if month == "march" or month == "april" or month == "may":
        print("It's Summer! Keep yourself Hydrated")
    case month if month == "june" or month == "july" or month == "august":
        print("It's Rainy Season! Take care of your health")
    case month if month == "september" or month == "october" or month == "november":
        print("It's Autumn!")
    case month if month == "december" or month == "january" or month == "february":
        print("Yay! Winter is here. Enjoy")
    case _:
        print("Please provide valid input")



