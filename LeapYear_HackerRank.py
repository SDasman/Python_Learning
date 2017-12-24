def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        else:
            leap = False
            return leap

    return leap

year = int(input())
print(is_leap(year))

#In the Gregorian calendar three criteria must be taken into account to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years,
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.