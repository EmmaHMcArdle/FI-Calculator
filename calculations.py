# import math
import numpy as np

# a = 1000000.0 #float(input("Enter in your fire number "))
# p = 50000.0 #float(input("Enter in the money you have invested "))
# r = 0.07 #float(input("Enter in your estimate rate of return "))
# n = 12 # assuming monthly compound interest
# oneTimeSavings = 1500.0
# repeatSavings = 650 #amount saved continuously

def calcTimeline(a, p, n, r):
    r = (r/100) # 0.07/12
    return (np.log(a/p)) / (n*(np.log(1 + (r/n))))

def continuousPaymentTimeline(a, p, n, r, saving, freq):
    daily = float(1.0/365.0)
    r = (r/100)
    days = 0
    curA = 0.0
    daysInAFreq = 365.0/freq
    while curA < a:
        # Compounding future value FV = $10,000 x (1 + 15%/1))^(1 x 1)
        # For one Day!
        curA = p*((1.0 + r/n)**(n*daily))
        #curA = curA - a/
        # Take today's principal + add that you're contributing
        p = curA + (saving / daysInAFreq)
        days += 1
    return days

def yearsToTotal(time):
    titles = ["month", "week", "day", "hour"]
    intervals = [12, 4.345, 7, 24]
    timelineStr = ""
    if time <= 0:
        timelineStr = "You're already financially independent!"
    else:
        timelineStr += " " + (str(int(time)) + " years ")
        for i in range(4):
            # t is a float, while int(t) is a integer so it automatically removes anything after decimal
            time = ((time - int(time)) * intervals[i])
            if int(time) > 0:
                if int(time) > 1:
                    timelineStr += " " + (str(int(time)) + " " + titles[i] + "s ")
                else:
                    timelineStr += " " + (str(int(time)) + " " + titles[i] + " ")
    return timelineStr

def daysToTotal(days):
    daysInMonth = 30.42
    timeLineStr = ""
    months = weeks = years = 0
    while ((days - 365) > 0):
        years += 1
        days -= 365
    timeLineStr += " " + (str(years) + " years")
    while((days - daysInMonth) > 0):
        months += 1
        days -= daysInMonth
    timeLineStr += " " + (str(months) + " months")
    while((days - 7) > 0):
        weeks += 1
        days -= 7
    timeLineStr += " " + (str(weeks) + " weeks")
    timeLineStr += " " + (str(int(days)) + " days")
    return timeLineStr
        
def daysToYears(days):
    # Might round in going in HTML round(, 2)
    return days*0.00273973

def calculate_diff(originTime, afterTime):
    titles = ["month", "week", "day", "hour"]
    intervals = [12, 4.345, 7, 24]
    newT = originTime - afterTime
    diffStr = ""
    if int(newT) != 0:
        diffStr += " " + str(int(newT)) + " years"
    for i in range(4):
        newT = (newT - int(newT)) * intervals[i]
        if int(newT) > 0:
            if int(newT) > 1:
                diffStr += " " + (str(int(newT)) + " " + titles[i] + "s")
            else:
                diffStr += " " + (str(int(newT)) + " " + titles[i])
    return diffStr