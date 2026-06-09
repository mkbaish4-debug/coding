# for loops = execute a block of code a finite number of times 
#            we can iterate over a range, sequence, or strings etc.

# for x in range(1, 11):
#     print(x)

# for x in range(1, 20, 4):
#     if x == 13:
#         continue # to skip over (basically it is go through this condition without doing anything)
#     else:
#         print(x)

# for x in range(1, 20):
#     if x == 13:
#         break
#     else: 
#         print(x)

# creditcard_num = "1234-5678-9012-3456"
# for x in creditcard_num:
#     print(x)

creditcard_num = "1234-5678-9012-3456"
for x in creditcard_num[1:13:2]:
    print(x)