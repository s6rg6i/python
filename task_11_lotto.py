# 11.0. Игра в лото
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, расположенных по возрастанию.
# Все цифры в карточке уникальны.
# Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается случайная карточка. Каждый ход выбирается
# один случайный бочонок и выводится на экран. Также выводятся карточка игрока и карточка компьютера.
#
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#     Если цифра есть на карточке - она зачеркивается и игра продолжается.
#     Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#     Если цифра есть на карточке - игрок проигрывает и игра завершается.
#     Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
# ..6..7.........49....57.58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
#
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

from random import sample, randint


class LottoCard:
    def __init__(self, player_type):
        self.MAX_NUM = 90  # количество боченков
        self.NUM_IN_LINE = 5  # количество чисел на одной линии карточки
        self.FIELDS_IN_LINE = 9  # количество полей для чисел на одной линии карточки
        self.player_type = player_type  # игрок или программа
        self.card = [[0 for _ in range(self.FIELDS_IN_LINE)] for _ in range(3)]  # карточка 3 строки с числами
        self.card_nums = sorted(
            sample(range(1, self.MAX_NUM + 1), self.NUM_IN_LINE * 3))  # случ. сорт. набор чисел (15)

        nums = [self.card_nums[i:i + self.NUM_IN_LINE] for i in range(0, self.NUM_IN_LINE * 3, self.NUM_IN_LINE)]
        idx = [sorted(sample(range(self.FIELDS_IN_LINE), self.NUM_IN_LINE)) for _ in range(3)]  # случ. индексы
        for line, val, idx in zip(range(3), nums, idx):  # расставляем числа по пять в линию по случайным индексам
            for i in range(self.NUM_IN_LINE):
                self.card[line][idx[i]] = val[i]

    def __str__(self):
        card_images = self.get_card_image()
        return '\n'.join([''.join([i for i in x]) for x in card_images])

    def get_card_image(self):
        # формируем список из строк, чтобы join можно было собрать
        # отдельный метод - для печати нескольких карточек в линию. Реализовано в след. классе
        card_image = [['   ' for _ in range(self.FIELDS_IN_LINE)] for _ in range(3)]
        for i, line in enumerate(self.card):
            for j, val in enumerate(line):
                if val > 0:
                    card_image[i][j] = str(val).rjust(3)
                elif val < 0:
                    card_image[i][j] = ' XX'
        return card_image

    def get_player_name(self):
        return self.player_type.ljust(self.FIELDS_IN_LINE * 3, '-')

    def get_matched_quantity(self):
        return self.NUM_IN_LINE * 3 - len(self.card_nums)

    def is_exist(self, num):
        # проверяет, есть ли номер бочонка: True - есть, False - нет, None - все числовые поля закрыты
        if num not in self.card_nums:
            return False
        self.card_nums.pop(self.card_nums.index(num))  # удаляем из одномерного списка
        for i, val in enumerate(self.card):
            if num in val:
                val[val.index(num)] = -num
        return True if len(self.card_nums) > 0 else None


class LottoGame:
    def __init__(self, player_type1):
        self.player_type1 = player_type1
        self.player1 = LottoCard(player_type1)  # карточка игрока
        self.player2 = LottoCard('Computer')  # карточка компьютера
        self.max_barrel = self.player1.MAX_NUM  # максимальное количество бочонков
        self.barrels = []  # список бочонков, уменьшающийся на 1 с каждым ходом

    def __str__(self):
        card1 = self.player1.get_card_image()  # отображение двух карточек в линию
        card2 = self.player2.get_card_image()
        separator = [[' | '], [' | '], [' | ']]
        for i in range(3):
            card1[i].extend(separator[i])
            card1[i].extend(card2[i])
        s = self.player1.get_player_name() + '   ' + self.player2.get_player_name() + '\n'
        s += '\n'.join([''.join([i for i in x]) for x in card1]) + '\n' + '-' * len(s)
        return s

    def play(self):
        # Логика игры. Сама игра - 2-й while, 1-й - для повторения по запросу.
        # Ввел еще возможность задания ограничения количества ходов. Обработка результата в блоке else.
        while True:
            self.player1 = LottoCard(self.player_type1)
            self.player2 = LottoCard('Computer')
            self.barrels = list(range(1, self.max_barrel + 1))
            try:
                max_step = int(input(f'Введите до скольких ходов играем от 1 до {self.max_barrel}:'))
                max_step = max_step if 0 < max_step < self.max_barrel else self.max_barrel
            except ValueError:
                max_step = len(self.barrels)
            print(self)
            while self.max_barrel - len(self.barrels) < max_step:
                new_barrel = self.barrels.pop(randint(0, len(self.barrels) - 1))
                is_matching_1 = self.player1.is_exist(new_barrel)
                is_matching_2 = self.player2.is_exist(new_barrel)
                print(f'Новый бочонок:({new_barrel}){" "*29}осталось:{max_step - self.max_barrel+len(self.barrels)}')
                is_yes = True if input('Зачеркнуть цифру? (y/n)').lower() == 'y' else False
                if is_matching_1 is not None and is_matching_2 is None:
                    print('Увы, Вы проиграли.')
                    break
                if is_yes and is_matching_1 is None and is_matching_2 is None:
                    print('Поздравляем! Ничья! Вы одновременно закрыли каточки.')
                    break
                if is_yes and is_matching_1 is None:
                    print('Поздравляем! Вы победили!')
                    break
                is_matching_1 = False if is_matching_1 is False else True
                if (not is_yes and is_matching_1) or (is_yes and not is_matching_1):
                    print('Увы...Вы проиграли из-за невнимательности!')
                    break
                print(self)
            else:
                q1, q2 = self.player1.get_matched_quantity(), self.player2.get_matched_quantity()
                s = 'Поздравляем! Вы победили!' if q1 > q2 else 'Поздравляем! Ничья!' if q1 == q2 else 'Вы проиграли.'
                print(f'Игра закончилась. {s} У Вас закрыто полей: {q1}. У противника {q2}.')
            if input('Новая игра? (y/n)').lower() == 'y':
                continue
            else:
                break


lotto = LottoGame('Игрок 1')
lotto.play()
