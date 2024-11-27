def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

day = int(input("Enter day : "))
month = int(input("Enter month : "))
year = int(input("Enter year : "))

print(f"Date: {day}-{month}-{year}")

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
