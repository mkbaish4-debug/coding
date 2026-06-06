temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")
if unit == "C":
    temp = round((9/5)*temp +32)
    print(f"Temperature in fahrenheit is: {temp}F ")
elif unit == "F":
    temp = round((temp - 32)*5/9)
    print(f"Temperature in celsius is: {temp}C ")
else:
    print("Enter a valid unit!")