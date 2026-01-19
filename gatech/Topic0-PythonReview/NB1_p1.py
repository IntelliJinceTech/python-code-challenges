# Exercise 2 - compress_vector_test
def compress_vector_test(L:list) -> dict:
    ###
    ### YOUR CODE HERE
    ###
    # take a list, create a dictionary
    # first key is "inds" with value of the indices of non zero
    # second key/value pair are the values themselves
    non_zero_ind = []
    non_zero_vals = []
    for ind,num in enumerate(L):
        if num != 0:
            non_zero_ind.append(ind)
            non_zero_vals.append(num)
    new_dict = {
        "inds": non_zero_ind,
        "vals": non_zero_vals
    }
    return new_dict

L=[0.0, 0.87, 0.0, 0.0, 0.0, 0.32, 0.46, 0.0, 0.0, 0.10, 0.0, 0.0]
# print(f'result={compress_vector_test(L)}')

# Repeated Indices

# multiple duplicate indices possibility with different values

# d['inds'] == [0, 3, 7, 3, 3, 5, 1]
# d['vals'] == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

# x == [1.0, 7.0 ( index of 'inds' and then apply to 'vals', 0.0, 2.0, 0.0, 6.0, 0.0, 3.0]

# inputs
#  dictionary of indicies and values
#  length of the full vector

# initialize a list * n of [0]
# loop to over d[inds]
#   for each loop:
#       the new list's index of inds += d[vals](index of d[ind] )

def decompress_vector_test(d: dict, n: int = None) -> list:
    # Checks the input
    assert type(d) is dict and 'inds' in d and 'vals' in d, "Not a dictionary or missing keys"
    assert type(d['inds']) is list and type(d['vals']) is list, "Not a list"
    assert len(d['inds']) == len(d['vals']), "Length mismatch"

    # Determine length of the full vector
    i_max = max(d['inds']) if d['inds'] else -1
    if n is None:
        n = i_max + 1
    else:
        assert n > i_max, "Bad value for full vector length"
    ###
    ### YOUR CODE HERE
    ###
    new_list = [0]*n
    for ind, val in enumerate(d['inds']):
        new_list[val] += d['vals'][ind]
    return new_list

### Demo function call
d = {'inds': [0, 3, 7, 3, 3, 5, 1],
     'vals': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
     }
# print(f'result={decompress_vector_test(d)}')

# exercise 4

def find_common_inds_test(d1:dict, d2:dict) -> list:
    intersection = set(d1['inds']) & set(d2['inds'])
    sorted_intersection = sorted(intersection)
    return sorted_intersection

### Demo function call
d1 = {'inds': [9, 9, 1, 9, 8, 1], 'vals': [0.28, 0.84, 0.71, 0.03, 0.04, 0.75]}
d2 = {'inds': [0, 9, 9, 1, 3, 3, 9], 'vals': [0.26, 0.06, 0.46, 0.58, 0.42, 0.21, 0.53, 0.76]}
print(f'result={find_common_inds_test(d1, d2)}')