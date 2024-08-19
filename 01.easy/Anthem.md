[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Anthem](https://tryhackme.com/r/room/anthem) 

Всего 3 задания:
## Задание 1
Это задание потребует от вас внимания к деталям и поиска «ключей к замку».

Эта комната предназначена для новичков, однако попробовать ее может каждый!

Наслаждайтесь гимном.

В этой комнате вам не нужно брутфорсить страницу входа. Только ваш любимый браузер и удаленный рабочий стол.

Дайте устройству до 5 минут на загрузку и настройку.

### Ответьте на вопросы ниже
Давайте запустим nmap и проверим, какие порты открыты.
```commandline
nmap -sS -sV -A <IP>
```
```commandline
Ответ не требуется
```
Какой порт у веб-сервера?
```commandline
80
```
Какой порт предназначен для службы удаленного рабочего стола?
```commandline
3389
```
Какой возможный пароль находится на одной из страниц, которые проверяют веб-сканеры?
```commandline
# http://<IP>/robots.txt
```
```commandline
UmbracoIsTheBest!
```
Какую CMS использует сайт?
```commandline
Umbraco
```
Какой домен у сайта?
```commandline
anthem.com
```
Как зовут администратора?
```commandline
Solomon Grundy
```
Можем ли мы найти адрес электронной почты администратора?
```commandline
SG@anthem.com
```

## Задание 2
Наш любимый администратор оставил несколько флагов, которые нам нужно собрать, прежде чем мы приступим к следующему заданию.

### Ответьте на вопросы ниже
Что такое флаг 1?
```commandline
# http://<IP>/archive/we-are hiring/ > view source code
```
```commandline
THM{L0L_WH0_US3S_M3T4}
```
Что такое флаг 2?
```commandline
http://<IP>/archive/a-cheers-to-our-itdepartments/ > view source code
```
```commandline
THM{G!T_G00D}
```
Что такое флаг 3?
```commandline
http://<IP>/authors/jane-doe/
```
```commandline
THM{L0L_WH0_D15}
```
Что такое флаг 4?
```commandline
http://<IP>/archive/a-cheers-to-our-it-departmenst/ > view source code
```
```commandline
THM{AN0TH3R_M3TA}
```

## Задание 3
Давайте заглянем в коробку, используя собранные нами данные.

### Ответьте на вопросы ниже
Давайте придумаем имя пользователя и пароль для входа в ящик. (Ящик не находится на домене)
```commandline
Ответ не требуется
```
Получите начальный доступ к машине. Каково содержимое файла user.txt?
```commandline
rdesktop -u SG -p UmbracoIsTheBest! <IP>
user.txt
```
```commandline
THM{N00T_NO0T}
```
Можем ли мы узнать пароль администратора?
```commandline
select restore.txt > Right click > properties > security > edit >type SG and click check nanes> ok>apply.
```
```commandline
ChangeMeBaby1MoreTime
```
Повысьте свои привилегии до root. Каково содержимое файла root.txt?
```commandline
C://Users/Administrator/Desktop/root.txt
```
```commandline
THM{Y0U_4R3_1337}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)