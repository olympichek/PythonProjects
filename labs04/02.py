def concat(words):
    if len(words) == 0: return ''
    if len(words) == 1: return words[0]
    return ', '.join(words[:-1]) + ' і ' + words[-1]

n = int(input('Введіть кількість слів: '))
words = []
for i in range(n):
    word = input('Введіть слово: ')
    words.append(word)

result = concat(words)
print('Результат:', result)
