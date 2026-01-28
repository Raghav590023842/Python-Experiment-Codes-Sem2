#Raghav Vij 590023842
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

day = day + 1

if day > 30:
    day = 1
    month = month + 1

    if month > 12:
        month = 1
        year = year + 1

print("Next date:", day, month, year)
