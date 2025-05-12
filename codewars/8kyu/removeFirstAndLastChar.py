#It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry about strings with less than two characters.


def remove_char(s):
    # string is an array
    # output is what's left after removing the first and last characters
    return s[1:-1]

print(remove_char("Hello"), 'ell')
print(remove_char("eloquent"), 'loquen')