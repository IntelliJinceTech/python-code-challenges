def sort_by_length(arr):
    return sorted(arr, key=len)

# take in a list
# output a list
# for each element in the list
    # count length for each element
    # sort from least to greatest length
# return list in sorted order

print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))  # ["Eyes", "Glasses", "Monocles", "Telescopes"]