# indexing = accessing elements of a sequence using [] (indexing operator)
#    [start : end : step] 
credit_number = "1234-5678-9012-3456"

# print(credit_number[9])
# print(credit_number[-4])
# print(credit_number[0:5])
# print(credit_number[:5])
# print(credit_number[5:10])
# print(credit_number[3:])
# print(credit_number[::3])
# last_digits = credit_number[-4:]
# print("xxxx-xxxx-xxxx-" + last_digits)
reverse_credit_number = credit_number[::-1] # steps can also be -ve
print(reverse_credit_number) 

