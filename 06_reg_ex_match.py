# checks if something is valid

import re

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