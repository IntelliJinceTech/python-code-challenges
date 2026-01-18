#

# John has f0 dollars in his bank account at the beginning of year 1. Each year, he will earn some interest and withdraw some money. He asks you, his financial manager, to help him come up with a sustainable plan, meaning one that allows him to survive until the n-th year. That is, there should be some nonzero amount of money in his account at the beginning of year n.
#
# Here are the parameters and rules you need to consider:
#
#     During the first year, John will withdraw c0 dollars for his expenses. However, his expenses increase by i percent per year in subsequent years due to inflation. This increase compounds from year to year. However, the value i does not change.
#     The interest rate is p percent per year and does not change. The interest he will earn that year is determined at the end of the year, based on the account's balance after withdrawing expenses.
#     When calculating the expenses for a given year, you should round up the decimal part, if any.
#     When calculating the interest for a given year, you should truncate the decimal part (that is, keep only the integer part).
#
# Suppose f0=100000 (one-hundred thousand) dollars, p=1 percent, n=12, and i=1.1 percent. Between which of the following values of c0  is this plan sustainable? (For example, if you pick "1000 <= c0 <= 2000", then you believe John will have some money at the start of year 12 when c0=1000, but if c0=2000, then he will not have money at the start of year 12.)

# starting = 100000
# p=0.01
# n = 12
# i = 0.011

# print((i**12)*starting)

import math

def banker_withdraw(f0, p, n, i, c0):
    balance = f0
    for year in range(1,n):
        expense = math.ceil(c0 * ((1+i/100) ** (year-1))) # not inclusive of n because we only care abou the start of year n
        # year n expenses haven't happened yet
        balance -= expense
        # withdraws money before interest is calculated


        if balance <= 0:
            return balance
        interest = int(balance * (p/100))
        # calculated after expenses
        balance += interest
        # balance is added so that we have the balance for the start of the next year
    return balance

print(banker_withdraw(100000, 1, 12, 1.1, 1000 ))


# def fortune(f0, p, c0, n, i):
#     # f0 = starting money in bank account
#     # p = interest rate
#     # needs to be / 100
#     # interest needs to be calculated from interest rate * balance
#     # interest would be added back onto f0
#     # c0  = withdraw amount
#     # n = years
#     # i = inflation
#
#     #
#
#     balance = f0
#
#     for year in range(1, n):
#         living_expenses = int(c0 * (1 + (i / 100) ** (year - 1)))
#         balance -= living_expenses
#
#         interest = int(balance * p / 100)
#         balance += interest
#
#     return True if balance >= 0 else False
#
#
# #         balance -= c0
#
# print(fortune(100000, 1, 9185, 12, 1), False)


def fortune(money, interest, withdraw, years, inflation):
    interest = 1 + (interest / 100)
    inflation = 1 + (inflation / 100)
    for _ in range(years - 1):
        money = int(money * interest - withdraw)
        if money < 0:
            return False
        withdraw *= inflation
    return True
