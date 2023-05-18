import requests


def main():
    base_currency = 'RUB'
    convert_currency = 'EUR'
    url = f'https://api.apilayer.com/exchangerates_data/latest?symbols={convert_currency}&base={base_currency}'

    headers = {
        "apikey": "bWaAfkwWh4ykoD5Bcor5148TG6mmT2Vj"
    }

    response = requests.request('GET', url, headers=headers)

    return response.text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(main())

