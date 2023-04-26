x=int(input("Year="))
if x % 100 != 0 and x % 4 == 0:
    print("It's a leap year")
elif x % 400 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")
