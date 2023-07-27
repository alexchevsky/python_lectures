# окупаемость:
# 1. выручка должна быть больше порогового значения
# 2. выручка должна быть больше расходов

threshold = 1000

revenue = 1423
cost = 5234

large_enough = revenue > threshold
roas_positive = revenue > cost

print()
print(large_enough and roas_positive)
print()

# text = '/Users/ak/Code/courses/python_lectures/lecture_2_control/logic_operations.py'
# search_query = 'ромашка'

# print(f'Нашли {search_query}?', search_query in text)
