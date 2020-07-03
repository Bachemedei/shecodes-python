print("lists yay!")

tea_collection = ["Earl Grey", "Peppermint", "Lemon and Ginger", "Strawberry Cream"]
print(tea_collection)

tea_collection.append("Chai")
print(tea_collection)

print(len(tea_collection))

tea_collection.extend(["New York Breakfast", "Berry"])
# print(tea_collection)

# print()

# print(tea_collection.pop())
# print(tea_collection)

tea_collection.remove("Chai")
print(tea_collection)

del tea_collection[1:3]
print(tea_collection)

tea_collection.clear()

tea_collection = [
    ["Earl Grey", "Melbourne Breakfast", "Chai"],
    ["Peppermint", "Lemon and Ginger", "Strawberry Cream"]
]
# print(tea_collection)
# print(tea_collection[0])
# print(tea_collection[0][0])

tea_collection.append(["Chamomile", "Green", "Dandelion"])
print(tea_collection)

print(len(tea_collection))

if (len(tea_collection)) > 3:
    print("Greater than three")
else:
    print("Less than or equal to 3")