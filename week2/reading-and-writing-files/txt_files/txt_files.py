names = []

with open("names.txt") as txt_file:
    for line in txt_file:
        #line.strip will remove the /n automatically added to the list
        line = line.strip()
        names.append(line)

# Challenge - Reading & Writing files
# Question 1

line_number = 1
with open("names_output.txt", "w") as txt_file:
    for name in names:
        name = f"{line_number}. {name}"
        txt_file.write(name + "\n")
        line_number += 1

