[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Vulnversity](https://tryhackme.com/r/room/vulnversity) 

Всего 5 заданий:
## Задание 1
Подключитесь к нашей сети и разверните эту машину. Если вам нужна помощь в подключении, сначала пройдите комнату OpenVPN.

### Ответить на вопросы ниже
Разверните машину.
```commandline
Ответ не нужен
```

## Задание 2
Соберите информацию об этой машине, используя сетевой сканирующий инструмент под названием Nmap. Посетите комнату 
Nmap для получения дополнительной информации! 

Подключение к машине
В этой комнате рекомендуется использовать AttackBox, который можно запустить, нажав синюю кнопку в правом верхнем углу.
Сканировать коробку
nmap -sV КОМПЬЮТЕР_IP.


Nmap — это бесплатный, открытый и мощный инструмент, используемый для обнаружения хостов и служб в компьютерной сети.
В нашем примере мы используем Nmap для сканирования этой машины, чтобы определить все службы, работающие на 
определенном порту. Nmap имеет много возможностей; в таблице ниже приведены некоторые из его функций.  



### Ответить на вопросы ниже
В сети есть множество «шпаргалок» по Nmap, которые вы также можете использовать.
```commandline
Ответ не нужен
```
Просканируйте коробку: сколько портов открыто?
```commandline
6
```
Какая версия прокси-сервера Squid запущена на компьютере?
```commandline
3.5.12
```
Сколько портов будет сканировать Nmap, если был использован флаг -p-400 ?
```commandline
400
```
Какая операционная система, скорее всего, установлена на этом компьютере?
```commandline
Ubuntu
```
На каком порту работает веб-сервер?
```commandline
3333
```
Важно убедиться, что вы всегда проводите тщательную разведку, прежде чем двигаться дальше. Знание всех открытых 
служб (которые могут быть точками эксплуатации) очень важно, не забывайте, что порты на более высоком диапазоне 
могут быть открыты, поэтому постоянно сканируйте порты после 1000 (даже если вы оставляете проверку в фоновом режиме).  
```commandline
Ответ не нужен
```
Какой флаг используется для включения подробного режима с помощью Nmap?
```commandline
-v
```

## Задание 3
Используя быстрый инструмент обнаружения каталогов, называемый Gobuster, вы найдете каталог, в который можно загрузить оболочку.

Давайте сначала просканируем веб-сайт на предмет скрытых каталогов. Для этого мы воспользуемся Gobuster .

хакер начинает

Gobuster — это инструмент для подбора URI (каталогов и файлов), поддоменов DNS и имен виртуальных хостов. Для этой 
машины мы сосредоточимся на его использовании для подбора каталогов. 

Загрузите Gobuster  здесь , или, если у вас Kali Linux, запустите sudo apt-get install gobuster.

Для начала вам понадобится список слов для Gobuster (который будет использоваться для быстрого просмотра списка слов 
с целью определения доступности публичного каталога. Если вы используете  Kali Linux , вы можете найти множество 
списков слов в разделе /usr/share/wordlists. Вы также можете использовать список слов для каталогов, расположенных 
по адресу /usr/share/wordlists/dirbuster/directory-list-1.0.txt в AttackBox.   

Теперь давайте запустим Gobuster со списком слов, используя `gobuster dir -u http://MACHINE_IP:3333 -w` .
### Ответить на вопросы ниже
Я успешно настроил Gobuster. 
```commandline
Ответ не нужен
```
В каком каталоге есть страница формы загрузки?


```commandline
/internal/
```

## Задание 4
Теперь, когда вы нашли форму для загрузки файлов, мы можем использовать ее для загрузки и выполнения нашей полезной 
нагрузки, что приведет к компрометации веб-сервера.  Мы проведем фаззинг формы загрузки, чтобы определить, какие 
расширения не заблокированы.  

Для этого мы будем использовать BurpSuite. Если вам нужно разъяснение того, что такое BurpSuite или как его 
настроить, пожалуйста, сначала заполните наш  модуль BurpSuite. 

Использование BurpSuite

Мы будем использовать Intruder (используется для автоматизации индивидуальных атак).  Для начала создайте список 
слов со следующими расширениями: 

.php
.php3
.php4
.php5
.phtml
 

Теперь убедитесь, что BurpSuite настроен на перехват всего трафика вашего браузера. Загрузите файл; как только этот 
запрос будет перехвачен, отправьте его злоумышленнику. Нажмите на " Payloads" и выберите Sniperтип атаки " ". 

Нажмите на вкладку " Positions", найдите имя файла и " Add §" для расширения. Это должно выглядеть так:

позиция полезной нагрузки burpsuite

Теперь, когда мы знаем, какое расширение можно использовать для нашей полезной нагрузки, мы можем двигаться дальше.

Получение обратного Shell

Мы собираемся использовать PHP обратный шелл в качестве нашей полезной нагрузки. Обратный шелл работает, вызываясь 
на удаленном хосте и заставляя этот хост установить соединение с вами. Таким образом, вы будете прослушивать 
входящие соединения, загружать и выполнять свой шелл, который будет сигнализировать вам для управления! Вы можете 
загрузить следующий обратный PHP шелл здесь.   

Чтобы получить удаленный доступ к этому компьютеру, выполните следующие действия:

- Отредактируйте файл php-reverse-shell.php и измените IP-адрес на ваш IP-адрес tun0 (его можно получить, перейдя по 
адресу  http://10.10.10.10  в браузере вашего подключенного к TryHackMe устройства). 
- Переименуйте этот файл в php-reverse-shell.phtml.
- Теперь мы будем прослушивать входящие соединения с помощью netcat. Выполните следующую команду: nc -lvnp 1234.
- Загрузите оболочку и перейдите по адресу  http://MACHINE_IP:3333/internal/uploads/php-reverse-shell.phtml - Это 
  запустит вашу полезную нагрузку.
- Вы должны увидеть соединение в сеансе Netcat.

доступ к оболочке

Ответьте на следующие вопросы, основываясь на приведенном выше упражнении.

### Ответить на вопросы ниже
Какой распространенный тип файла вы хотели бы загрузить, чтобы эксплуатировать заблокированный сервер? Попробуйте 
несколько, чтобы узнать. 
```commandline
.php
```
Я понимаю инструмент Burpsuite и его назначение во время пентеста.
```commandline
Ответ не нужен
```
Какое расширение допускается после выполнения вышеуказанного упражнения?
```commandline
.phtml
```
Выполняя вышеуказанное упражнение, я успешно загрузил обратную оболочку PHP.
```commandline
Ответ не нужен
```
Каково имя пользователя, который управляет веб-сервером?
```commandline
bill
```
Что такое флаг пользователя?
```commandline
8bd7992fbe8a6ad22a63361004cfcedb
```

## Задание 5
Теперь, когда вы взломали эту машину, мы повысим свои привилегии и станем суперпользователем (root).

В Linux SUID (set owner userId upon execution) — это особый тип разрешения на доступ к файлу. SUID предоставляет 
пользователю временные разрешения на запуск программы/файла с разрешения владельца файла (а не пользователя, который 
его запускает).  

Например, двоичный файл для изменения пароля имеет установленный бит SUID (/usr/bin/passwd). Это связано с тем, что 
для изменения пароля вам нужно будет записать файл shadowers, к которому у вас нет доступа; но root есть, поэтому у 
него есть привилегии root для внесения правильных изменений.  

Пришло время испытаний! Мы провели вас до этого места. Раскройте свои навыки и используйте эту систему дальше, чтобы 
повысить свои привилегии и ответить на следующие вопросы. 

### Ответить на вопросы ниже
В системе выполните поиск всех файлов SUID. Какой файл выделяется?

```commandline
/bin/systemctl
```
Каково значение корневого флага?

```commandline
a58ff8579f0a9270368d33a9966c7fd5
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)