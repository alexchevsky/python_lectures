print()
print()

txt = 'Это текст!'
txt2 = "Это тоже текст!"

# Hello, I'm Alex!
my_name = 'Hello, I\'m Alex!'
my_name2 = "Hello, I'm Alex!"
book = 'My favourite book is "The Lord of the Rings"'

# Операции с текстом

# print(txt, txt2, my_name, my_name2)

# получение подстроки
book = 'My favourite book is "The Lord of the Rings"'
# print(book[10::])

# измерить длинну строки
print('Длина строки: ' + str(len(book)))

# умножение текста
print('-' * 30)

# найти подстроку с строке
print('@' in book)

print(book.upper())
print(book.lower())

# подставлять в текст значение переменных
template = 'Привет, username. Спишь?'
name = 'Сергей'

# Привет, Алексей. Спишь?

#print('Привет, ' + name + '. Спишь?')
print('Привет, {}. Спишь?'.format(name))
print(f'Привет, {name}. Спишь?')

print(f"""Привет, {name}!  Как дела?
Да все отлично! Вот, учу Python!
Ну ты молодец!""")

print()
print()