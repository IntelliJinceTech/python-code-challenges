def abbrev_name(name):
    # arr = name.split()
    # return f'{arr[0][0].upper()}.{arr[1][0].upper()}'
    # return '.'.join(w[0] for w in name.split()).upper()
    for w in name.split():
        return (w[0], name.split())
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# patrick feeney => P.F

print(abbrev_name("Sam Harris"))



