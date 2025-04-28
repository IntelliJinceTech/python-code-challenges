# input integer
# output list of numbers



def divisors(integer):
    return [n for n in range(2,integer-1) if integer % n == 0] or f'{integer} is prime'


print(divisors(25))

