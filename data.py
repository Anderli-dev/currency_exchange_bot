import requests
import json

URL = 'https://api.monobank.ua/bank/currency'


def get_data():
    response = requests.get(URL)
    data = json.loads(response.text)
    return data


def get_exchange_rates(data):
    # 1 справочник кода валют
    # 2 пройти 3 елемента списка
    # 3 создать словарь : ключ название валюты по коду , значение обект класса
    exchange_rates = {}
    exchange_code = {"840": "usd", "978": "eur", "643": "rur"}
    for i in range(3):
        key = exchange_code[str(data[i]["currencyCodeA"])]
        sell = round(float(data[i]['rateSell']), 2)
        buy = round(float(data[i]['rateBuy']), 2)
        exchange_rates[key] = Currency(sell, buy)
    return exchange_rates


class Currency:
    def __init__(self, sell, buy):
        self.sell = sell
        self.buy = buy


exchange_rates = get_exchange_rates(get_data())
