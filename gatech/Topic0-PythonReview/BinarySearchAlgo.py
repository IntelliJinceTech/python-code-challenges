# Fast searching in ordered collections

# Binary Search Algorithm
# searching a value within a list

# left and right variables in the sorted list
# find mid point
# if value is above or below
# if above mid-point, set mid-point as left
# if below mid-point,set mid-point as right

def ordered_contains(S, x):
# You may assume that `S` is sorted
###
### YOUR CODE HERE
###
    left = 0
    right = len(S)-1

    while left <= right:
        mid = (left+right) // 2

        if S[mid] == x:
            # return mid
            return True
        # if midpoint value is less than target value, move right to mid - 1
        if S[mid] > x:
            right = mid-1
        else:
            left = mid + 1
    return False

A = [2, 16, 26, 32, 52, 71, 80, 88]


print("A contains 32: {}".format(ordered_contains(A, 32)))
print("A contains 7: {}".format(ordered_contains(A, 7)))
print("A contains -10: {}".format(ordered_contains(A, -10)))