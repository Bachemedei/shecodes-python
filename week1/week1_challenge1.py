# Question 1

num_1 = input("Pick a number ")
num_2 = input("Pick another number ")

print(int(num_1) + int(num_2))

# Question 2

num_3 = input("Pick a number ")
try:
    num_3 = int(num_3)
except ValueError:
    try:
        num_3 = float(num_3)
    except ValueError:
        print("That isn't a number!")


num_4 = input("Pick another number ")
try:
    num_4 = int(num_4)
except ValueError:
    try:
        num_4 = float(num_4)
    except ValueError:
        print ("That isn't a number!")

sum_1 = num_3 * num_4
print(f"{num_3} * {num_4} = {sum_1}")

# Question 3

distance = input("Enter a distance in kilometers without the unit ")
try: 
    distance = int(distance)
except ValueError:
    try: 
        distance = float(distance)
    except ValueError:
        print("Either that isn't a number or you added a unit")

distance_in_m = distance * 1000
distance_in_cm = distance * 10000
print(f"{distance}km = {distance_in_m}m")
print(f"{distance}km = {distance_in_cm}cm")

# Question 4 

name = input("What is your name? ")

height = input("Enter your height in centermetres, without the unit ")
try: 
    height = int(height)
except ValueError:
    try:
        height = float(height)
    except ValueError:
        print("Either that isn't a number or you added a unit")

print(f"{name} is {height}cms tall.")
