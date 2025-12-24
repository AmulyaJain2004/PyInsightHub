year = int(input("Enter year: "))
month = int(input("Enter month number (1-12): "))
if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print("Given year is leap year")
            if month == 1 or month == 3 or month == 5 or month == 6 or month == 7 or month == 8 or month == 10 or month == 12:
                day = int(input("Enter the day: "))
                if (day>=32 or day<=0):
                    print("Day does not exist")
                else:
                    print(f"Day: {day+1}, Month: {month}, Year: {year}")
            elif month == 2:
                day = int(input("Enter the day: "))
                if (day>=29 or day<=0):
                    print("Day does not exist")
                else:
                    print(f"Day: {day+1}, Month: {month}, Year: {year}")
            else:
                day = int(input("Enter the day: "))
                if (day>=31 or day<=0):
                    print("Day does not exist")
                else:
                    print(f"Day: {day+1}, Month: {month}, Year: {year}")
        else:
            print("Given year is not leap year")
            if month == 1 or month == 3 or month == 5 or month == 6 or month == 7 or month == 8 or month == 10 or month == 12:
                day = int(input("Enter the day: "))
                if (day>=32 or day<=0):
                    print("Day does not exist")
                else:
                    print(f"Day: {day+1}, Month: {month}, Year: {year}")
            elif month == 2:
                day = int(input("Enter the day: "))
                if (day>=28 or day<=0):
                    print("Day does not exist")
                else:
                    print(f"Day: {day+1}, Month: {month}, Year: {year}") 
            else:
                day = int(input("Enter the day: "))
                if (day>=31 or day<=0):
                    print("Day does not exist")
                else:
                    print(f"Day: {day+1}, Month: {month}, Year: {year}")           
    else:
        print("Given year is leap year")
        if month == 1 or month == 3 or month == 5 or month == 6 or month == 7 or month == 8 or month == 10 or month == 12:
            day = int(input("Enter the day: "))
            if (day>=32 or day<=0):
                print("Day does not exist")
            else:
                print(f"Day: {day+1}, Month: {month}, Year: {year}")
        elif month == 2:
            day = int(input("Enter the day: "))
            if (day>=29 or day<=0):
                print("Day does not exist")
            else:
                print(f"Day: {day+1}, Month: {month}, Year: {year}")
        else:
            day = int(input("Enter the day: "))
            if (day>=31 or day<=0):
                print("Day does not exist")
            else:
                print(f"Day: {day+1}, Month: {month}, Year: {year}")
else:
    print("Given year is not leap year")
    if month == 1 or month == 3 or month == 5 or month == 6 or month == 7 or month == 8 or month == 10 or month == 12:
        day = int(input("Enter the day: "))
        if (day>=32 or day<=0):
            print("Day does not exist")
        else:
            print(f"Day: {day+1}, Month: {month}, Year: {year}")
    elif month == 2:
        day = int(input("Enter the day: "))
        if (day>=28 or day<=0):
            print("Day does not exist")
        else:
            print(f"Day: {day+1}, Month: {month}, Year: {year}") 
    else:
        day = int(input("Enter the day: "))
        if (day>=31 or day<=0):
            print("Day does not exist")
        else:
            print(f"Day: {day+1}, Month: {month}, Year: {year}")
