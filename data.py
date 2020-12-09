import requests
import json

URL = 'https://api.monobank.ua/bank/currency'

def get_data():
    response = requests.get(URL)
    data = json.loads(response.text)

    USD_buy = float(data[0]['rateBuy'])
    USD_sale = float(data[0]['rateSell'])
    EUR_buy = float(data[1]['rateBuy'])
    EUR_sale = float(data[1]['rateSell'])
    RUR_buy = float(data[2]['rateBuy'])
    RUR_sale = float(data[2]['rateSell'])

    exchange_rates = {"buy": (USD_buy, EUR_buy, RUR_buy), "sale": (USD_sale, EUR_sale, RUR_sale)}
    return exchange_rates
