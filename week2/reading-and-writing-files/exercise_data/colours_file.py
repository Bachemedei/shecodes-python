import csv
# Challenge - Reading & Writing files
# Question 2

colours = []

with open ("colours_20.csv") as colours_csv:
    reader = csv.reader(colours_csv)
    for line in reader:
        colours.append(line)

with open ("colours_20_output.csv", "w") as colours_csv:
    csv_writer = csv.writer(colours_csv, delimiter=",")
    for colour in colours:
        csv_writer.writerow([colour[2], colour[3], colour[4]])

colours = []

with open ("colours_213.csv") as colours_csv:
    reader = csv.reader(colours_csv)
    for line in reader:
        colours.append(line)

with open ("colours_213_output.csv", "w") as colours_csv:
    csv_writer = csv.writer(colours_csv, delimiter=",")
    for colour in colours:
        csv_writer.writerow([colour[2], colour[3], colour[4]])

