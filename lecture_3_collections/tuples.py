# tuples / кортежи
print()

# создание
sales = 10, 5, 6, 8, 1
# sales = (10, 5, 6, 8, 1)
# sales = (10,)
# sales = ()

print()
print(sales)
print()

# Извлечение данных
print(sales[1:4])
print()

# Агрегирование
txt = '/ak/Code/courses/'
print(len(txt))

print(sum(sales))
print(max(sales))
print(min(sales))
print(len(sales))
print()

# Перебор
test_results = (5, 2, 4, 'na', 5)
# print(sum(test_results))

total = 0
for result in test_results:
    if (type(result) == int) or (type(result) == float):
        total += result

print(total)

# Распаковка

test_results = 5, 2, 4

res1, res2, _ = test_results

print(res1, res2)
