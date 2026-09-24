#LeapYear

Year1 = int(input("Enter a year: "))

if Year1 % 4 == 0 and Year1 % 100 != 0 or Year1 % 400 == 0:
    print("This is a leap year")
else:
    print("Not a leap year")