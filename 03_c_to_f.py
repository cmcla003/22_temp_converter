# convert degrees c to f
# function takes in value does conversion and puts answer into a list

def to_f(from_c):
    farenheit = (from_c * 9/5) + 32
    return farenheit

# Main routine
temperature = [0,40,100]
converted = []

for item in temperature:
    answer = to_f(item)
    ans_statement = "{} degrees C is {} degrees F.".format(item,answer)
    converted.append(ans_statement)

print(converted)