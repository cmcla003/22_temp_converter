# Write data to txt file

# Data to be output
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# get file name can't be blank/invalid
filename = input("Enter a file name (no extensions): ")

# add .txt suffix
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at the end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()