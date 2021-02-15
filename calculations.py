import math

a = 1000000.0 #float(input("Enter in your fire number "))
p = 50000.0 #float(input("Enter in the money you have invested "))
r = 0.07 #float(input("Enter in your estimate rate of return "))
n = 12 # assuming monthly compound interest
oneTimeSavings = 1500.0
repeatSavings = 650 #amount saved continuously
#For continuous
daily = float(1.0/365.0)
# Compounding monthly and incrementing daily
#100 a month / 365

daysInMonth = 30.42

def originalTimeline(a, p, n, r):
    return (math.log(a/p)) / (n*(math.log(1 + (r/n))))

def continuousPaymentTimeline(p, r, n, saving, a):
    print("This is if you save $" + str(saving) + " a month")
    days = 0
    curA = 0.0
    while curA < a:
        curA = p*(1.0 + r/n)**(n*daily)
        p = curA+(saving/daysInMonth)
        days += 1
    return days


print("Originally calculated time: " + str(originalTimeline(a, p, n, r)))

titles = ["month", "week", "day", "hour"]
intervals = [12, 4.345, 7, 24]

def daysToYears(time):
    print(str(int(time)) + " years")
    for i in range(4):
        # t is a float, while int(t) is a integer so it automatically removes anything after decimal
        time = ((time - int(time)) * intervals[i])
        if int(time) > 0:
            if int(time) > 1:
                print(str(int(time)) + " " + titles[i] + "s")
            else:
                print(str(int(time)) + " " + titles[i])

# def daysToYears(days):
#     months = weeks = years = 0
#     while ((days - 365) > 0):
#         years += 1
#         days -= 365
#     print(str(years) + " years")
#     while((days - daysInMonth) > 0):
#         months += 1
#         days -= daysInMonth
#     print(str(months) + " months")
#     while((days - 7) > 0):
#         weeks += 1
#         days -= 7
#     print(str(weeks) + " weeks")
#     print(str(int(days)) + " days")
#     print("")
        

def calculate_diff(originTime, afterTime):
    newT = originTime - afterTime
    print(newT)
    if int(newT) != 0:
        print(str(int(newT)) + " years")
    for i in range(4):
        newT = (newT - int(newT)) * intervals[i]
        if int(newT) > 0:
            if int(newT) > 1:
                print(str(int(newT)) + " " + titles[i] + "s")
            else:
                print(str(int(newT)) + " " + titles[i])

# daysToYears(time)


print("")
print("This is how long until FIRE if you save amount:")
p += repeatSavings
afterTime = (math.log(a/p)) / (n*(math.log(1 + (r/n))))

print("After calculated time: " + str(afterTime))
daysToYears(afterTime)
print("")
print("You saved this amount of your time:")
# calculate_diff(t, afterTime)

# For continuous Payments
days = continuousPaymentTimeline(50000, 0.07, n, 0, a)
daysToYears(days)

# days = continuousPaymentTimeline(p, r, n, repeatSavings, a)
# daysToYears(days)

# days = continuousPaymentTimeline(p, r, n, repeatSavings+1500, a)
# daysToYears(days)

# days = continuousPaymentTimeline(p, 0.08, n, repeatSavings+1500, a)
# daysToYears(days)