[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Network Services 2](https://tryhackme.com/r/room/networkservices2) 

Всего 11 заданий:
## Задание 1
Привет и добро пожаловать!

Эта комната является продолжением первой комнаты сетевых служб. Аналогично, она рассмотрит несколько более 
распространенных уязвимостей и неправильных конфигураций сетевых служб, которые вы, вероятно, найдете в CTF, а также 
некоторые сценарии тестов на проникновение.

Я бы рекомендовал вам завершить первую комнату сетевых служб ( https://tryhackme.com/room/networkservices ), прежде 
чем приступать к этой. 

Как и в предыдущей комнате, определенно стоит иметь базовые знания Linux, прежде чем пробовать эту комнату. Если вы 
считаете, что вам понадобится помощь, попробуйте пройти модуль 'Linux Fundamentals' ( https://tryhackme.com/module/linux-fundamentals ) 

Прежде чем мы начнем:

Подключитесь к серверу TryHackMe OpenVPN (для получения помощи см. https://tryhackme.com/access !)
Устройтесь поудобнее и выпейте чашку чая, кофе или воды рядом!
Давайте начнем!
NB Это не комната о взломе или перехвате доступа к WiFi, а скорее о том, как получить несанкционированный доступ к 
машине, эксплуатируя сетевые службы. Если вас интересует взлом WiFi, я предлагаю ознакомиться с WiFi Hacking 101 от 
NinjaJc01 ( https://tryhackme.com/room/wifihacking101 )  

### Ответить на вопросы ниже
Готовы? Поехали!

```commandline
Ответ не нужен
```

## Задание 2
### Что такое НФС?

NFS означает «сетевая файловая система» и позволяет системе делиться каталогами и файлами с другими через сеть. 
Используя NFS, пользователи и программы могут получать доступ к файлам на удаленных системах почти так же, как если 
бы они были локальными файлами. Это происходит путем монтирования всей файловой системы или ее части на сервере. К 
смонтированной части файловой системы могут получить доступ клиенты с любыми привилегиями, назначенными каждому файлу.

### Как работает NFS? Общий файл

Нам не нужно слишком подробно разбираться в техническом обмене, чтобы эффективно использовать NFS, однако, если вас 
это интересует, я бы порекомендовал этот ресурс: https://docs.oracle.com/cd/E19683-01/816-4882/6mb2ipq7l/index.html 

Сначала клиент запросит монтирование каталога с удаленного хоста в локальный каталог точно так же, как он может 
монтировать физическое устройство. Затем служба монтирования будет действовать для подключения к соответствующему 
демону монтирования с помощью RPC.  

Сервер проверяет, есть ли у пользователя разрешение на монтирование любого запрошенного каталога. Затем он 
возвращает дескриптор файла, который уникально идентифицирует каждый файл и каталог, находящиеся на сервере. 

Если кто-то хочет получить доступ к файлу с помощью NFS, RPC-вызов помещается в NFSD (демон NFS) на сервере. Этот 
вызов принимает такие параметры, как: 

 - Дескриптор файла
 - Имя файла, к которому необходимо получить доступ
 - Идентификатор пользователя
 - Идентификатор группы пользователя
Они используются для определения прав доступа к указанному файлу. Это то, что контролирует разрешения пользователя, 
   чтение и запись файлов в IE. 

### Что управляет NFS?

Используя протокол NFS, вы можете передавать файлы между компьютерами под управлением Windows и других операционных 
систем, отличных от Windows, таких как Linux, MacOS или UNIX. 

Компьютер под управлением Windows Server может выступать в качестве файлового сервера NFS для других клиентских 
компьютеров, отличных от Windows. Аналогично, NFS позволяет компьютеру под управлением Windows Server получать 
доступ к файлам, хранящимся на сервере NFS, отличном от Windows.  

### Больше информации:

Вот несколько ресурсов, которые объясняют техническую реализацию и работу NFS более подробно, чем я описал здесь.

https://www.datto.com/library/what-is-nfs-file-share

http://nfs.sourceforge.net/

https://wiki.archlinux.org/index.php/NFS

### Ответить на вопросы ниже
Что означает NFS?
```commandline
Network File System
```
Какой процесс позволяет клиенту NFS взаимодействовать с удаленным каталогом, как если бы это было физическое устройство?

```commandline
Mounting
```
Что использует NFS для представления файлов и каталогов на сервере?
```commandline
file handle
```
Какой протокол использует NFS для связи между сервером и клиентом?
```commandline
RPC
```
Какие два фрагмента пользовательских данных сервер NFS принимает в качестве параметров для управления разрешениями 
пользователя? Формат: параметр 1 / параметр 2 
```commandline
user id / group id
```
Может ли сервер Windows NFS обмениваться файлами с клиентом Linux? (Да/Нет)
```commandline
Y
```
Может ли сервер Linux NFS обмениваться файлами с клиентом MacOS? (Да/Нет)
```commandline
Y
```
Какая версия NFS является последней? [выпущена в 2016 году, но по состоянию на 2020 год все еще актуальна] Для этого 
потребуется внешнее исследование. 
```commandline
4.2
```

## Задание 3
Давайте начнем

Прежде чем начать, обязательно разверните комнату и дайте ей время на загрузку. Имейте в виду — это может занять до пяти минут, так что будьте терпеливы!

Что такое перечисление?

Перечисление определяется как «процесс, который устанавливает активное соединение с целевыми хостами для обнаружения потенциальных векторов атак в системе, и то же самое может быть использовано для дальнейшей эксплуатации системы». - Infosec Institute . Это критический этап при рассмотрении того, как перечислить и эксплуатировать удаленную машину, поскольку информация, которую вы будете использовать для информирования ваших атак, будет поступать с этого этапа

Требования

Для того, чтобы сделать более продвинутый перечисление  сервера NFS и общих ресурсов, нам понадобится несколько инструментов. Первый  из которых является ключевым для взаимодействия с любым общим ресурсом NFS с вашей локальной  машины: nfs-common .

NFS-Common

Важно  установить этот пакет на любой машине, использующей NFS, как  клиент, так и  сервер. Он включает в себя такие программы, как:  lockd , statd , showmount , nfsstat,  gssd ,  idmapd и mount.nfs . В первую очередь нас интересуют "showmount" и  "mount.nfs", поскольку они будут наиболее полезны для нас, когда дело дойдет до  извлечения информации из общего ресурса NFS. Если вам нужна дополнительная  информация об этом пакете, не стесняйтесь читать: https://packages.ubuntu.com/jammy/nfs-common .

Установить nfs-common можно с помощью « sudo apt install nfs-common », он входит в стандартные репозитории большинства дистрибутивов Linux , таких как Kali Remote Machine или AttackBox, которые предоставляются TryHackMe.

Сканирование портов

Сканирование портов уже много раз рассматривалось, поэтому я расскажу только об основах, которые вам понадобятся для этой комнаты. Если вы хотите узнать больше о nmap более подробно, пожалуйста, посмотрите комнату nmap .

Первый шаг перечисления — провести сканирование портов, чтобы узнать как можно больше информации о службах, открытых портах и ​​операционной системе целевой машины. Вы можете углубиться в это настолько, насколько захотите, однако я предлагаю использовать nmap с тегами -A и -p- .

Монтаж общих ресурсов NFS

Вашей клиентской системе нужен каталог, в котором можно получить доступ ко всему контенту, предоставленному хост-сервером в папке экспорта. Вы можете создать
эту папку в любом месте вашей системы. После создания этой точки монтирования вы можете использовать команду "mount" для подключения общего ресурса NFS к точке монтирования на вашей машине следующим образом:

sudo mount -t nfs IP:share /tmp/mount/ -nolock

Давайте разберемся

Ярлык	Функция
судо	Запуск от имени пользователя root
устанавливать	Выполните команду монтирования
-т нфс	Тип устройства для монтирования, затем указание, что это NFS
IP:поделиться	IP-адрес NFS-сервера и имя общего ресурса, который мы хотим смонтировать.
-nolock	Указывает, что не следует использовать блокировку NLM.


Теперь, когда мы разобрались с нашими инструментами, давайте начнем!

### Ответить на вопросы ниже
Проведите тщательное сканирование портов по вашему выбору. Сколько портов открыто?


```commandline
7
```
Какой порт содержит службу, которую мы хотим перечислить?

```commandline
2049
```
Теперь используйте /usr/sbin/showmount -e [IP], чтобы вывести список общих ресурсов NFS. Каково имя видимого общего ресурса?


```commandline
/home
```
Пришло время подключить общий ресурс к нашему локальному компьютеру!

Сначала используйте " mkdir /tmp/mount ", чтобы создать каталог на вашем компьютере для монтирования общего ресурса. 
Он находится в каталоге /tmp, поэтому имейте в виду, что он будет удален при перезапуске. 

Затем используйте команду mount, которую мы разобрали ранее, чтобы смонтировать ресурс NFS на локальной машине. 
Измените каталог на тот, куда вы смонтировали ресурс — как называется папка внутри? 


```commandline
cappucino
```
Посмотрите в этот каталог, посмотрите на файлы. Похоже, мы в домашнем каталоге пользователя...
```commandline
Ответ не нужен
```
Интересно! Давайте проведем небольшое исследование, посмотрим папки. Какие из этих папок могут содержать ключи , 
которые дадут нам удаленный доступ к серверу? 


```commandline
.ssh
```
Какой из этих ключей наиболее полезен для нас?


```commandline
id_rsa
```
Скопируйте этот файл в другое место на локальном компьютере и измените права доступа на «600» с помощью «chmod 600 
[файл]». 
Если мы правильно определили тип этого каталога, то мы можем довольно легко определить имя пользователя, которому 
соответствует этот ключ. 
Можем ли мы войти в машину с помощью ssh -i <key-file> <username>@<ip> ? (Да/Нет)

```commandline
Y
```

## Задание 4
### Мы закончили, да?

Не совсем так. Если у вас оболочка с низкими привилегиями на какой-либо машине и вы обнаружили, что на машине есть 
общий ресурс NFS, вы можете использовать его для повышения привилегий, в зависимости от того, как он настроен.

### Что такое root_squash?

По умолчанию на общих ресурсах NFS включено сжатие корней, которое не позволяет любому, кто подключается к общему 
ресурсу NFS, получить доступ root к тому NFS. Удаленным пользователям root при подключении назначается пользователь 
«nfsnobody», который имеет наименьшие локальные привилегии. Это не то, что нам нужно. Однако, если отключить этот 
параметр, он может разрешить создание файлов битов SUID, что позволит удаленному пользователю получить доступ root к 
подключенной системе.

### SUID
Итак, что такое файлы с установленным битом SUID? По сути, это означает, что файл или файлы могут быть запущены с 
разрешениями владельца/группы файла(ов). В данном случае, как суперпользователь. Мы можем использовать это, чтобы 
получить оболочку с этими привилегиями!  

### Метод

Это звучит сложно, но на самом деле — если вы знакомы с тем, как работают файлы SUID, это довольно легко понять. Мы 
можем загружать файлы на общий ресурс NFS и контролировать разрешения этих файлов. Мы можем устанавливать разрешения 
для всего, что мы загружаем, в данном случае исполняемого файла оболочки bash. Затем мы можем войти через SSH, как 
мы делали в предыдущей задаче — и запустить этот исполняемый файл, чтобы получить root shell!

### Исполняемый файл

Из соображений совместимости   мы получим исполняемый файл bash непосредственно с целевой машины.
С ключом, полученным в предыдущей задаче, мы можем использовать SCP с командой  scp -i key_name 
username@MACHINE_IP:/bin/bash ~/Downloads/bash для его загрузки на нашу атакующую машину.

Другой способ преодоления проблем совместимости — получить стандартный исполняемый файл bash Ubuntu Server 18.04, 
такой же, как у сервера, как мы знаем из нашего сканирования nmap. Вы можете загрузить его здесь. Если вы хотите 
загрузить его через командную строку, будьте осторожны, чтобы не загрузить страницу github вместо необработанного 
скрипта. Вы можете использовать wget https://github.com/polo-sec/writing/raw/master/Security%20Challenge%20Walkthroughs/Networks%202/bash. Обратите внимание, что этот метод требует подключения к Интернету, поэтому вы не сможете загрузить его при использовании бесплатного AttackBox.   

### Намеченный путь:

Если вам все еще сложно это понять, вот пошаговое описание действий, которые мы предпринимаем, и то, как все они 
связаны между собой, чтобы позволить нам получить root-оболочку: 


    NFS-доступ ->

        Получить оболочку с низкими привилегиями ->

            Загрузите исполняемый файл Bash на общий ресурс NFS ->

                Установка разрешений SUID через NFS из-за неправильно настроенного Root Squash ->

                    Войти через SSH ->

                        Выполнить исполняемый файл Bash SUID Bit ->

                            КОРНЕВОЙ ДОСТУП

Давай сделаем это!

### Ответить на вопросы ниже
Сначала измените каталог на точку монтирования на вашем компьютере, где все еще должен быть смонтирован общий ресурс 
NFS, а затем на домашний каталог пользователя. 
```commandline
Ответ не нужен
```
Загрузите исполняемый файл bash в каталог Downloads. Затем используйте "cp ~/Downloads/bash .", чтобы скопировать 
исполняемый файл bash в общий ресурс NFS. Скопированная оболочка bash должна принадлежать пользователю root, это 
можно сделать с помощью "sudo chown root bash"  
```commandline
Ответ не нужен
```
Теперь мы добавим разрешение бита SUID к исполняемому файлу bash, который мы только что скопировали в общий ресурс, 
используя "sudo chmod +[permission] bash". Какую букву мы используем, чтобы установить бит SUID с помощью chmod? 
```commandline
s
```
Давайте проверим работоспособность, проверим права доступа к исполняемому файлу "bash" с помощью "ls -la bash". Как 
выглядит набор прав доступа? Убедитесь, что он заканчивается на -sr-x. 
```commandline
-rwsr-sr-x
```
Теперь подключитесь по SSH к машине как пользователь. Перечислите каталог, чтобы убедиться, что исполняемый файл 
bash там есть. Теперь момент истины. Давайте запустим его с помощью " ./bash -p ". -p сохраняет разрешения, так что 
он может работать как root с SUID-, так как в противном случае bash иногда будет сбрасывать разрешения.  
```commandline
Ответ не нужен
```
Отлично! Если все прошло хорошо, у вас должна быть оболочка от имени root! Какой флаг root?
```commandline
THM{nfs_got_pwned}
```

## Задание 5
### Что такое SMTP ?

SMTP означает "Simple Mail Transfer Protocol". Он используется для обработки отправки электронных писем. Для 
поддержки служб электронной почты требуется пара протоколов, состоящая из SMTP и POP/ IMAP. Вместе они позволяют 
пользователю отправлять исходящую почту и получать входящую почту соответственно.  

SMTP - сервер выполняет три основные функции:

- Он проверяет, кто отправляет электронные письма через SMTP -сервер.
- Он отправляет исходящую почту
- Если исходящая почта не может быть доставлена, сообщение отправляется обратно отправителю.


Большинство людей сталкивались с SMTP при настройке нового адреса электронной почты в некоторых сторонних почтовых 
  клиентах, таких как Thunderbird; поскольку при настройке нового почтового клиента вам потребуется настроить 
  конфигурацию SMTP- сервера для отправки исходящих писем.  
### POP и IMAP

POP, или «Post Office Protocol», и IMAP, «Internet Message Access Protocol», — это протоколы электронной почты, 
которые отвечают за передачу электронной почты между клиентом и почтовым сервером. Основное различие заключается в 
более упрощенном подходе POP к загрузке входящих сообщений с почтового сервера на клиент. В то время как IMAP 
синхронизирует текущий почтовый ящик с новой почтой на сервере, загружая все новое. Это означает, что изменения в 
почтовом ящике, внесенные на одном компьютере через IMAP, сохранятся, если вы затем синхронизируете входящие 
сообщения с другого компьютера. Сервер POP/ IMAP отвечает за выполнение этого процесса.

### Как работает SMTP ?

Функция доставки электронной почты во многом схожа с функцией доставки физической почты. Пользователь предоставляет 
электронную почту (письмо) и услугу (почтовую службу доставки), а затем, пройдя ряд шагов, доставит ее в почтовый 
ящик получателя. Роль SMTP-сервера в этой услуге заключается в том, чтобы действовать как сортировочный офис, 
электронная почта (письмо) собирается и отправляется на этот сервер, который затем направляет ее получателю.   
Мы можем отобразить путь электронного письма от вашего компьютера до получателя следующим образом:



1. Почтовый агент пользователя, который является либо вашим почтовым клиентом, либо внешней программой, подключается 
   к SMTP- серверу вашего домена, например, smtp.google.com. Это инициирует SMTP- рукопожатие. Это подключение 
   работает через порт SMTP , который обычно равен 25. После того, как эти подключения установлены и проверены, 
   начинается сеанс SMTP .   

2. Теперь можно начинать процесс отправки почты. Клиент сначала отправляет серверу адрес отправителя и получателя, а 
   также текст письма и все вложения. 

3. Затем SMTP -сервер проверяет, совпадают ли доменные имена получателя и отправителя.

4. SMTP-сервер отправителя установит соединение с SMTP-сервером получателя перед ретрансляцией письма. Если сервер 
   получателя недоступен или недоступен, письмо помещается в очередь SMTP . 

5. Затем SMTP -сервер получателя проверит входящее письмо. Он делает это, проверяя, распознаны ли домен и имя 
   пользователя. Затем сервер пересылает письмо на сервер POP или IMAP , как показано на схеме выше. 

6. Электронное письмо появится в папке «Входящие» получателя.

Это очень упрощенная версия процесса, и есть много подпротоколов, коммуникаций и деталей, которые не были включены. 
Если вы хотите узнать больше об этой теме, это действительно удобная для чтения разбивка более тонких технических 
деталей - я фактически использовал ее, чтобы написать эту разбивку:  

https://computer.howstuffworks.com/e-mail-messaging/email3.htm

Что запускает SMTP ?

Программное обеспечение SMTP-сервера доступно на серверных платформах Windows, а многие другие варианты SMTP 
доступны для работы на Linux. 

Больше информации:

Вот ресурс, который объясняет техническую реализацию и работу SMTP более подробно, чем я описал здесь.

https://www.afternerd.com/blog/smtp/

### Ответить на вопросы ниже
Simple Mail Transfer Protocol
```commandline
Что означает SMTP?
```
Что обрабатывает SMTP-отправку? (ответ во множественном числе)
```commandline
emails
```
Каков первый шаг в процессе SMTP?
```commandline
SMTP handshake
```
Какой порт SMTP по умолчанию?
```commandline
25
```
Куда SMTP-сервер отправляет электронное письмо, если сервер получателя недоступен?
```commandline
smtp queue
```
На каком сервере в конечном итоге оказывается электронное письмо?
```commandline
POP/IMAP
```
Может ли машина с Linux запустить SMTP-сервер? (Да/Нет)
```commandline
Y
```
Может ли машина с Windows запустить SMTP-сервер? (Да/Нет)
```commandline
Y
```
## Задание 6
#### Давайте начнем

Прежде чем начать, обязательно разверните комнату и дайте ей время на загрузку. Имейте в виду, что это может занять 
до пяти минут, так что будьте терпеливы! 

#### Перечисление данных сервера

Плохо настроенные или уязвимые почтовые серверы часто могут стать начальной точкой входа в сеть, но перед началом 
атаки мы хотим получить отпечаток сервера, чтобы сделать наше нацеливание максимально точным. Для этого мы 
воспользуемся модулем " smtp_version " в MetaSploit. Как следует из его названия, он будет сканировать диапазон 
IP-адресов и определять версию любых почтовых серверов, с которыми столкнется.

#### Перечисление пользователей из SMTP

Служба SMTP имеет две внутренние команды, которые позволяют производить перечисление пользователей: VRFY 
(подтверждение имен действительных пользователей) и EXPN (которая раскрывает фактический адрес псевдонимов 
пользователя и списки электронной почты (списки рассылки). Используя эти команды SMTP, мы можем раскрыть список 
действительных пользователей

Мы можем сделать это вручную, через telnet-соединение, однако Metasploit снова приходит на помощь, предоставляя 
удобный модуль с соответствующим названием "smtp_enum", который сделает всю работу за нас! Использование модуля 
заключается в простом указании ему хоста или диапазона хостов для сканирования и списка слов, содержащего имена 
пользователей для перечисления.

#### Требования
Поскольку мы собираемся использовать Metasploit для этого, важно, чтобы у вас был установлен Metasploit. Он 
установлен по умолчанию как в Kali Linux, так и в Parrot OS; однако, всегда стоит сделать быстрое обновление, чтобы 
убедиться, что у вас установлена последняя версия, прежде чем запускать какие-либо атаки. Вы можете сделать это с 
помощью простого "sudo apt update" и сопутствующего обновления, если таковые требуются.

#### Альтернативы
Стоит отметить, что этот метод перечисления будет работать для большинства конфигураций SMTP; однако есть и другие, 
не metasploit-инструменты, такие как smtp-user-enum, которые работают еще лучше для перечисления учетных записей 
пользователей на уровне ОС в Solaris через службу SMTP. Перечисление выполняется путем проверки ответов на команды 
VRFY, EXPN и RCPT TO.   

Эту технику можно было бы адаптировать в будущем для работы против других уязвимых демонов SMTP, но на момент 
написания статьи этого сделано не было. Это альтернатива, которую стоит иметь в виду, если вы пытаетесь 
дистанцироваться от использования Metasploit, например, при подготовке к OSCP.

Итак, мы рассмотрели теорию. Давайте начнем!

### Ответить на вопросы ниже
Сначала давайте запустим сканирование портов на целевой машине, как и в прошлый раз. На каком порту работает SMTP?
```commandline
25
```
Хорошо, теперь мы знаем, какой порт нам нужен, давайте запустим Metasploit. Какую команду мы используем для этого?

Если вам нужна дополнительная помощь или практика использования Metasploit, у TryHackMe есть модуль по Metasploit, с 
которым вы можете ознакомиться здесь: https://tryhackme.com/module/metasploit
```commandline
msfconsole
```
Давайте найдем модуль « smtp_version», каково его полное имя?
```commandline
auxiliary/scanner/smtp/smtp_version
```
Отлично, теперь — выберите модуль и перечислите опции. Как это сделать?
```commandline
options
```
Посмотрите на параметры, все ли правильно? Какой параметр нам нужно установить?
```commandline
RHOSTS
```
Установите правильное значение для вашей целевой машины. Затем запустите эксплойт. Какое имя системной почты?
```commandline
polosmtp.home
```
Какой почтовый агент (MTA) управляет сервером SMTP? Для этого потребуется внешнее исследование.
```commandline
Postfix
```
Хорошо! Теперь у нас есть достаточно информации о целевой системе, чтобы перейти к следующему этапу. Давайте найдем 
модуль " smtp_enum ", каково его полное имя? 
```commandline
auxiliary/scanner/smtp/smtp_enum
```
Мы будем использовать список слов «top-usernames-shortlist.txt» из подраздела «Имена пользователей» раздела seclists 
(/usr/share/wordlists/SecLists/Usernames, если он у вас установлен). 

Seclists — это потрясающая коллекция списков слов. Если вы используете Kali или Parrot, вы можете установить 
seclists с помощью: "sudo apt install seclists" В качестве альтернативы вы можете загрузить репозиторий  отсюда . 

Какую опцию нам нужно задать для пути к списку слов?
```commandline
USER_FILE
```
После того, как мы установили эту опцию, какой еще важный параметр нам нужно установить?
```commandline
RHOSTS
```
Теперь запустите эксплойт, это может занять несколько минут, так что возьмите чашку чая, кофе, воды. Пейте 
достаточно жидкости! 
```commandline
Ответ не нужен
```
Хорошо! Теперь, когда все готово, какое имя пользователя возвращается?
```commandline
administrator
```
## Задание 7
#### Что мы знаем?
Итак, в конце раздела «Перечисление» у нас есть несколько важных фрагментов информации:
1. Имя учетной записи пользователя
2. Тип SMTP- сервера и работающей операционной системы.

Из сканирования портов мы знаем, что единственный другой открытый порт на этой машине — это вход SSH. Мы собираемся 
использовать эту информацию, чтобы попытаться подобрать пароль входа SSH для нашего пользователя с помощью Hydra. 

#### Подготовка

Желательно выйти из Metasploit, чтобы продолжить эксплуатацию этой части комнаты. Во-вторых, полезно сохранить 
информацию, собранную вами на этапе перечисления, чтобы помочь в эксплуатации.

#### Гидра

Существует широкий спектр возможностей настройки при использовании Hydra, и он позволяет проводить адаптивные атаки 
паролей против множества различных служб, включая SSH. Hydra поставляется по умолчанию как в Parrot, так и в Kali, 
однако, если вам это нужно, вы можете найти GitHub здесь.

Hydra в первую очередь использует атаки по словарю, и Kali Linux, и Parrot OS имеют много разных списков слов в 
каталоге " /usr/share/wordlists " - если вы хотите просмотреть и найти другие списки слов, помимо широко 
используемого "rockyou.txt". Аналогично я рекомендую проверить SecLists для более широкого спектра других списков 
слов, которые чрезвычайно полезны для самых разных целей, помимо простого взлома паролей. Например, перечисление 
поддоменов
Синтаксис команды, которую мы будем использовать для поиска паролей, следующий:
```commandline
"hydra -t 16 -l ИМЯ_ПОЛЬЗОВАТЕЛЯ -P /usr/share/wordlists/rockyou.txt -vV IP_МАШИНЫ ssh"
```
Давайте разберемся:

>РАЗДЕЛ	ФУНКЦИЯ
гидра	Запускает инструмент hydra
-t 16 Количество параллельных соединений на цель
-l [пользователь]	Указывает на пользователя, аккаунт которого вы пытаетесь взломать.
-P [путь к словарю]	Указывает на файл, содержащий список возможных паролей.
-vV Устанавливает очень подробный режим, показывает комбинацию логин+пароль для каждой попытки
[IP-адрес машины]	IP-адрес целевой машины
ssh / протокол	Устанавливает протокол


Похоже, мы готовы к рок -н-роллу!
### Ответить на вопросы ниже
Какой пароль у пользователя, которого мы нашли на этапе перечисления?
```commandline
alejandro
```
Отлично! Теперь давайте подключимся к серверу по SSH как пользователь. Каково содержимое smtp.txt?
```commandline
THM{who_knew_email_servers_were_c00l?}
```
## Задание 8
### Что такое MySQL?
В самом простом определении MySQL — это система управления реляционными базами данных (СУБД), основанная на языке 
структурированных запросов (SQL). Слишком много сокращений? Давайте разберемся: 

#### База данных:
База данных — это просто постоянная, организованная коллекция структурированных данных.

#### СУРБД:
Программное обеспечение или сервис, используемый для создания и управления базами данных на основе реляционной 
модели. Слово «реляционный» просто означает, что данные, хранящиеся в наборе данных, организованы в виде таблиц. 
Каждая таблица каким-то образом связана с «первичным ключом» друг друга или другими «ключевыми» факторами.  

#### SQL-запрос :
MYSQL — это просто торговая марка одной из самых популярных реализаций программного обеспечения RDBMS. Как мы знаем, 
она использует модель клиент-сервер. Но как клиент и сервер взаимодействуют? Они используют язык, а именно язык 
структурированных запросов ( SQL ).  

Многие другие продукты, такие как PostgreSQL и Microsoft SQL server, содержат слово SQL . Это также означает, что 
это продукт, использующий синтаксис Structured Query Language. 

#### Как работает MySQL?
MySQL как СУРБД состоит из сервера и служебных программ, которые помогают в администрировании баз данных MySQL.

Сервер обрабатывает все инструкции базы данных, такие как создание, редактирование и доступ к данным. Он принимает и 
управляет этими запросами и взаимодействует с использованием протокола MySQL. Весь этот процесс можно разбить на 
следующие этапы:  

- MySQL создает базу данных для хранения и обработки данных, определяя взаимосвязь каждой таблицы.
- Клиенты делают запросы, используя определенные операторы на языке SQL.
- Сервер ответит клиенту, предоставив всю запрошенную информацию.

#### Что управляет MySQL?
MySQL может работать на различных платформах, будь то Linux или Windows. Он обычно используется в качестве 
внутренней базы данных для многих известных веб-сайтов и является важным компонентом стека LAMP, который включает: 
Linux, Apache, MySQL и PHP.  

### Больше информации:
Вот несколько ресурсов, которые объясняют техническую реализацию и работу MySQL более подробно, чем я описал здесь:

https://dev.mysql.com/doc/dev/mysql-server/latest/PAGE_SQL_EXECUTION.html 

https://www.w3schools.com/php/php_mysql_intro.asp

### Ответить на вопросы ниже
К какому типу программного обеспечения относится MySQL?
```commandline
relational database management system
```
На каком языке основан MySQL?
```commandline
SQL
```
Какую модель связи использует MySQL?
```commandline
client-server
```
Каково наиболее распространённое применение MySQL?
```commandline
back end database
```
Какая крупная социальная сеть использует MySQL в качестве своей внутренней базы данных? Это потребует дальнейшего исследования.
```commandline
Facebook
```
## Задание 9
### Давайте начнем

Прежде чем начать, обязательно разверните комнату и дайте ей время на загрузку. Пожалуйста, учтите, это может занять 
до пяти минут, так что будьте терпеливы! 

#### Когда вы начнете атаковать MySQL
MySQL, скорее всего, не будет первой точкой вызова при получении первоначальной информации о сервере. Вы можете, как 
мы делали в предыдущих задачах, попытаться подобрать пароли учетных записей по умолчанию, если у вас действительно 
нет никакой другой информации; однако в большинстве сценариев CTF это вряд ли будет тем путем, которым вы должны 
следовать.   

#### Сценарий

Обычно вы получаете некоторые начальные учетные данные от перечисления других служб, которые затем можно 
использовать для перечисления и эксплуатации службы MySQL. Поскольку эта комната посвящена эксплуатации и 
перечислению сетевой службы, ради сценария мы предположим, что вы нашли учетные данные : "root:password" при 
перечислении поддоменов веб-сервера. После неудачной попытки входа через SSH вы решаете попробовать его через MySQL.

#### Требования

Вам понадобится установить MySQL на вашей системе для подключения к удаленному серверу MySQL. Если он еще не 
установлен, вы можете установить его с помощью sudo apt install default-mysql-client. Не волнуйтесь — это не 
установит серверный пакет на вашу систему — только клиент.

Опять же, для этого мы будем использовать Metasploit; важно, чтобы у вас был установлен Metasploit, так как он 
установлен по умолчанию как в Kali Linux, так и в Parrot OS. 

#### Альтернативы

Как и в предыдущем задании, стоит отметить, что все, что мы будем делать с помощью Metasploit, можно сделать вручную 
или с помощью набора не-Metasploit-инструментов, таких как скрипт mysql-enum от nmap: https://nmap.org/nsedoc/scripts/mysql-enum.html или https://www.exploit-db.com/exploits/23081 . Я рекомендую вам после завершения 
этой комнаты вернуться и попробовать сделать все вручную, чтобы убедиться, что вы понимаете процесс, который 
используется для отображения полученной вами информации.    

#### Ладно, хватит разговоров. Поехали!

### Ответить на вопросы ниже
Как всегда, начнем со сканирования портов, чтобы знать, на каком порту работает служба, которую мы пытаемся 
атаковать. Какой порт использует MySQL? 

```commandline
3306
```
Хорошо, теперь мы думаем, что у нас есть набор учетных данных. Давайте дважды проверим это, вручную подключившись к 
серверу MySQL. Мы можем сделать это с помощью команды " mysql -h [IP] -u [username] -p " 
```commandline
Ответ не нужен
```
Хорошо, мы знаем, что наши учетные данные работают. Давайте выйдем из этой сессии с помощью "exit" и запустим Metasploit.
```commandline
Ответ не нужен
```
Мы будем использовать модуль «mysql_sql».
Найдите, выберите и перечислите необходимые параметры. Какие три параметра нам нужно установить? (в порядке убывания).


```commandline
PASSWORD/RHOSTS/USERNAME
```
Запустите эксплойт. По умолчанию он будет тестировать с помощью команды "select version()", какой результат это вам 
даст? 

```commandline
5.7.29-0ubuntu0.18.04.1
```
Отлично! Мы знаем, что наш эксплойт приземляется, как и планировалось. Давайте попробуем получить более амбициозную 
информацию. Измените опцию "sql" на "показать базы данных". Сколько баз данных возвращается?


```commandline
4
```
## Задание 10
Что мы знаем?

Давайте проведем проверку на благонадежность, прежде чем попытаться полностью использовать базу данных и получить 
более конфиденциальную информацию, чем просто имена баз данных. Мы знаем: 
1. Учетные данные сервера MySQL
2. Версия MySQL, работающая
3. Количество баз данных и их названия.

#### Ключевая терминология

Чтобы понять, какие эксплойты мы будем использовать дальше, нам нужно понять несколько ключевых терминов.

#### Схема:
В MySQL физически схема является синонимом базы данных. Вы можете заменить ключевое слово "SCHEMA" вместо DATABASE 
в синтаксисе MySQL SQL, например, используя CREATE SCHEMA вместо CREATE DATABASE. Важно понимать эту связь, 
поскольку некоторые другие продукты баз данных проводят различие. Например, в продукте Oracle Database схема 
представляет только часть базы данных: таблицы и другие объекты, принадлежащие одному пользователю.

#### Хэши:
Проще говоря, хэши — это продукт криптографического алгоритма, преобразующего входные данные переменной длины в 
выходные данные фиксированной длины.

В MySQL хэши могут использоваться по-разному, например, для индексации данных в хэш-таблице. Каждый хэш имеет 
уникальный идентификатор, который служит указателем на исходные данные. Это создает индекс, который значительно 
меньше исходных данных, что позволяет более эффективно искать и получать доступ к значениям

Однако данные, которые мы собираемся извлечь, представляют собой хэши паролей, которые представляют собой просто 
способ хранения паролей не в текстовом формате. 

Давайте начнем.

### Ответить на вопросы ниже
Сначала давайте найдем и выберем модуль "mysql_schemadump". Каково полное имя модуля?
```commandline
auxiliary/scanner/mysql/mysql_schemadump
```
Отлично! Теперь, вы уже делали это несколько раз, так что я позволю вам действовать дальше. Установите 
соответствующие параметры, запустите эксплойт. Как называется последняя таблица, которая выгружается? 
```commandline
x$waits_global_by_latency
```
Отлично, теперь вы выгрузили таблицы и имена столбцов всей базы данных. Но мы можем сделать лучше... найдите и 
выберите модуль "mysql_hashdump". Каково полное имя модуля? 
```commandline
auxiliary/scanner/mysql/mysql_hashdump
```
Опять же, я позволю вам взять это отсюда. Установите соответствующие параметры, запустите эксплойт. Какой 
нестандартный пользователь выделяется для вас? 
```commandline
carl
```
Другой пользователь! И у нас есть его хэш пароля. Это может быть очень интересно. Скопируйте строку хэша полностью, 
например: bob:*HASH в текстовый файл на локальной машине под названием "hash.txt". 

Что такое строка комбинации пользователя и хэша?
```commandline
carl:*EA031893AA21444B170FC2162A56978B8CEECE18
```
Теперь нам нужно взломать пароль! Давайте попробуем Джона Потрошителя против него, используя: " john hash.txt " 
Какой пароль у пользователя, которого мы нашли? 
```commandline
doggie
```
Потрясающе. Повторное использование пароля не только крайне опасно, но и крайне распространено. Каковы шансы, что 
этот пользователь повторно использовал свой пароль для другого сервиса? 

Каково содержимое MySQL.txt?
```commandline
THM{congratulations_you_got_the_mySQL_flag}
```
## Задание 11
Чтение

Вот несколько вещей, которые может быть полезно прочитать после завершения этой комнаты, если это вас заинтересует:

 https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/security_guide/ch-exploits
 https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/
Спасибо

Спасибо, что уделили время изучению этой темы, желаю вам удачи в будущем.

~ Поло
### Ответить на вопросы ниже
Поздравляю! Вы сделали это!
```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)