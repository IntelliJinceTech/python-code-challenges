import math
def litres(time):
    # return math.floor(time*0.5)
    return time // 2

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
#
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# given time in float
# multiply 0.5 litres with the input time
# return an integer rounded down


print(litres(6.7),3)  # 3
print(litres(3),1)  # 1
print(litres(11.8),5)  # 3