# comprehension
print()
print()

sales = [10, 5, 6, 8, 1]

total = sum([x for x in sales if x < 10])
print(total)
print()

client = {
    'name': 'Федор',
    'email':  'fedor@yandex.ru',
    'reg_date': '2021-01-01',
    'status': 'active',
    'n_order': 12,
    'total_sales': 100500
}

# res = []
# for k, v in client.items():
#     if type(v) == int:
#         res.append(v)

res = {k: v for k, v in client.items() if type(v) == int}
print(res)
print()

# enumeration

sales = [10, 5, 6, 8, 1]

for i, x in enumerate(sales):
    if i % 2 == 0:
        sales[i] *= 2
print(sales)

print()
print()
