def is_leap(year):
    leap = False
    while year % 4 == 0:
        if year % 100 != 0:
            leap = True
        elif year % 400 == 0:
            leap = True
        else:
            leap = False
        exit()

    return leap

year = int(input())
print(is_leap(year))