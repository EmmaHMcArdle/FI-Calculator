import math

print("One time payment calculator")


a = 1000000.0 #float(input("Enter in your fire number "))
p = 50000.0 #float(input("Enter in the money you have invested "))
r = 0.07 #float(input("Enter in your estimate rate of return "))
n = 12 # assuming monthly compound interest
saving = 650 #amount saving
t = (math.log(a/p)) / (n*(math.log(1 + (r/n))))
print("")
print("Time to FI if you do nothing:")
print("OG T " + str(t))
print(str(int(t)) + " years")
months = (t - int(t)) * 12
print(str(int(months)) + " months")
# assuming 30 days in a month
weeks = (months - int(months)) * 4.345
print(str(int(weeks)) + " weeks")
days = (weeks - int(weeks)) * 7
print(str(int(days)) + " days")
hours = (days - int(days)) * 24
print(str(int(hours)) + " hours")
print("")
print("This is how long until FIRE if you save amount:")
p += saving
afterT = (math.log(a/p)) / (n*(math.log(1 + (r/n))))
print(afterT)
print(str(int(afterT)) + " years")
m = (afterT - int(afterT)) * 12
print(str(int(m)) + " months")
# assuming 30 days in a month
w = (m - int(m)) * 4.345
print(str(int(w)) + " weeks")
d = (w - int(w)) * 7
print(str(int(d)) + " days")
h = (d - int(d)) * 24
print(str(int(h)) + " hours")
print("")
print("You saved this amount of your time:")
newT = t - afterT
print(newT)
if int(newT) > 0:
    print(str(int(newT)) + " years")
m = (newT - int(newT)) * 12
if int(m) > 0:
    print(str(int(m)) + " months")
# assuming 30 days in a month
w = (m - int(m)) * 4.345
print(str(int(w)) + " weeks")
d = (w - int(w)) * 7
if int(d) > 0:
    print(str(int(d)) + " days")
h = (d - int(d)) * 24
if int(h) > 0:
    print(str(int(h)) + " hours")

