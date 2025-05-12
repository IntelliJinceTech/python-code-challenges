def digitize(n):
#     turn into array
#     reverse array
#     return the reversed array
#     arr = list(str(n))[::-1]
#     new_arr = [int(num) for num in arr]
#     return new_arr
      return [int(num) for num in str(n)[::-1]]


print(digitize(35231), f'is the same as {[1, 3, 2, 5, 3]}?')
print(digitize(0), f'is the same as {[0]}?')

