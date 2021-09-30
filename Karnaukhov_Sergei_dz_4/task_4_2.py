# 4.2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить
# поставленную задачу? Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

# 4.3.* Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
# как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

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


#     code, name, nom, val = info.get('CODE'), info.get('NAME'), info.get('NOMINAL'), info.get('VALUE')
#     s = f'Текущий курс: за {nom} {name}({code}) - {val} RUB'

req_curr = ['Usd', 'eur', 'gbr', 'huf', 'HKD']
currency_dict = currency_rates_args(*req_curr)
print(f"Курсы Российского рубля (RUB) на {currency_dict.get('DATE').strftime('%d/%m/%Y')}:")
for code in req_curr:
    if (dc := currency_dict.get(code.upper())) is None:
        print(f'Код валюты ({code.upper()}) не найден в словаре')
        continue
    code, name, nom, val = dc.get('CODE'), dc.get('NAME'), dc.get('NOMINAL'), dc.get('VALUE')
    print(f'За {nom} {name}({code}) - {val} RUB')


print(f'Тукущая дата: {currency_rates_date()}')
print(f'Курс "HUF" к RUB: {currency_rates("HUF")}')
print(f'Курс "HKD" к RUB: {currency_rates("HKD")}')
print(f'Курс "USD" к RUB: {currency_rates("USD")}')
print(f'Курс "XXX" к RUB: {currency_rates("XXX")}')

