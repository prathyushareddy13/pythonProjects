def leap_year(year):
    if year > 0:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(f"{year} is a Leap year")
        else:
            print(f"{year} is not a Leap year")
    else:
        print("Not a valid input")

input_year = int(input("Enter the year:"))
leap_year(input_year)
