# def count_sheeps(sheep):
#     num_sheep = 0
#     for n in sheep:
#         if n:
#             num_sheep +=1
#     return num_sheep

def count_sheeps(sheep):
    return sheep.count(True)

print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))