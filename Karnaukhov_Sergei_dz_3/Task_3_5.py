# 3.5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice, sample


def get_jokes(num, is_repeat=False):
    """
    returns n jokes formed from three random words
    :param num: int - number of jokes
    :param is_repeat: if False, words in phrases can be repeated
    :return: list of jokes
    """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    phrases = []

    if is_repeat:
        num = num if 0 < num < len(nouns) else len(nouns)   # шутки без повтора ограничены длиной списка слов
        phrases = [val for val in sample(nouns, num)]
        for i, val in enumerate(sample(adverbs, num)):
            phrases[i] += f' {val}'
        for i, val in enumerate(sample(adjectives, num)):
            phrases[i] += f' {val}'
    else:
        for i in range(num):
            phrases.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return phrases


print(get_jokes(5, True))
print(get_jokes(8))
