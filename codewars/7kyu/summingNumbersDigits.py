def sum_digits(number):
    return sum(map(int, str(abs(number))))

# number input
# number output
# split converted string of number into a list
# turn each element of the list back into a number and take the absolute value
# sum
# return sum

print(sum_digits(-32))
