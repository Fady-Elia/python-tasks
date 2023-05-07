#function leap year
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

#input year
year = int(input("Enter a year = "))

#calling the function to calculate
result = is_leap(year)

#the resualt
print(result)