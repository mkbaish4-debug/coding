weight = float(input("Enter you weight: "))
unit = input("Kilograms or Pounds?(Kg or lb): ")
unit = unit.lower()
if unit == "kg":
    weight = round(weight/0.4536)
    print(f"Your weight in lb is: {weight}lb")
elif unit == 'lb':
    weight = round(weight * 0.4536)
    print(f"Your weight in  Kg is: {weight}Kg ")
else:
    print("Enter a valid unit!")
