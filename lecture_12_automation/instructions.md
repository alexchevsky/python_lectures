
Шаблон для запуска программы с помощью cron
```
* * * * * [python] [programm] >> [log file] 2>&1
```


Закрываем доступ к файлу с ключем
```
chmod 600 [secret key file]
```

Подключаемся к серверу:

```
ssh [user_name]@[server_address] -i [secret_key]
```

Копируем файл на сервер:
```
scp -i [secret key file] [file to copy] [user_name]@[server ip]:[path on server]
```

Как сохранить текущее окружение в файл (не забудьте предварительно активировать окружение):
```
pip freeze > requirements.txt
```

Устанавливаем пакеты из requirements.txt:
```
pip install -r requirements.txt
```
