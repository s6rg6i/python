# 8.1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
#       >>> email_parse('someone@geekbrains.ru')
#               {'username': 'someone', 'domain': 'geekbrains.ru'}
#       >>> email_parse('someone@geekbrainsru')
#               Traceback (most recent call last):
#               File "<stdin>", line 1, in <module>
#               ...
#               raise ValueError(msg)
#               ValueError: wrong email: someone@geekbrainsru

import re


def email_parse(adr):
    if (match := re.fullmatch(r'[\w\.-]+@[\w\.-]+(\.[\w]+)+', val)) is None:
        raise ValueError(f'ValueError: wrong email: {adr}')
    return {'username': re.search(r"[\w\.+-]+(?=@)", match[0])[0],
            'domain': re.search(r"(?<=@)[\w\.-]+(\.[\w]+)+", match[0])[0]}


mail_list = ['someone@geekbrains.ru', 'so-m_eo.ne@geek.bra.ins.ru', 'Some_One.geekbrains.ru']

for val in mail_list:
    parse_dic = email_parse(val)
    print(parse_dic)
pass
