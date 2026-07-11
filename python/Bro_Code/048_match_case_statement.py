# match case statement = It is an alternative to using many elif statements
#                        execute some code if a value matches a 'case'
#                        cleaner and syntax is more usable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday!"
#         case 2:
#             return "It is Monday!"
#         case 3:
#             return "It is Tuesday!"
#         case 4:
#             return "It is Wednesday!"
#         case 5:
#             return "It is Thursday!"
#         case 6:
#             return "It is Friday!"
#         case 7:
#             return "It is Saturday!"
#         case _:
#             return "Invalid day!"

# print(day_of_week(1))

def isweekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Tuesday" | "Monday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False


print(isweekend("Sunday"))
