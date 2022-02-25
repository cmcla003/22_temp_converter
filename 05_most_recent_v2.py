# Get data from user and store in a list
# then display most recetn 3 entries

# set up empty list
all_calcuations =[]

# Get 5 items of data
get_item = " "
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calcuations.append(get_item)

print()
if len(all_calcuations) == 0:
    print("Oops the list is empty")

else:
    # Show everything made it into the list
    print()
    print("*** The full list ***")
    print(all_calcuations)
    print()

    if len(all_calcuations) >= 3:
        # Print items from the end of the list
        print("*** Most Recent ***")
        for item in range(0,3):
            print(all_calcuations[len(all_calcuations)- item - 1])

    else:
        print("*** Newest to oldest ***")
        for item in all_calcuations:
            print(all_calcuations[len(all_calcuations) - all_calcuations.index(item) -1])