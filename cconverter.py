# write your code here!
import requests

currency_catche = list()
currency_catche.append(requests.get("http://www.floatrates.com/daily/usd.json").json())
currency_catche.append(requests.get("http://www.floatrates.com/daily/eur.json").json())


def currency_exchanger(code, exchange_code, money):
    currency_rate = requests.get(f"http://www.floatrates.com/daily/{code.lower()}.json").json()
    exchange_rate = requests.get(f"http://www.floatrates.com/daily/{exchange_code.lower()}.json").json()
    exchanged_money = float(currency_rate[f'{exchange_code.lower()}']['rate'] * float(money))
    print("Checking the cache...")
    if exchange_rate in currency_catche:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
    currency_catche.append(exchange_rate)
    print(f'You received {round(exchanged_money, 2)} {exchange_code}.')


your_currency = str(input())

while True:
        exchange_currency = str(input())
        if exchange_currency:
            money_ammount = float(input())
            currency_exchanger(your_currency, exchange_currency, money_ammount)
        else:
            break
