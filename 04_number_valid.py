# Code to check if number is valid

def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))

            if response < low:
                print("Too cold")
            else:
                return response

        except ValueError:
            print("Please enter a number")


# main routin
number = temp_check(-273)
print("You chose {}".format(number))

number = temp_check(-459)
print("You chose {}".format(number))
