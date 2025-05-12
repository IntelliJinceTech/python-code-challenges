# Complete the square sum function so that it squares each number passed into it and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because

def square_sum(numbers):
    # sum = 0
    # for num in numbers:
    #     sum += num**2
    # return sum
    return sum([n**2 for n in numbers])


print(square_sum([1,2,2])) # 9
print(square_sum([])) # 0
