
def create_phone_number(n):
    return f"({''.join(str(x) for x in (n[0:3]))}) {''.join(str(x) for x in n[3:6])}-{''.join(str(x) for x in n[6:10])}"


# input array of 10 integers
# output string of those numbers in form of a phone number "(123) 456-7890"


print(create_phone_number([1,2,3,4,5,6,7,8,9,0])) # "(123) 456-7890"