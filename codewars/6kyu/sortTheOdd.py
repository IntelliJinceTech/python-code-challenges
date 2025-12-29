def sort_array(source_array):
    sorted_odds = sorted([i for i in source_array if i % 2 != 0])
    counter = 0
    new_array = []
    for num in range(0, len(source_array)):
        curr = source_array[num]
        if curr % 2 == 0:
            new_array.append(curr)
        else:
            new_array.append(sorted_odds[counter])
            counter += 1
    return new_array




# given array input
# output array output

# given array of numbers
# construct list of sorted ascending order of odd numbers from source array
# add counter for counting the list of odd numbers ascending
# for the range of length source array:
    # if even --> ignore or continue
    # if odd -->
        # add sorted odd number at counter
# return the new list


# print(sort_array([7,1]),[1,7])
# print(sort_array([5,8,6,3,4]),[3,8,6,5,4])
print(sort_array(([1, 111, 11, 11, 2, 1, 5, 0])))