year = int(input("Enter year to check whether it is leap year or not: "))

if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print("Given year is leap year")
        else:
            print("Given year is not leap year")
    else:
        print("Given year is leap year")
else:
    print("Given year is not leap year")
