# dictionary = a collection of {key: value} pair
#          ordered and changable. no duplicates allowed

capitals = {"usa": "washington d.c.",
            "india": "new delhi",
            "china": "beijing",
            "russia": "moscow"}

# print(capitals)
# print(dir(capitals))
# print(help(dict))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# print(capitals.get("japan"))
# capitals.update({"japan": "tokyo"})
# capitals.update({"usa": "new york"})
# capitals.pop("usa")
# capitals.popitem()
# capitals.clear()
# capitals.setdefault("japan", "tokyo")
# print(capitals)
# for key in capitals.keys():
#     print(key)
# for values in capitals.values():
#     print(values)
for key, value in capitals.items():
    print(key, value)
