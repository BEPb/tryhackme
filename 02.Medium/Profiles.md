[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Profiles](https://tryhackme.com/r/room/profilesroom) 

Всего 1 заданиe:
## Задание 1
Группа реагирования на инциденты предупредила вас о подозрительной активности на одном из серверов баз данных Linux.

Был сделан дамп памяти сервера, который был предоставлен вам для анализа. Вы сообщаете команде, что вам не хватает 
важной информации с сервера, но он уже отключен. Они просто немного усложнили вашу работу, но не сделали ее 
невозможной.

Нажмите кнопку Download Task Files в верхней части этого задания. Вам будет предоставлен файл доказательства .zip.

Извлеките содержимое zip-файла и начните анализ, чтобы ответить на вопросы.
Примечание: лучше всего выполнить задачу, используя собственную среду.  Я рекомендую использовать Volatility 2.6.1 
для решения этой задачи и настоятельно рекомендую использовать эту статью Шона Уэйлена, которая поможет вам с 
установкой Volatility.

### Ответьте на вопросы ниже
Какой пароль root раскрыт?

Volatility — это инструмент командной строки, который позволяет группам цифровой криминалистики и реагирования на 
инциденты анализировать дамп памяти для выполнения анализа памяти. 

Volatility написан на Python и может анализировать снимки, сделанные в Linux, Mac OS и Windows.

Волатильность имеет широкий спектр применения, включая следующие:
- Список всех активных и закрытых сетевых подключений.
- Список запущенных процессов устройства на момент захвата.
- Список возможных значений истории командной строки.
- Извлечение возможных вредоносных процессов для дальнейшего анализа.
И этот список можно продолжать.

https://github.com/volatilityfoundation/volatility



```commandline
Ftrccw45PHyq
```
И в какое время примерно был доступ к файлу users.db? Формат ГГГГ-ММ-ДД ЧЧ:ММ:СС 
```commandline
2023-11-07 03:49:45
```
Каков MD5-хеш найденного вредоносного файла?
```commandline
0511ccaad402d6d13ce801e1e9136ba2
```
Какой IP-адрес и порт у злоумышленника? Формат IP:Port
```commandline
10.0.2.72:1337
```
Какой полный путь к файлу cronjob и его номер inode? Формат: имя_файла: номер inode
```commandline
/var/spool/cron/crontabs/root:131127
```
Какая команда находится внутри файла cronjob?
```commandline
* * * * * cp /opt/.bashrc /root/.bashrc
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)