# 4.4 Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
# Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
# Убедиться, что ничего лишнего не происходит.

import utils

print(f'Тукущая дата: {utils.currency_rates_date()}')
print(f'Курс "HUF" к RUB: {utils.currency_rates("HUF")}')
print(f'Курс "HKD" к RUB: {utils.currency_rates("HKD")}')
print(f'Курс "USD" к RUB: {utils.currency_rates("USD")}')
print(f'Курс "XXX" к RUB: {utils.currency_rates("XXX")}')
