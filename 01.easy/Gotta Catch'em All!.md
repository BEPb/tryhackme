[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Gotta Catch'em All!](https://tryhackme.com/r/room/pokemon) 

Всего 1 заданиe:
## Задание 1
Не забудьте подключиться к сети VPN с помощью OpenVPN. Для правильного развертывания устройства может потребоваться 
некоторое время.

Вы также можете развернуть собственную машину Kali Linux и управлять ею в своем браузере, используя предоставленную 
машину Kali (требуется подписка). 

Наслаждайтесь комнатой!

### Ответьте на вопросы ниже
Найдите покемона травяного типа
```commandline
nmap -sC -sV <IP>
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.30medium.txt
# http://<IP>
pokemon:hack_the_pokemon
ssh pokemon@<IP>
cd /Desktop
ls -la
unzip P0kEm0n.zip
cd P0kemon
cat grass-type.txt
# HEX decoder
```
```commandline
PoKeMoN{Bulbasaur}
```
Найдите покемона водного типа
```commandline
cd /var/www/html
ls -la
cat water-type.txt
# Caesar Cipher Cryptography Algorithm shift : 14
```
```commandline
Squirtle_SqUaD{Squirtle}
```
Найдите покемона огненного типа
```commandline
sudo -l
sudo su
locate fire-type.txt
cd /etc/why_am_i_here
cat fire-type.txt

cat fire-type.txt | base-64 -d
```
```commandline
P0k3m0n{Charmander}
```
Кто любимый покемон Рута?
```commandline
cat /home/roots-pokemon.txt
```
```commandline
Pikachu!
```
Поздравляю! Большое спасибо за прохождение Pokemon Room!
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)