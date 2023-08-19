import os
import csv
import json

print('' '')

# print(os.getcwd())

target_dir = 'lecture_5_automatization'

os.chdir('/Users/ak/Code/courses/python_lectures/lecture_5_automatization')

# obj = os.listdir()

# for o in obj:
#     print(o,
#           os.path.isfile(o),
#           os.path.isdir(o),
#           os.path.exists(o))

# data_file = 'data.csv'

# if not os.path.exists(data_file):
#     ...

# open a file
# with open('lecture_5.md', 'r') as f:
#     txt = f.read()
#     lines = f.readlines()
#     for line in f:
#         print(line)


# CSV
# comma-separated-values

new_user = ['Ivan,Ivan', 'Ivanov', 40]
with open('users.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(new_user)

one_more_new_user = {
    'first_name': 'Alexander',
    'last_name': 'Pushkin',
    'is_alive': False,
    'books': ['Капитанская дочка', 'Евгений Онегин']
}

with open('test.txt', 'w') as f:
    json.dump(one_more_new_user, f)

with open('test.txt', 'r') as f:
    u = json.load(f)
    print(u['first_name'])

print('' '')
