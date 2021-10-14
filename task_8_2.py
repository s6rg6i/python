# 8.2. * Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
#  (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
#  например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
#        "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

import re
import requests

# rex = re.compile(r"^[\d.]+|(?<=\[)[\w+ :/]+|(?<=\] \")\w+|/\w+/\w+|(?<=\" )\d+|\d+(?= \")")
# re пришлось уточнить т.к в некоторых строках адреса были: <2a01:7e00::f03c:91ff:fe70:a4cc> вместо <54.183.198.11>

rex = re.compile(r"^[\w.:]+(?= - - )|(?<=\[)[\w+ :/]+|(?<=\] \")\w+|/\w+/\w+|(?<=\" )\d+|\d+(?= \")")

print('Считываем страницу с github и записываем в файл "nginx_logs.txt" ...')
with open('nginx_logs.txt', 'w+', encoding='utf-8') as f:
    f.writelines(requests.get(
        'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)

print('Делаем парсинг и записываем в файл "nginx_parsed_logs.txt" ...')
parsed_raw = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        parsed_raw.append(tuple(re.findall(rex, line)))
with open('nginx_parsed_logs.txt', 'w', encoding='utf-8') as fw:
    for list0 in parsed_raw:
        fw.write(f"{' '.join(list0)}\n")
print(f'1-я строка: {parsed_raw[:1]}')
