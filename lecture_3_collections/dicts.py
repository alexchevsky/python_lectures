# Словари
print()
print()

# Создание
client = {
    'name': 'Федор',
    'email':  'fedor@yandex.ru',
    'reg_date': '2021-01-01',
    'status': 'active',
    1: 'foobar',
}

# Извлечение

email = client['email']
name = client['name']

# Редактирование и добавление значений

client['name'] = 'Константин'
client['birth_date'] = '1990-01-01'
print(client)
print()

del client[1]
print(client)
print()

for k in client:
    print(k, client[k])
print()

print(client.keys())
print(client.values())
print()
print(client.items())
print()

for k, v in client.items():
    if k == 'name':
        print(v)
    elif k == 'reg_date':
        foo = v
print(foo)

name, email, reg_date, status, birth_date = client.items()
print(name, email, reg_date, status, birth_date)

x = {
    'foo': 1,
    'bar': 2
}

print()
print(sum(x.values()))

print()
print()
