from currencies import Currency
from currency_converter import CurrencyConverter


def getCurrency(curr, amt):
    nCurr = Currency(curr)
    cash = nCurr.get_money_with_currency_format(amt)
    return cash


def main():
    conv = CurrencyConverter()
    money = input("How many dollars in USD do you have? ")
    changed = conv.convert(money, 'USD', "EUR")

    owned = getCurrency('USD', money)
    result = getCurrency('EUR', changed)
    print(f'If you have {owned} that is equivalent to {result}')


if __name__ == '__main__':
    main()
