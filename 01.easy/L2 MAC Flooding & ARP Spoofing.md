

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [L2 MAC Flooding & ARP Spoofing](https://tryhackme.com/r/room/layer2) 

Всего 9 заданий:
## Задание 1
Хотя это и не обязательно, в идеале вы должны иметь общее представление о работе сетевых коммутаторов OSI Model 
Layer 2 (L2) , что такое таблица MAC- адресов, что делает протокол разрешения адресов ( ARP ) и как использовать 
Wireshark на базовом уровне.  Если вы не знакомы с этими темами, пожалуйста, ознакомьтесь с модулями Network and 
Linux Fundamentals и комнатой Wireshark.

Теперь, когда мы рассмотрели все необходимые условия, запустите машину и начнем!

Пожалуйста, подождите не менее 5 минут, чтобы машины полностью запустили и запустили службы, прежде чем подключаться 
по SSH. 

### Ответьте на вопросы ниже
Я понимаю и запустил машину, нажав кнопку «Запустить машину».
```commandline
Ответ не нужен
```

## Задание 2
Ради этой комнаты давайте предположим следующее:

Проводя пентест, вы получили начальный доступ к сети и повысили привилегии до root на машине Linux. Во время рутинного перечисления ОС вы понимаете, что это хост с двойным подключением , то есть он подключен к двум (или более) сетям. Будучи любопытным хакером, вы решили исследовать эту сеть, чтобы посмотреть, сможете ли вы двигаться вбок.

После установления устойчивости вы можете получить доступ к скомпрометированному хосту через SSH :

Пожалуйста, подождите не менее 5 минут , чтобы машина полностью запустила и запустила службы, затем попробуйте подключиться по SSH (если вы вошли в систему, а командная строка еще не отображается, не нажимайте Ctrl+C! Просто будьте терпеливы…):
`ssh -o StrictHostKeyChecking=accept-new admin@MACHINE_IP`

Примечание:  Пользователь admin  находится в группе sudo . Я предлагаю использовать  пользователя root для 
завершения этой комнаты :sudo su - 

### Ответьте на вопросы ниже
Теперь, вы можете (снова) получить доступ? (Ура/Нет)

```commandline
Yay
```

## Задание 3
Как упоминалось ранее, хост подключен к одной или нескольким дополнительным сетям.  В настоящее время вы подключены к машине через SSH на адаптере Ethernet eth0 .  Интересующая вас сеть подключена к адаптеру Ethernet eth1 .

Сначала взгляните на адаптер:

ip address show eth1или сокращенная версия: ip a s eth1

Используя эти знания, ответьте на вопросы №1 и №2 .

Теперь используйте инструмент для подсчета сетевых адресов по вашему выбору, например,  ping , скрипт bash или python или Nmap (предустановлен), чтобы обнаружить другие хосты в сети и ответить на вопрос № 3 .

### Ответьте на вопросы ниже
Какой у вас IP-адрес?
```commandline
192.168.12.66
```
Какой префикс CIDR у сети?
```commandline
/24
```
Сколько еще живых ведущих?
```commandline
2
```
Каково имя первого хоста (с наименьшим IP-адресом), который вы нашли?
```commandline
alice
```

## Задание 4
Простое сканирование этих хостов не поможет нам собрать какую-либо полезную информацию, и вы можете спросить,  что может сделать пентестер в этой ситуации? В зависимости от правил взаимодействия  и области действия , вы можете попробовать прослушивать трафик в этой сети.

На схеме ниже описана ваша текущая ситуация, в которой вы являетесь Атакующим и имеете постоянный доступ к Еве.



Давайте попробуем запустить tcpdump на сетевом интерфейсе eth1 :

`tcpdump -i eth1`

При желании можно получить более подробный вывод, который выводит каждый пакет (за исключением заголовка уровня канала) в формате ASCII:

`tcpdump -A -i eth1`

Попробуйте ответить на вопросы №1–2 .

Теперь давайте более подробно рассмотрим захваченные пакеты!  Мы можем перенаправить их в файл pcap , указав файл назначения через аргумент -w :


`tcpdump -A -i eth1 -w /tmp/tcpdump.pcap`

Захватывайте трафик в течение минуты, затем перенесите  pcap-файл  либо на свой компьютер, либо в AttackBox, чтобы 
открыть его в Wireshark.

Пример передачи захваченного пакета с помощью scp и открытия его в Wireshark:
```commandline
scp admin@MACHINE_IP:/tmp/tcpdump.pcap .
wireshark tcpdump.pcap
```


Теперь вы должны быть в состоянии ответить на вопросы №3 и №4.

Примечание: Если вы получили сообщение об ошибке «`tcpdump: /tmp/tcpdump.pcap`: Отказано в доступе» и не можете 
перезаписать существующий файл `/tmp/tcpdump.pcap` , укажите новое имя файла, например tcpdump 2 .pcap , или запустите 
`rm -f /tmp/*.pcap` и повторно запустите tcpdump.

### Ответьте на вопросы ниже
Видите ли вы трафик с этих хостов? (Ура/Нет)
```commandline
Yay
```
Кто продолжает отправлять пакеты Еве?
```commandline
Bob
```
Какие типы пакетов отправляются?
```commandline
ICMP
```
Каков размер их раздела данных? (байты)
```commandline
666
```

## Задание 5
К сожалению, нам пока не удалось захватить какой-либо интересный трафик. Однако мы не собираемся сдаваться так 
просто! Итак, как нам захватить больше сетевого трафика?  Как упоминалось в описании комнаты, мы могли бы попытаться 
запустить атаку MAC-флуда против коммутатора L2.  

Будьте осторожны: MAC-флуд может вызвать тревогу в SOC . Нет, серьезно, подозрительный трафик уровня 2 может быть 
легко обнаружен и сообщен современными и правильно настроенными сетевыми устройствами. Хуже того, ваш сетевой порт 
может быть вообще заблокирован сетевым устройством, что сделает вашу машину заблокированной в сети. В случае, если 
на этом сетевом подключении запущены производственные службы или производственный трафик направляется через это 
сетевое соединение, это может даже привести к эффективному отказу в обслуживании !     

Однако, если нам это удастся, коммутатор перейдет в режим аварийного открытия и временно будет работать аналогично 
сетевому концентратору — пересылая все полученные кадры на каждый подключенный порт (кроме порта, с которого пришел 
трафик). Это позволит злоумышленнику или пентестеру прослушивать сетевой трафик между другими хостами, который 
обычно не был бы получен их устройством, если бы коммутатор работал правильно.   

Рассматривать такой вектор атаки рекомендуется только в том случае, если у вас есть основания полагать, что...

Это на самом деле коммутируемая сеть (а не виртуальный мост) И
Коммутатор может быть потребительским или полупотребительским (неуправляемым) коммутатором ИЛИ администраторы сети не настроили меры по смягчению последствий, например, динамическую проверку  ARP (DAI) И
Атаки спуфинга ARP и MAC явно разрешены в  правилах взаимодействия . Если у вас есть сомнения, сначала проясните ситуацию с вашим клиентом!
В любом случае, предположим, что вы приняли обдуманное решение попробовать.

Для большего удобства откройте второй сеанс SSH. Таким образом, вы можете оставить процесс tcpdump запущенным на переднем плане в первом сеансе SSH :

`tcpdump -A -i eth1 -w /tmp/tcpdump2.pcap`

Теперь, во втором сеансе SSH, пристегнитесь и позвольте macof запуститься на интерфейсе, чтобы начать заполнение 
коммутатора: 

`macof -i eth1`

Примерно через 30 секунд остановите macof и tcpdump (Ctrl+C).

Как и в предыдущем задании, перенесите pcap на свою машину ( kali/AttackBox) и посмотрите:
```commandline
scp admin@MACHINE_IP:/tmp/tcpdump2.pcap .
wireshark tcpdump2.pcap
```

Теперь вы должны быть в состоянии ответить на вопросы №1 и №2 .

Примечание: Если это не сработало, попробуйте снова захватить на 30 секунд (во время работы macof
). Если это все еще не сработает, сделайте последнюю попытку с длительностью захвата в одну минуту.
В качестве крайней меры попробуйте использовать ettercap (представлен в следующих задачах) с плагином rand_flood :

`ettercap -T -i eth1 -P rand_flood -q -w /tmp/tcpdump3.pcap` (Выйти с помощью q )

### Ответьте на вопросы ниже
Какие пакеты Алиса постоянно отправляет Бобу? 
```commandline
ICMP
```
Каков размер их раздела данных? (байты)
```commandline
1337
```

## Задание 6
Как вы могли заметить, MAC Flooding можно считать действительно «шумной» техникой. Чтобы снизить риск обнаружения и DoS , мы пока оставим macof в стороне. Вместо этого мы собираемся выполнить так называемые атаки отравления кэша ARP против Алисы и Боба, в попытке стать полноценным Man-in-the-Middle ( MITM ).

Для более глубокого понимания этой техники прочитайте статью в Википедии об ARP- спуфинге .

tl;dr – «злоумышленник отправляет (поддельные) ARP-сообщения […], чтобы связать MAC-адрес злоумышленника с 
IP-адресом другого хоста […], в результате чего любой трафик, предназначенный для этого IP-адреса, отправляется 
злоумышленнику. ARP -спуфинг может позволить злоумышленнику перехватывать кадры данных в сети, изменять трафик или 
останавливать весь трафик. Часто атака используется как возможность для других атак, таких как отказ в обслуживании, 
атака типа « человек посередине » или атака с перехватом сеанса».  -  Википедия - ARP - спуфинг     


https://commons.wikimedia.org/wiki/File:ARP_Spfing.svg

Однако существуют меры и средства контроля, позволяющие обнаружить и предотвратить такие атаки. В текущем сценарии оба хоста используют реализацию ARP, которая прилагает все усилия для проверки входящих ответов ARP. Без лишних слов, мы используем ettercap для запуска атаки ARP Spoofing против Алисы и Боба и посмотрим, как они отреагируют:

`ettercap -T -i eth1 -M arp`

### Ответьте на вопросы ниже
Может ли ettercap установить MITM между Алисой и Бобом? (Да/Нет)
```commandline
Nay
```
Ожидали бы вы другого результата при атаке на хосты без включенной проверки пакетов ARP? (Да/Нет)
```commandline
Yay
```

## Задание 7
В этом несколько измененном сценарии Алиса и Боб используют другую ОС (Ubuntu) с ее реализацией ARP по умолчанию и без защитных элементов управления на своих машинах. Как и в предыдущей задаче, попробуйте установить MITM с помощью ettercap  и посмотрите, не станет ли Ubuntu (по умолчанию) его жертвой .

После запуска виртуальной машины , подключенной к этой задаче, вы можете войти в систему через SSH , используя те же учетные данные, что и раньше:

Имя пользователя: admin
Пароль: Layer2

Как и в случае с предыдущей машиной, пожалуйста, подождите не менее 5 минут , пока этот блок раскрутится, затем попробуйте подключиться по SSH (если вы вошли в систему, а командная строка еще не отображается, не нажимайте Ctrl+C! Просто будьте терпеливы…)

### Ответьте на вопросы ниже
Просканируйте сеть на eth1. Кто там? Введите их IP-адреса в порядке возрастания.
```commandline
192.168.12.10, 192.168.12.20
```
На каком компьютере имеется открытый известный порт?
```commandline
192.168.12.20
```
Какой номер порта?
```commandline
80
```
Можете ли вы получить доступ к контенту сервиса с вашего текущего местоположения? (Нет/Да)
```commandline
Nay
```
Видите ли вы какой-либо значимый трафик, идущий к этому порту или с него, пассивно прослушивающий ваш интерфейс eth1? (Нет/Ура)
```commandline
Nay
```
Теперь запустите ту же атаку ARP-спуфинга, что и в предыдущей задаче. Видите ли вы какой-нибудь интересный трафик? (Нет/Ура)
```commandline
Yay
```
Кто пользуется этой услугой?
```commandline
alice
```
На какой хост отправляются запросы?
```commandline
www.server.bob
```
Какой файл запрашивается?
```commandline
test.txt
```
Какой текст содержится в файле?
```commandline
OK
```
Какие учетные данные используются для аутентификации? (имя пользователя:пароль)
```commandline
admin:s3cr3t_P4zz
```
Теперь остановите атаку (нажав q). Что делает ettercap, чтобы изящно покинуть позицию посредника и отменить отравление?
```commandline
RE-ARPing the victims
```
Можете ли вы получить доступ к контенту, стоящему за этой услугой, сейчас, используя полученные учетные данные? (Нет/Ура)
```commandline
Yay
```
Что такое флаг user.txt?
```commandline
THM{wh0s_$n!ff1ng_0ur_cr3ds}
```
Вы также должны были увидеть довольно сомнительный вид трафика. Какой тип удаленного доступа (shell) есть у Алисы на сервере?
```commandline
reverse shell
```
Какие команды выполняются? Отвечайте в том порядке, в котором они выполняются.
```commandline
whoami, pwd, ls
```
Какой из перечисленных файлов вам нужен?
```commandline
root.txt
```
## Задание 8
Как пентестер, ваш первый подход — попытаться взломать веб-сервер Боба. Для целей этой комнаты предположим, что это невозможно. Кроме того, захват учетных данных базовой аутентификации не поможет от повторного использования пароля или подобных атак.

Итак, давайте превратим нашу текущую атаку отравления ARP в полноценный MITM, включающий манипуляцию пакетами! Поскольку пакеты Алисы проходят через вашу атакующую машину ( eve ), мы можем вмешиваться в них.

Как мы можем это сделать? Ettercap поставляется с -Fопцией, которая позволяет вам применять фильтры в виде указанных файлов etterfilter.ef для сеанса. Однако эти файлы .ef должны быть сначала скомпилированы из исходных файлов фильтров etterfilter ( .ecf ). Синтаксис их исходного кода похож на код C.  Чтобы сделать эту задачу более удобной для новичков, мы предполагаем, что не будет иметь значения, обнаружит ли Алиса наши манипулятивные действия. Ради этой комнаты мы собираемся только манипулировать ее командами и не будем принимать никаких мер предосторожности OPSEC .

Какая из ее храбрых команд должна добровольно принять участие в нашем дерзком начинании? Как насчет... да, whoami, конечно!  

Прежде чем копировать и вставлять фильтр ниже, лучше понять команду etterfilter и синтаксис ее исходного файла. Проконсультируйтесь со страницей man, запустив  man etterfilter или просмотрев страницу linux.die.net/man/8/etterfilter .

Теперь создайте новый файл кода etterfilter с именем whoami.ecf и попробуйте написать фильтр, соответствующий исходному порту и транспортному протоколу Алисы, а также заменить данные whoami на обратную полезную нагрузку оболочки по вашему выбору. Чтобы увидеть решение, щелкните стрелку раскрывающегося списка:

Показать возможное решение (спойлер!)

Примечание: Кавычки необходимо экранировать . Так что, если вы хотите, чтобы ваш фильтр заменил, например , whoamiна echo -e "whoami\nroot", то кавычки вокруг whoami\nrootнужно экранировать следующим образом:replace("whoami", "echo -e \"whoami\nroot\" " )
Чтобы увидеть решение для обратной оболочки полезной нагрузки, щелкните стрелку раскрывающегося списка:

Показать возможное решение (спойлер!)

Наконец, нам нужно скомпилировать .ecf в  файл .ef :

`etterfilter whoami.ecf -o whoami.ef`

Не забудьте запустить свой слушатель (фоновый режим). Для верхнего примера выше вы можете использовать:

`nc -nvlp 6666 &`

Не так быстро! Если что, нам все равно нужно разрешить входящее соединение через брандмауэр. Отключите ufw или создайте соответствующее разрешающее правило; в противном случае обратный шелл Боба будет заблокирован брандмауэром:

ufw allow in on eth1 from 192.168.12.20 to 192.168.12.66 port 6666 proto tcpили полностью отключить брандмауэр, запустив ufw disable

Теперь запустите ettercap , указав только что созданный файл etterfilter :

`ettercap -T -i eth1 -M arp -F whoami.ef`

Через несколько секунд после выполнения этой команды вы должны увидеть сообщение "###### ETTERFILTER: …" и/или "Connection received on 192.168.12.20 …"   в выводе Netcat, что означает, что вы только что поймали обратный шелл от Боба! Теперь вы можете выйти из ettercap (с помощью q ), перевести на передний план своего слушателя Netcat (с помощью fg ) и наслаждаться своей оболочкой!

Примечание: чтобы ограничить попытки ettercap отравить ARP-пакеты вашими фактическими целями и отображать только трафик между ними, вы можете указать их как целевые группы 1 и 2, используя аннотацию токена "///" после опции -M arp :

`ettercap -T -i eth1 -M arp /192.168.12.10// /192.168.12.20// -F whoami.ef`

Подсказка: если обратная оболочка не работает, попробуйте заменить whoami на подходящую команду cat , чтобы получить флаг.
### Ответьте на вопросы ниже
Что такое флаг root.txt?
```commandline
THM{wh4t_an_ev1l_M!tM_u_R}
```

## Задание 9
Надеюсь, эта комната открыла вам новые перспективы в области сетевого пентестинга и дала вам новый уровень  атак для 
вашего инструментария, а также, надеюсь, вы получили удовольствие от этого процесса! 

Это также должно было вдохновить сообщество на создание большего количества контента и учебных ресурсов L2, поэтому 
не стесняйтесь взглянуть на «бэкэнд» виртуализации L2 Eve ( GNS3 ): 
http://MACHINE_IP:3080

Пожалуйста, не стесняйтесь оставлять мне любые отзывы или вопросы по внедрению блоков GNS3 и следите за новостями о 
новых событиях L2!
### Ответьте на вопросы ниже
Прочитайте вышеизложенное.
```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)