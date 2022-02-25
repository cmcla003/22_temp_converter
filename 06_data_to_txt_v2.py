# Write data to txt file

# checks if something is valid

import re

# Data to be output
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# get file name can't be blank/invalid
has_error = "yes"

while has_error =="yes":
    print()
    filename = input("Enter a file name (no extensions): ")
    has_error = "no"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char,letter):
            continue
        elif letter == " ":
            problem = "No spaces allowed"
        else:
            problem = "No {} allowed".format(letter)
        has_error = "yes"

    if filename == "":
        problem = "Can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename = {}".format(problem))
    else:
        print("You have entered a valid filename")

# add .txt suffix
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at the end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()