[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [ffuf](https://tryhackme.com/r/room/ffuf) 

Всего 9 заданий:
## Задание 1
Краткое содержание

ffuf означает Fuzz Faster U Fool . Это инструмент, используемый для веб-перебора, фаззинга и брутфорса каталогов.

Установить ффуф

ffuf уже включен в следующие дистрибутивы Linux :
- BlackArch
- Пентоо
- Кали
- Попугай
Поиск по Repology для других дистрибутивов

Примечание: Repology — это служба , которая отслеживает множество репозиториев пакетов и других источников, а также 
собирает данные о версиях пакетов программного обеспечения, сообщая о новых выпусках и проблемах с упаковкой. 

Если он не включен в ваш дистрибутив Linux, вы можете развернуть его вручную, следуя инструкциям по установке.

Установить SecLists

SecLists — это набор списков различных типов, используемых при оценке безопасности. Типы списков включают имена 
пользователей, пароли, URL-адреса, шаблоны конфиденциальных данных, полезные нагрузки фаззинга, веб-шеллы и многое 
другое.  

SecLists уже включен в следующие дистрибутивы Linux :
- BlackArch
- Пентоо
- Кали
- Попугай
Поиск по Repology для других дистрибутивов
Если он не включен в ваш дистрибутив Linux, вы можете развернуть его вручную, следуя инструкциям по установке .

### Ответьте на вопросы ниже
У меня установлен ffuf
Ответ не требуется

Правильный ответ
У меня установлен SecLists

```commandline
Ответ не нужен
```

## Задание 2
Страницу справки можно отобразить с помощью, ffuf -hи она будет полезна, так как мы будем использовать множество опций.

```commandline

Fuzz Faster U Fool - v1.3.0-dev

HTTP OPTIONS:
  -H                  Header `"Name: Value"`, separated by colon. Multiple -H flags are accepted.
  -X                  HTTP method to use
  -b                  Cookie data `"NAME1=VALUE1; NAME2=VALUE2"` for copy as curl functionality.
  -d                  POST data
  -ignore-body        Do not fetch the response content. (default: false)
  -r                  Follow redirects (default: false)
  -recursion          Scan recursively. Only FUZZ keyword is supported, and URL (-u) has to end in it. (default: false)
  -recursion-depth    Maximum recursion depth. (default: 0)
  -recursion-strategy Recursion strategy: "default" for a redirect based, and "greedy" to recurse on all matches (default: default)
  -replay-proxy       Replay matched requests using this proxy.
  -timeout            HTTP request timeout in seconds. (default: 10)
  -u                  Target URL
  -x                  Proxy URL (SOCKS5 or HTTP). For example: http://127.0.0.1:8080 or socks5://127.0.0.1:8080

GENERAL OPTIONS:
  -V                  Show version information. (default: false)
  -ac                 Automatically calibrate filtering options (default: false)
  -acc                Custom auto-calibration string. Can be used multiple times. Implies -ac
  -c                  Colorize output. (default: false)
  -config             Load configuration from a file
  -maxtime            Maximum running time in seconds for entire process. (default: 0)
  -maxtime-job        Maximum running time in seconds per job. (default: 0)
  -p                  Seconds of `delay` between requests, or a range of random delay. For example "0.1" or "0.1-2.0"
  -rate               Rate of requests per second (default: 0)
  -s                  Do not print additional information (silent mode) (default: false)
  -sa                 Stop on all error cases. Implies -sf and -se. (default: false)
  -se                 Stop on spurious errors (default: false)
  -sf                 Stop when > 95% of responses return 403 Forbidden (default: false)
  -t                  Number of concurrent threads. (default: 40)
  -v                  Verbose output, printing full URL and redirect location (if any) with the results. (default: false)

MATCHER OPTIONS:
  -mc                 Match HTTP status codes, or "all" for everything. (default: 200,204,301,302,307,401,403,405)
  -ml                 Match amount of lines in response
  -mr                 Match regexp
  -ms                 Match HTTP response size
  -mw                 Match amount of words in response

FILTER OPTIONS:
  -fc                 Filter HTTP status codes from response. Comma separated list of codes and ranges
  -fl                 Filter by amount of lines in response. Comma separated list of line counts and ranges
  -fr                 Filter regexp
  -fs                 Filter HTTP response size. Comma separated list of sizes and ranges
  -fw                 Filter by amount of words in response. Comma separated list of word counts and ranges

INPUT OPTIONS:
  -D                  DirSearch wordlist compatibility mode. Used in conjunction with -e flag. (default: false)
  -e                  Comma separated list of extensions. Extends FUZZ keyword.
  -ic                 Ignore wordlist comments (default: false)
  -input-cmd          Command producing the input. --input-num is required when using this input method. Overrides -w.
  -input-num          Number of inputs to test. Used in conjunction with --input-cmd. (default: 100)
  -input-shell        Shell to be used for running command
  -mode               Multi-wordlist operation mode. Available modes: clusterbomb, pitchfork (default: clusterbomb)
  -request            File containing the raw http request
  -request-proto      Protocol to use along with raw request (default: https)
  -w                  Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist:KEYWORD'

OUTPUT OPTIONS:
  -debug-log          Write all of the internal logging to the specified file.
  -o                  Write output to file
  -od                 Directory path to store matched results to.
  -of                 Output file format. Available formats: json, ejson, html, md, csv, ecsv (or, 'all' for all formats) (default: json)
  -or                 Don't create the output file if we don't have results (default: false)

```
Разверните машину.

Как минимум, нам необходимо предоставить два варианта: -uуказать URL и -wуказать список слов. Ключевое слово по 
умолчанию FUZZиспользуется для указания ffuf, куда будут введены записи списка слов. Мы можем добавить его в конец 
URL следующим образом:  

Команда для Q1

`ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt`

Вы также можете использовать любое пользовательское ключевое слово вместо FUZZ, вам просто нужно определить его 
следующим образом wordlist.txt:KEYWORD . 

`ffuf -u http://MACHINE_IP/NORAJ -w /usr/share/wordlists/SecLists/Discovery/Web-Content/big.txt:NORAJ`

Примечание: путь к списку слов может различаться в зависимости от того, где вы их сохранили.

### Ответьте на вопросы ниже
Какой файл с кодом статуса 200 вы нашли первым?
```commandline
favicon.ico
```

## Задание 3
Один из подходов, который вы могли бы использовать, — начать перечисление с общего списка файлов, например, 
raft-medium-files-lowercase.txt. 

Команда для Q1
`ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt`

Однако использование большого общего списка слов, содержащего нерелевантные расширения файлов, не очень эффективно.

Вместо этого мы обычно можем предположить index.<extension>, что это страница по умолчанию на большинстве веб-сайтов,
поэтому мы можем попробовать общие расширения только для страницы индекса. С помощью этого метода мы обычно можем 
определить, какой язык или языки программирования использует сайт.

Например, мы можем добавить расширение после индекса.
```commandline
head /usr/share/seclists/Discovery/Web-Content/web-extensions.txt                                                            
.asp
.aspx
.bat
.c
.cfm
.cgi
.css
.com
.dll
.exe
```

Команда для Q2
`ffuf -u http://MACHINE_IP/indexFUZZ -w /usr/share/seclists/Discovery/Web-Content/web-extensions.txt`

Теперь, когда мы знаем поддерживаемые расширения, мы можем попробовать список общих слов (без расширения) и 
применить расширения, которые, как мы знаем, работают (найденные из Q2), а также некоторые распространенные, такие как .txt. 

Мы исключим из этого списка словарей расширения из 4 букв, поскольку они приведут к большому количеству ложных срабатываний.

Команда для Q3
`ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt -e .php,.txt`

Имена каталогов не всегда зависят от типа среды, которую вы перечисляете, и часто являются хорошей отправной точкой 
перед попыткой фаззинга файлов. Если мы хотим фаззинга каталогов, нам нужно только предоставить список слов. 

Команда на Q4

`ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt`
### Ответьте на вопросы ниже
Какой текстовый файл вы нашли?
```commandline
robots.txt
```
Какие два расширения файлов были обнаружены для страницы индекса?
```commandline
php,phps
```
Какая страница имеет размер 4840?
```commandline
about.php
```
Сколько существует каталогов?
```commandline
4
```

## Задание 4
Помните команду, которую мы выполнили для Q1 задачи 3?
```commandline

$ ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.3.1-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.130.176/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

favicon.ico             [Status: 200, Size: 1406, Words: 5, Lines: 2]
.htaccess               [Status: 403, Size: 289, Words: 21, Lines: 11]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1]
robots.txt              [Status: 200, Size: 26, Words: 3, Lines: 2]
phpinfo.php             [Status: 302, Size: 0, Words: 1, Lines: 1]
.                       [Status: 302, Size: 0, Words: 1, Lines: 1]
php.ini                 [Status: 200, Size: 148, Words: 17, Lines: 5]
about.php               [Status: 200, Size: 4840, Words: 331, Lines: 109]
.html                   [Status: 403, Size: 285, Words: 21, Lines: 11]
login.php               [Status: 200, Size: 1523, Words: 89, Lines: 77]
.php                    [Status: 403, Size: 284, Words: 21, Lines: 11]
setup.php               [Status: 200, Size: 4067, Words: 308, Lines: 123]
.htpasswd               [Status: 403, Size: 289, Words: 21, Lines: 11]
security.php            [Status: 302, Size: 0, Words: 1, Lines: 1]
.htm                    [Status: 403, Size: 284, Words: 21, Lines: 11]
.htpasswds              [Status: 403, Size: 290, Words: 21, Lines: 11]
index.php               [Status: 302, Size: 0, Words: 1, Lines: 1]
.htgroup                [Status: 403, Size: 288, Words: 21, Lines: 11]
wp-forum.phps           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htaccess.bak           [Status: 403, Size: 293, Words: 21, Lines: 11]
.htuser                 [Status: 403, Size: 287, Words: 21, Lines: 11]
.ht                     [Status: 403, Size: 283, Words: 21, Lines: 11]
.htc                    [Status: 403, Size: 284, Words: 21, Lines: 11]
:: Progress: [16243/16243] :: Job [1/1] :: 1690 req/sec :: Duration: [0:00:13] :: Errors: 0 ::
```

У нас было много выходных данных, но мало что было полезным.
Например, код статуса HTTP 403 указывает на то, что нам запрещен доступ к запрошенному ресурсу. Давайте пока скроем 
ответы с кодами статуса 403. Мы можем сделать это с помощью фильтров. 

Добавив -fc 403(код фильтра), мы скроем из вывода все коды статуса HTTP 403.

Команда для Q1
`
ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -fc 403
`

Иногда вам может потребоваться отфильтровать несколько кодов статуса, таких как 500, 302, 301, 401 и т. д. Например, 
если вы знаете, что хотите увидеть 200 ответов с кодами статуса, вы можете использовать -mc 200(код соответствия) 
вместо длинного списка отфильтрованных кодов.  

Команда для Q2
`ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -mc 200`

Иногда может быть полезно посмотреть, какие запросы сервер не обрабатывает, сопоставив коды ответов HTTP-mc 500 500 
Internal Server Error ( ). Обнаружение нарушений в поведении может помочь лучше понять, как работает веб-приложение. 

Существуют и другие фильтры и сопоставители. Например, вы можете столкнуться с записями с кодом статуса 200 с 
размером ответа, равным нулю. например, functions.phpили inc/myfile.php. 
```commandline
$ ffuf -u http://MACHINE_IP/config/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -fc 403
...
.                       [Status: 200, Size: 1165, Words: 76, Lines: 18]
config.inc.php          [Status: 200, Size: 0, Words: 1, Lines: 1]
:: Progress: [16243/16243] :: Job [1/1] :: 1732 req/sec :: Duration: [0:00:13] :: Errors: 0 ::

```

Если у нас нет LFI (локального включения файлов), такие файлы не представляют интереса, поэтому мы можем использовать -fs 0(размер фильтра).

Вот все фильтры и сопоставители:
```commandline
$ ffuf -h
...
MATCHER OPTIONS:
  -mc                 Match HTTP status codes, or "all" for everything. (default: 200,204,301,302,307,401,403,405)
  -ml                 Match amount of lines in response
  -mr                 Match regexp
  -ms                 Match HTTP response size
  -mw                 Match amount of words in response

FILTER OPTIONS:
  -fc                 Filter HTTP status codes from response. Comma separated list of codes and ranges
  -fl                 Filter by amount of lines in response. Comma separated list of line counts and ranges
  -fr                 Filter regexp
  -fs                 Filter HTTP response size. Comma separated list of sizes and ranges
  -fw                 Filter by amount of words in response. Comma separated list of word counts and ranges
...

```

Мы часто видим ложные срабатывания с файлами, начинающимися с точки (например, .htgroups, .phpи т. д.). Они выдают ошибку 403 Forbidden, однако эти файлы на самом деле не существуют. Это заманчиво, -fc 403но это может скрыть ценные файлы, к которым у нас пока нет доступа. Поэтому вместо этого мы можем использовать регулярное выражение для сопоставления всех файлов, начинающихся с точки.
Команда для Q3

`ffuf -u http://MACHINE_IP/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -fr '/\..*'`
### Ответьте на вопросы ниже
Сколько результатов было возвращено после применения фильтра fc?
```commandline
11
```
Сколько результатов было возвращено после применения фильтра mc?
```commandline
6
```
Какой ценный файл был бы скрыт, если бы вы использовали -fc 403вместо-fr?

```commandline
wp-forum.phps
```

## Задание 5
Разверните новую машину.

Для этой задачи мы рассмотрим фаззинг параметров. Это базовый URL, который мы будем фаззингить: http://MACHINE_IP/sqli-labs/Less-1/.

Что бы вы сделали, если бы нашли страницу или конечную точку API, но не знаете, какие параметры принимаются? Вы путаете!

Обнаружение уязвимого параметра может привести к включению файла, раскрытию пути, XSS , SQL- инъекции или даже инъекции команды. Поскольку ffuf позволяет вам поместить ключевое слово в любое место, мы можем использовать его для поиска параметров.

Команда для Q1
```commandline
$ ffuf -u 'http://MACHINE_IP/sqli-labs/Less-1/?FUZZ=1' -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -fw 39
$ ffuf -u 'http://MACHINE_IP/sqli-labs/Less-1/?FUZZ=1' -c -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt -fw 39
```

Теперь, когда мы нашли параметр, принимающий целочисленные значения, мы начнем фаззинг значений.

На этом этапе мы могли бы сгенерировать список слов и сохранить файл, содержащий целые числа. Чтобы вырезать шаг, мы 
можем использовать команду -w - ffuf, которая сообщает ffuf о необходимости считать список слов из stdout .  Это 
позволит нам сгенерировать список целых чисел с помощью команды по нашему выбору, а затем передать вывод в ffuf. 
Ниже приведен список из 5 различных способов генерации чисел от 0 до 255.

Команды для Q2
```
$ ruby -e '(0..255).each{|i| puts i}' | ffuf -u 'http://MACHINE_IP/sqli-labs/Less-1/?id=FUZZ' -c -w - -fw 33
$ ruby -e 'puts (0..255).to_a' | ffuf -u 'http://MACHINE_IP/sqli-labs/Less-1/?id=FUZZ' -c -w - -fw 33
$ for i in {0..255}; do echo $i; done | ffuf -u 'http://MACHINE_IP/sqli-labs/Less-1/?id=FUZZ' -c -w - -fw 33
$ seq 0 255 | ffuf -u 'http://MACHINE_IP/sqli-labs/Less-1/?id=FUZZ' -c -w - -fw 33
$ cook '[0-255]' | ffuf -u 'http://MACHINE_IP/sqli-labs/Less-1/?id=FUZZ' -c -w - -fw 33
```

Мы также можем использовать ffuf для атак методом перебора по словарному списку, например, для подбора паролей на 
странице аутентификации. 

Команда для Q3

`$ ffuf -u http://MACHINE_IP/sqli-labs/Less-11/ -c -w /usr/share/seclists/Passwords/Leaked-Databases/hak5.txt -X POST -d 'uname=Dummy&passwd=FUZZ&submit=Submit' -fs 1435 -H 'Content-Type: application/x-www-form-urlencoded'
`
Здесь нам нужно использовать метод POST (указанный с помощью -X) и предоставить данные POST (с помощью -d), где мы 
включаем FUZZключевое слово вместо пароля. 

Нам также необходимо указать пользовательский заголовок, поскольку ffuf не устанавливает этот заголовок типа 
содержимого автоматически, как это делает curl.-H 'Content-Type: application/x-www-form-urlencoded' 

### Ответьте на вопросы ниже
Какой параметр вы нашли?
```commandline
id
```
Какой самый высокий допустимый идентификатор?
```commandline
14
```
Какой пароль у Дамми?
```commandline
p@ssword
```
## Задание 6
ffuf может быть не столь эффективен, как специализированные инструменты, когда дело касается перечисления поддоменов, но это возможно.

```commandline
$ ffuf -u http://FUZZ.mydomain.com -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt

```
Некоторые поддомены могут не разрешаться DNS-сервером, который вы используете, и разрешаться только из локальной сети цели их частными DNS-серверами. Поэтому некоторые виртуальные хосты (vhosts) могут существовать с частными поддоменами, поэтому предыдущая команда их не находит. Чтобы попытаться найти частные поддомены, нам придется использовать заголовок HTTP Host , так как эти запросы могут быть приняты веб-сервером.
Примечание : виртуальные хосты (vhosts) — это название, используемое Apache httpd, но для Nginx правильным термином будет Server Blocks .

Вы можете сравнить результаты, полученные с помощью прямого перечисления поддоменов и перечисления vhost:
```commandline
$ ffuf -u http://FUZZ.mydomain.com -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -fs 0
$ ffuf -u http://mydomain.com -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H 'Host: FUZZ.mydomain.com' -fs 0

```

Например, возможно, что вы не сможете найти поддомен с помощью прямого перечисления поддоменов (первая команда), но 
сможете найти его с помощью перечисления vhost (вторая команда). 

Не следует сбрасывать со счетов метод перечисления виртуальных хостов, поскольку он может привести к обнаружению 
контента, к которому не предназначался внешний доступ. 
### Ответьте на вопросы ниже
Я прочитал материал задания
```commandline
Ответ не нужен
```

## Задание 7
Будь то для сетевого поворота или для использования плагинов BurpSuite, вы можете направлять весь трафик ffuf через веб-прокси ( HTTP или SOCKS5).

```commandline
$ ffuf -u http://MACHINE_IP/FUZZ -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -x http://127.0.0.1:8080
```

Также можно отправлять на прокси-сервер только матчи для повторного воспроизведения:
```commandline
$ ffuf -u http://MACHINE_IP/FUZZ -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -replay-proxy http://127.0.0.1:8080
```

Это может быть полезно, если вам не нужно, чтобы весь трафик проходил через прокси-сервер верхнего уровня, и вы хотите минимизировать использование ресурсов или не засорять историю прокси-серверов.

### Ответьте на вопросы ниже
Я понимаю, как заставить трафик идти через прокси.
```commandline
Ответ не нужен
```

## Задание 8
Когда вы начнете больше использовать ffuf, некоторые опции окажутся очень полезными в зависимости от вашей ситуации. Например, -icпозволяет игнорировать комментарии в списках слов, таких как заголовки, примечания об авторских правах, комментарии и т. д.

$ head /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt                                                            
# directory-list-2.3-medium.txt
#
# Copyright 2007 James Fisher
#
# This work is licensed under the Creative Commons
# Attribution-Share Alike 3.0 License. To view a copy of this
# license, visit http://creativecommons.org/licenses/by-sa/3.0/
# or send a letter to Creative Commons, 171 Second Street,
# Suite 300, San Francisco, California, 94105, USA.
#

$ ffuf -u http://MACHINE_IP/FUZZ -c -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -ic -fs 0

Мы рассмотрели только небольшое подмножество полезных функций и опций, которые ffuf может предложить для фаззинга.
Используйте ffuf -h, чтобы узнать о других опциях, которые могут быть вам полезны, и ответить на оставшиеся вопросы в этой задаче.

### Ответьте на вопросы ниже
Как сохранить вывод в файл markdown (ffuf.md)?
```commandline
-of md -o ffuf.md
```
Как повторно использовать необработанный файл http-запроса?
```commandline
-request
```
Как удалить комментарии из списка слов?
```commandline
-ic
```
Как бы вы прочитали список слов из STDIN?
```commandline
-w -
```
Как распечатать полные URL-адреса и места перенаправления?
```commandline
-v
```
Какой вариант вы бы использовали для отслеживания перенаправлений?
```commandline
-r
```
Как включить цветной вывод?
```commandline
-c
```

## Задание 9
Надеюсь, вам понравилась комната.
Чтобы узнать больше обо мне ( noraj ), посетите pwn.by/noraj .
Вы можете найти мои другие комнаты THM в моем профиле THM .

ПопробуйтеHackMe
### Ответьте на вопросы ниже
Спасибо
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)