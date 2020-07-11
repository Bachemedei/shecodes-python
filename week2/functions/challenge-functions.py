import csv


# Question 1
# def temp_to_celcius (fahrenheit):
    celcius = (fahrenheit - 32) * 0.5556
    return celcius

# print(temp_to_celcius(32))
# print(temp_to_celcius(113))
# print(temp_to_celcius(26.6))

# Question 2
def calculate_mean(total_sum, num_items):
    mean = total_sum//num_items
    return mean


number = input("Enter a number ")
total_sum = 0
num_items = 0

while number != "": 
    total_sum += float(number)
    num_items += 1
    number = input("Enter a number ")

print(calculate_mean(total_sum, num_items))

# Question 3

def read_csv_file(filepath):
    with open (filepath) as colours_csv:
    reader = csv.reader(colours_csv)
    for line in reader:
        colours.append(line)

def format_colour_line(colour_data):
    return