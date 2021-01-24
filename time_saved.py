import math

print("One time payment calculator")


a = 1000000.0 #float(input("Enter in your fire number "))
p = 50000.0 #float(input("Enter in the money you have invested "))
r = 0.07 #float(input("Enter in your estimate rate of return "))
n = 12 # assuming monthly compound interest
repeatSavings = 650 #amount saved continuously

t = (math.log(a/p)) / (n*(math.log(1 + (r/n))))

print("")
print("Time to FI if you do nothing: ")
print("Originally calculated time: " + str(t))

titles = ["month", "week", "day", "hour"]
intervals = [12, 4.345, 7, 24]

def calculate_time(time):
    print(str(int(time)) + " years")
    for i in range(4):
        # t is a float, while int(t) is a integer so it automatically removes anything after decimal
        time = ((time - int(time)) * intervals[i])
        if int(time) > 0:
            if int(time) > 1:
                print(str(int(time)) + " " + titles[i] + "s")
            else:
                print(str(int(time)) + " " + titles[i])
        

def calculate_diff(originT, afterT):
    newT = originT - afterT
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

calculate_time(t)


print("")
print("This is how long until FIRE if you save amount:")
p += repeatSavings
afterT = (math.log(a/p)) / (n*(math.log(1 + (r/n))))

print("After calculated time: " + str(afterT))
calculate_time(afterT)
print("")
print("You saved this amount of your time:")
calculate_diff(t, afterT)

