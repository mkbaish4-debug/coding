principle = 0
rate = 0
time = 0

# while principle <= 0:
#      principle = float(input("Enter the principle amount($): "))
#      if principle <= 0:
#         print("Principle can't be negative or zero!")

# while rate <= 0:
#      rate = int(input("Enter the rate(%): "))
#      if rate <= 0:
#         print("Rate can't be negative or zero!")

# while time <= 0:
#         time = int(input("Enter the time in year/s: "))
#         if time <= 0:
#          print("Time can't be negative or zero!")

# total = principle * pow((1+rate/100), time)
# print(f"The total amount after {time:,}year/s is ${total:,.2f}!")

# in the above code we can't calculate for 0 value's
# In the below code we can

while True:
     principle = float(input("Enter the principle amount($): "))
     if principle < 0:
        print("Principle can't be negative!")
     else:
         break

while True:
     rate = int(input("Enter the rate(%): "))
     if rate < 0:
        print("Rate can't be negative!")
     else:
         break


while True:
        time = int(input("Enter the time in year/s: "))
        if time < 0:
         print("Time can't be negative!")
        else:
            break

total = principle * pow((1+rate/100), time)
print(f"The total amount after {time:,}year/s is ${total:,.2f}!")