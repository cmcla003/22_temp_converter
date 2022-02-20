# convert degrees f to c
# function takes in value does conversion and puts answer into a list

def to_c(from_f):
    centigrade = (from_f -32) * 5/9
    return centigrade

# Main routine
temperature = [0,32,100]
converted = []

for item in temperature:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C.".format(item,answer)
    converted.append(ans_statement)

print(converted)