# Question 1

moths_in_house = True

if moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")

# Question 2

mitch_is_home = False

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")
elif moths_in_house and not mitch_is_home:
    print("Meooooooooow! Hissss!")
elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch.")

# Question 3

light_colour = "Amber"
car_detected = False

if light_colour == "Red" and not car_detected:
    print("Do nothing.")
elif light_colour == "Red" and car_detected:
    print("Flash!")
elif light_colour == "Green" and not car_detected:
    print("Do nothing.")
elif light_colour == "Green" and car_detected:
    print("Do nothing.")
elif light_colour == "Amber" and not car_detected:
    print("Do nothing.")
elif light_colour == "Amber" and car_detected:
    print("Do nothing.")

Could also be implemented as

if light_colour == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.")

# Question 4

height = input("Enter your height in centimetres, without the unit ")
try: 
    height = int(height)
except ValueError:
    try:
        height = float(height)
    except ValueError:
        print("Either that isn't a number or you added a unit")

if height >= 120:
    print("Hop on!")
elif height < 120:
    print("Sorry, not today :(")