def nb_dig(n,d):

    squared_list = [n**2 for n in range(1,n+1)]
    cnt = 0
    for squared in squared_list:
        cnt += str(squared).count(str(d))
    return cnt if d>0 else cnt+1



    # integer n and digit d
    # square all numbers k between 0 and n
    # count the number of digits d is used in the writing of all the numbers in the list
    # return the count

print(nb_dig(10,1)) # 4
print(nb_dig(25,1)) # 11
print(nb_dig(10576,9)) # 7860
print(nb_dig(854,0)) # 521