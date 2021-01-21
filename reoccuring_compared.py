print("Reoccuring payments calculator")
print("")

a = 1000000 #float(input("Enter in your fire number "))
p = 18000 #float(input("Enter in the money you have invested "))
r = 0.07 #float(input("Enter in your estimate rate of return "))
n = 12.0 # assuming monthly compound interest
saving = 1500.0 #amount saving
daily = float(1.0/365.0)
# Compounding monthly and incrementing daily
#100 a month / 365

daysInMonth = 30.42

def time(p, r, n, saving, a):
    print("This is if you save $" + str(saving) + " a month")
    days = 0
    curA = 0.0
    while curA < a:
        curA = p*(1.0 + r/n)**(n*daily)
        p = curA+(saving/daysInMonth)
        days += 1
    return days

def daysToYears(days):
    months = weeks = years = 0
    while ((days - 365) > 0):
        years += 1
        days -= 365
    print(str(years) + " years")
    while((days - daysInMonth) > 0):
        months += 1
        days -= daysInMonth
    print(str(months) + " months")
    while((days - 7) > 0):
        weeks += 1
        days -= 7
    print(str(weeks) + " weeks")
    print(str(int(days)) + " days")
    print("")

days = time(p, r, n, 0, a)
daysToYears(days)

days = time(p, r, n, saving, a)
daysToYears(days)

days = time(p, r, n, saving+1500, a)
daysToYears(days)

days = time(p, 0.08, n, saving+1500, a)
daysToYears(days)
