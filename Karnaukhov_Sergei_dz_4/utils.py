import requests
import re
from decimal import Decimal
from datetime import date


def get_curr_ex_rates():
    """
    The function makes a request to the server 'http://www.cbr.ru/scripts/XML_daily.asp' and
    processes data with currency rates.
    :return: dictionary with the key {'DATA':date(yyyy/mm/dd)} and currency exchange rate in the format
     {'USD':{'CODE':'USD', 'NOMINAL':'1', 'NAME':'Доллар США', 'VALUE:'72,6642'}
    """
    keys = ('NumCode', 'CODE', 'NOMINAL', 'NAME', 'VALUE')  # needed keys XML
    currency_dict = {}
    resp_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    dat0 = d[0] if (d := re.search(r'\d\d.\d\d.\d{4}', resp_xml)) is not None else "01.01.9999"
    curr_date = date(int(dat0[6:10]), int(dat0[3:5]), int(dat0[:2]))  # year, month, year
    curr_list = [val for val in re.split(r'<[^>]+>', resp_xml) if len(val) != 0]  # XML --> list & remove blank str
    currency_dict.setdefault('DATE', curr_date)  # add pair: DATE: <date object>
    length = len(keys)
    for i, val in enumerate(curr_list):
        if (idx_0 := i % length) == 0:
            continue  # skip the <NumCode>
        if idx_0 == 1:
            currency_dict.setdefault(curr_list[i], {})  # base key <CharCode> (USD, EUR, BYN ...)

        if idx_0 == length - 1:  # Currency exchange rate in the form of 'dd,dddd'
            curr_list[i] = Decimal(curr_list[i].replace(',', '.'))  # в формат Decimal
        nested = curr_list[i - idx_0 + 1]
        currency_dict[nested].setdefault(keys[idx_0], curr_list[i])  # nested keys 'CODE', 'NOMINAL', 'NAME', 'VALUE'
    return currency_dict


def currency_rates(currency_code):          # вход код валюты <'USD'>
    currency_dict = get_curr_ex_rates()
    char_code = currency_code.upper()
    info = currency_dict.get(char_code)
    ret = None if info is None else info.get('VALUE') / int(info.get('NOMINAL'))  # м.б. за 100, за 10
    return ret                              # выход текущий курс


def currency_rates_date():
    return get_curr_ex_rates().get('DATE')


def currency_rates_args(*curr_codes):
    curr_dict_ret = {}
    curr_dict = get_curr_ex_rates()
    curr_dict_ret.setdefault('DATE', curr_dict.get('DATE'))
    for v in curr_codes:
        curr_dict_ret.setdefault(v.upper(), curr_dict.get(v.upper()))
    return curr_dict_ret


def print_hello(name):
    print(f'Hello, {name}')


if __name__ == '__main__':
    print_hello('Sergei')


