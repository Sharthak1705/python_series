year = int(input("enter the year is :"))

if (year % 400 ==0) or (year % 4 == 0 and year % 100 !=0):
    print("The year is a leap year")
else:
    print(year,"The year is not a leap year")