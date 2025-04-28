# input string
# output string

def maskify(cc):
    # -4 is the index
    # maskStr = ""
    if len(cc) > 4:
        return f'{(len(cc)-4)*"#"}{cc[-4:]}'
    return cc
    # print(cc[-4]) # i



# print(maskify("skippy")) #"##ippy"
print(maskify("123"))