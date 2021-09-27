# 3.2. Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One") --> "Один"
# >>> num_translate_adv("two") -->"два"


dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'
        }

test_list = ['zEro', 'One', 'two', 'ThrEe', 'Four', 'five', 'Six', 'Seven', 'eight', 'Nine', 'teN']


def num_translate_adv(eng_num):
    if dict.get(eng_num.lower()) is None:
        return None
    return dict[eng_num.lower()].capitalize() if eng_num[:1].isupper() else dict[eng_num.lower()]


for val in test_list:
    print(val, end=' --> ')
    print(num_translate_adv(val))
