
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.
import math

def century(year):
    # todo given year - always round up to the nearest two digits

    return math.ceil(year/100)


print(century(1705)) # 18
print(century(1900)) # 19
print(century(1601)) # 17
print(century(2000)) # 20
print(century(2742)) # 28
