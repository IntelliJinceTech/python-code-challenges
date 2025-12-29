def small_enough(array,limit):
    for num in array:
        if num > limit:
            return False
    return True

# Given an array and a limit value
# output a boolean
# check if all values are below or equal to the limit value - if they are:
    # TRUE
# else false

print(small_enough([66, 101],200)) # True
print(small_enough([66, 101,201],200)) # False