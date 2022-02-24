# Get data from user and store in a list
# then display most recetn 3 entries

# set up empty list
all_calcuations =[]

# Get 5 items of data
for item in range (0,5):
    get_item = input("Enter an item: ")
    all_calcuations.append(get_item)

# Show everything made it into the list
print()
print("*** The full list ***")
print(all_calcuations)
print()

# Print items from the end of the list
print("*** Most Recent ***")
for item in range(0,3):
    print(all_calcuations[len(all_calcuations)- item - 1])