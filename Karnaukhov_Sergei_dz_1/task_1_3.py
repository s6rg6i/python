'''Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100'''

end_of_word = ''
last_digit = 0
word = 'процент'    ## заданное слово
for i in range(1, 101):
    last_digit = i % 10
    if 10 < i < 15:         ## исключаем 11,12,13,14
        end_of_word = 'ов'
    elif last_digit == 1:
        end_of_word = ''
    elif 2 <= last_digit <= 4:
        end_of_word = 'а'
    else:
        end_of_word = 'ов'
    print(f'{i} {word}{end_of_word}')
