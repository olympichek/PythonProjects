def daysInMonth(month, year):
    if month < 0 or month > 12:
        raise ValueError("Month should be between 1 and 12!")
    elif month == 2:
        if year % 400 == 0: return 29
        if year % 100 == 0: return 28
        if year % 4   == 0: return 29
        return 28
    else:
        m31 = [1, 3, 5, 7, 8, 10, 12]
        if month in m31: return 31
        else:            return 30

month = int(input("Enter month: "))
year  = int(input("Enter year: "))
try:
    days = daysInMonth(month, year)
    print("Days in this month:", days)
except ValueError as e:
    print(e)