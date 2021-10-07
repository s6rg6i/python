# 6.1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [...  ('141.138.90.60', 'GET', '/downloads/product_2'),
#       ('141.138.90.60', 'GET', '/downloads/product_2'),
#       ('173.255.199.22', 'GET', '/downloads/product_2'),  ...]
# str типа '80.91.33.133 - - [17/May/2015:08:05:24 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 ....'

import requests


def parse_string(str_in):
    s = str_in.split('"', maxsplit=1)
    s1 = s[1].split(maxsplit=2)
    ret = (s[0].split(maxsplit=1)[0], s1[0], s1[1])
    return ret


file_users = open('nginx_logs.txt', 'w+', encoding='utf-8')
file_users.write(requests.get(
    'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)
file_users.close()

nginx_log = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for s in file:
        nginx_log.append(parse_string(s))
print(nginx_log[:10])
