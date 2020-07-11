# Question 1
number = input("Enter a number ")
sum_list = 0
while number != "":
    sum_list += int(number)
    number = input("Enter a number ")
print(sum_list)

# Question 2
mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"]
]

for pet in mailing_list:
    print(f"{pet[0]}: {pet[1]}")

#  Question 3
names = []
name = input("Enter a name ")
while len(names) < 3 :
    names.append(name)
    if len(names) < 3:
        name = input("Enter a name ")
    else:
        for individual in names:
            print(individual)

# Question 4
groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]
total = 0

for item in groceries:
    quantity = input(f"What quantity of {item[0]} would you like? ")
    item[1] = item[1] * int(quantity)
    total += item[1]

total = f"${total:.2f}"

print("====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")
print("============================")
print(f"{total:>27}")






