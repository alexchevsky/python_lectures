# if elif else

n_good_campaigns = 9

revenue = 1534
theshhold = 1000
cost = 5320

# revenue > threhsold
# revenue > cost
# n_good_campaigns += 1
# print Всего хороших кампаний: n_good_campaigns
# если кампания плохая, но количество хороших кампаний больше 10
# print Эта кампания так себе, но хороших уже много!
# print Эта кампания так себе, давайте посмотрим следующую!


print()
if revenue > theshhold:
    if revenue > cost:
        n_good_campaigns += 1
        print(f'Всего хороших кампаний: {n_good_campaigns}')
elif n_good_campaigns > 10:
    print('Эта кампания так себе, но хороших уже много!')
else:
    print('Эта кампания так себе, давайте посмотрим следующую!')
print()
