def convertYears(x):
    k1 = 10.5
    k2 = 4
    if x < 0:    raise ValueError("Years should be positive!")
    elif x <= 2: return x * k1
    else:        return 2 * k1 + (x - 2) * k2

humanYears = float(input("Enter human years: "))
try:
    dogYears = convertYears(humanYears)
    print("Dog years:", dogYears)
except ValueError as e:
    print(e)