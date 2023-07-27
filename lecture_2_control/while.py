print("""Python 3.8.9 (default, Apr 13 2022, 08:48:06) 
[Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.""")

while True:
    com = input('>>> ')
    if com[:5] == 'print':
        com = com.replace('"', '\'')
        print(com.split("'")[1])
    else:
        print('ERROR')
