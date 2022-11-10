"""Bonus exercise to input a string, count the number of characters in the string and print that value out to the command line"""

# title = input("Please input the title of your book: ")

# print(f"Your book's title is {len(title)} characters in length.")
# """___________________________________________________________________________________"""
from currencies import Currency
from currency_converter import CurrencyConverter


def getCurrency(curr, amt):
    nCurr = Currency(curr)
    cash = nCurr.get_money_format(amt)
    return cash


conv = CurrencyConverter()
money = input("How many dollars in USD do you have? ")
changed = conv.convert(money, 'USD', "EUR")

owned = getCurrency('USD', money)
result = getCurrency('EUR', changed)
print(f'If you have {owned} that is equivalent to {result}')
