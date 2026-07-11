# membership operators = used to check whether a vaue or variable is found in a sequence
#                        (list, set, tuple, string, dictionary etc)
#                        1. in 2. not in

# num_list = (2, 5, 9)
# while True:
#     num = input("Guess if a number is present in the list(1-10): ")
#     if not num.isdigit():
#         print("Invalid input!")
#     else:
#         num = int(num)
#         if num in num_list:
#             print(f"{num} was found in the list!")
#             break
#         else:
#             print(f"{num} was not found in the list!")

# students = {"Vimal": "B+",
#             "Shiva": "A+",
#             "Abhisekh": "B+",
#             "Ankit": "A"}
# student = input("Enter the name of the student: ")
# if student in students:
#     print(f"{student}'s grade is {students.get(student)}.")
# else:
#     print(f"{student} was not found!")

email = "fakeemail@gmail.com"
if "@" in email and "." in email:
    print("It's a valid email.")
else:
    print("It's an invalid email!")
