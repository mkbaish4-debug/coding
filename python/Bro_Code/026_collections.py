# collection = single "variable" used to store multiple variables.
#     List   = [] Ordered and changable. duplicates ok.
#      set   = {} unordered and immutable. add or remove ok. No duplicates.
#     tuples = () ordered and unchangable. duplicates ok. FASTER.


# print(len(fruits))
# print(dir(fruits))
# print(help(fruits))
# print("apple" in fruits)
# These  are applicable to all.

#              List
# fruits = ["apple", "pineapple", "mango", "banana"]
# print(fruits[0])
# fruits.append("apple")
# fruits.remove("apple")
# fruits.insert(2,"coconut")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("mango"))
# print(fruits.count("mango"))

#            Set
# fruits = {"apple", "mango", "pineapple", "coconut"}
# fruits.add("banana")
# fruits.remove("apple")
# fruits.pop()

#           Tuples
fruits = ("apple", "banana", "pineapple", "mango")
# print(fruits.index("mango"))
# print(fruits.count("mango"))

# all of these are iterable over loop
# for fruit in fruits:
#     print(fruit)
print(fruits)
