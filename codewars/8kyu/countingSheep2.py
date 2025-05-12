def count_sheeps(sheep):
    return sheep.count(True)

# Count the number of sheep present / truthy in the sheep list/array

print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))

# 17