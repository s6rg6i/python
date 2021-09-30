# 4.5. * Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
#> python task_4_5.py USD --> #75.18, 2020-09-05

import utils
from datetime import date

def main(argv):
   program, *args = argv
   currency_dict = utils.currency_rates_args(*args)
   print(f"Курсы Российского рубля (RUB) на {currency_dict.get('DATE').strftime('%d/%m/%Y')}:")
   for code in args:
       if (dc := currency_dict.get(code.upper())) is None:
           print(f'Код валюты ({code.upper()}) не найден в словаре')
           continue
       code, name, nom, val = dc.get('CODE'), dc.get('NAME'), dc.get('NOMINAL'), dc.get('VALUE')
       print(f'За {nom} {name}({code}) - {val} RUB')
   return 0


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))



