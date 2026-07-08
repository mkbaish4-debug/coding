# nested loops = a loop within another loop (outer, inner)
#                outer loop:
#                      inner loop:



# for x in range(2,5):
#     for y in range(2, 10):
#         print(f"{x}{y}", end = "")
#     print()

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol =  (input("Enter the symbol: "))

for x in range(rows):
    for y in range(columns):
        print(symbol, end = "")
    print()
