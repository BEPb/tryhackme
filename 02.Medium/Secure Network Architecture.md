[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Secure Network Architecture](https://tryhackme.com/r/room/introtosecurityarchitecture) 

Всего 8 заданий:
## Задание 1
Сетевое взаимодействие является одним из важнейших компонентов корпоративной среды, но его часто можно упустить из 
виду с точки зрения безопасности. Правильно спроектированная сеть обеспечивает не только использование Интернета и 
связь устройств, но и избыточность, оптимизацию и безопасность.

В хорошо спроектированной сети, если коммутатор выходит из строя, пакеты могут быть перераспределены по другому 
маршруту без потери времени безотказной работы. Если веб-сервер скомпрометирован, он не может пересекать сеть и 
получать доступ к важной информации. Системный администратор должен быть уверен, что его серверы защищены, если 
случайное устройство присоединяется к сети, зная, что устройство сегментировано от остальной части сети и не может 
получить доступ к этим системам.

Все эти концепции и сценарии отличают функциональную сеть от хорошо спроектированной сети.

В этой комнате мы разберем эти сценарии или цели и поймем различные концепции, которые мы можем использовать для их 
внедрения в сеть. Мы также обсудим потенциальные угрозы, с которыми может столкнуться сеть даже после внедрения 
надлежащих передовых практик.

Декоративное изображение облака и шара.
Цели обучения
- Понимать принципы проектирования безопасной сетевой архитектуры
- Изучите и внедрите общие концепции и протоколы сетевой безопасности.
- Понимание сетевой среды и потенциальных угроз
Прежде чем приступить к изучению этой темы, мы рекомендуем вам иметь базовые знания об общепринятой сетевой 
  терминологии и концепциях.

В этой комнате мы представим несколько команд и приложений только для демонстрационных целей. На все вопросы можно 
ответить, используя контент, изображения и другие предоставленные материалы.

### Ответьте на вопросы ниже
Прочитайте вышеизложенное и перейдите к следующему заданию.
```commandline
Ответ не нужен
```

## Задание 2
Необходимость безопасной сегментации
Подсети, похоже, решают все проблемы, с которыми может столкнуться сеть; зачем нам использовать другое решение? 
Чтобы ответить на этот вопрос, давайте рассмотрим сценарий, в котором клиент приносит свое собственное устройство, 
распространенная практика, известная как BYOD (Bring Your O wn D evice). Устройство клиента было заражено  
трояном удаленного доступа (RAT), который попытается проникнуть в сеть, к которой подключено устройство, и извлечь 
любую конфиденциальную информацию. При наличии подсетей нет ограничений на то, куда может подключаться зараженное 
устройство, пока существуют надлежащие маршруты, оставляя конфиденциальную информацию и серверы открытыми для 
неизвестного устройства.  Как решить эту проблему? VLAN!

Сети VLAN (виртуальные локальные сети) используются для сегментации частей сети на втором уровне и дифференциации 
устройств.  

VLAN настраиваются на коммутаторе путем добавления «тега» к кадру.  Тег 802.1q или dot1q будет обозначать VLAN, из 
которой исходит трафик.

Схема фрейма, расширяющего поле тега заголовка

Тег 802.1 обеспечивает стандарт между поставщиками, который всегда будет определять VLAN кадра. Например, если наши 
коммутаторы — Cisco, а маршрутизаторы — Juniper, они могут отправлять тегированные кадры и обрабатывать их одинаково,
поскольку это стандартизировано.  В качестве демонстрации мы покажем, как настраивать теги на интерфейсах коммутатора.

В этом примере мы будем использовать коммутатор с открытым исходным кодом: Open vSwitch

Давайте сначала рассмотрим конфигурацию коммутатора по умолчанию.
`$ ovs-vsctl show`
Чтобы добавить VLAN и теги к подинтерфейсу, нам необходимо изменить конфигурацию через ovs-vsctl

`$ ovs-vsctl set port <interface> tag=<0-99>`
Теперь тег должен быть указан в подинтерфейсе конфигурации.

`Port eth1
		tag: 10
		Interface eth1`
Теперь у нас есть первые интерфейсы, настроенные на маркировку своих кадров! Но что, если мы не знаем, откуда 
исходит трафик VLAN? Например, трафик с виртуализированных устройств или сетевой трафик.

Пометка неизвестного трафика
Native VLAN используется для любого трафика, который не помечен и проходит через коммутатор. Чтобы настроить native 
VLAN, мы должны определить, какой интерфейс и тег им назначить, а затем установить интерфейс как native VLAN по 
умолчанию. Ниже приведен пример добавления native VLAN в Open vSwitch.

`$ ovs-vsctl set port eth0 tag=10 vlan_mode=native-untagged`
Теперь весь трафик должен быть помечен, даже с неизвестным происхождением.

### Маршрутизация между VLAN
Но как VLAN подключается к Интернету или получает доступ к ресурсам в других VLAN? Поскольку они сегментированы, они 
не могут общаться за пределами своих помеченных устройств. Так же, как маршрутизаторы используются для связи между 
традиционными сетями, маршрутизаторы могут использоваться для маршрутизации между VLAN.

До внедрения современных решений сетевые инженеры физически подключали коммутатор и маршрутизатор отдельно для 
каждой присутствующей VLAN. В настоящее время эта проблема решается с помощью конструкции ROAS (Router on a Stick).
VLAN настраиваются для связи с маршрутизатором через назначенный интерфейс коммутатора, известный как порт 
коммутатора. Соединение между коммутатором и маршрутизатором известно как транк. VLAN маршрутизируются через порт 
коммутатора, требуя только одного транка/соединения между коммутатором и маршрутизатором, следовательно, «на палочке ».

Перед настройкой маршрутизатора мы должны настроить транк на уже существующем соединении. В нашей демонстрационной 
лабораторной среде транки по умолчанию настроены как мосты. Каждый поставщик настраивает свои транки и порты 
коммутатора по-разному, некоторые даже с помощью собственных протоколов; пожалуйста, обратитесь к их конкретной 
документации.

Ниже приведен пример добавления нового моста и интерфейса для создания транка.
```commandline
$ ovs-vsctl add-br br0
$ ovs-vsctl add-port br0 eth0 tag=10
```
Теперь мы можем настроить наш маршрутизатор для маршрутизации тегированного трафика между VLAN. Помните, как 
упоминалось, когда мы ввели теги, поскольку тег 802.1q стандартизирован, нам нужно только указать нашему 
маршрутизатору, как настроить его порт коммутатора и какие теги принимать для каждого интерфейса.

Поскольку весь маркированный трафик исходит из одного соединения, маршрутизатор должен иметь возможность сохранять 
каждый маркированный кадр отдельно. Это достигается с помощью виртуальных подинтерфейсов; они будут действовать 
аналогично физическим интерфейсам и обычно определяются идентификатором VLAN; синтаксис для подинтерфейсов обычно 
такой:
`<name>.<vlan/sub-interface id> `
Ниже приведен пример добавления нового виртуального подинтерфейса и настройки его соответствующей адресации.
В этом примере мы будем использовать маршрутизатор с открытым исходным кодом: VyOS.
```commandline
vyos@vyos-rtr# set interfaces ethernet eth0 vif 10 description 'VLAN 10'
vyos@vyos-rtr# set interfaces ethernet eth0 vif 10 address '192.168.100.1/24'
```
Если все прошло хорошо и было правильно настроено, мы сможем маршрутизировать трафик между VLAN, сохраняя при этом 
маркировку и изоляцию трафика!

Но действительно ли они изолированы? Физически они изолированы, но поскольку между ними существуют маршруты, то нет 
границы безопасности, и они не обязательно изолированы. Пока существует маршрут между двумя VLAN, любое устройство 
может взаимодействовать между ними.

Это подводит нас к следующим двум задачам, в которых мы обсудим проектирование безопасных VLAN и познакомимся с 
концепцией зонирования.

Анализ конфигурации VLAN
Примените полученные знания для анализа конфигурации VLAN с учетом приведенных ниже выходных данных.

Фрагмент конфигурации интерфейса (нажмите для просмотра)
### Ответьте на вопросы ниже
Сколько каналов присутствует в этой конфигурации?
```commandline
4
```
Каков идентификатор тега VLAN для интерфейса eth12?
```commandline
30
```

## Задание 3
С введением VLAN происходит сдвиг в проектировании сетевой архитектуры, чтобы включить безопасность в качестве 
ключевого фактора.  Безопасность, оптимизация и избыточность должны быть учтены при проектировании сети, в 
идеале без ущерба для одного компонента.

Это подводит нас к вопросу, как правильно реализовать VLAN в качестве границы безопасности? Зоны безопасности!  Зоны 
безопасности определяют, что или кто находится в VLAN и как трафик может входить и выходить.

В зависимости от того, с кем вы общаетесь, каждый сетевой архитектор может иметь свой подход/мнение относительно 
языка или требований, окружающих зоны безопасности. В этой задаче мы погрузим вас в наиболее общепринятые стандарты 
зон безопасности, сохраняя минималистский подход к сегментации.

Ниже мы представим вам таблицу наиболее часто стандартизированных зон. Это сделано только для того, чтобы 
познакомить вас с терминологией; мы рассмотрим каждую концепцию более подробно в этой комнате.

В то время как зоны безопасности в основном влияют на то, что будет происходить внутри, не менее важно учитывать, 
как новый трафик или устройства будут поступать в сеть, назначаться и взаимодействовать с внутренними системами. 
Большая часть внешнего трафика ( HTTP , почта и т. д.) останется в DMZ , но что, если удаленному пользователю 
понадобится доступ к внутреннему ресурсу? Мы можем легко создать правила для ресурсов, к которым пользователь или 
устройство может получить доступ на основе MAC, IP-адресов и т. д. Затем мы можем применять эти правила с помощью 
элементов управления сетевой безопасностью; в следующей задаче мы обсудим различные элементы управления доступом и 
решения для внедрения политик.

Диаграмма, показывающая слои сети со значками, представляющими их компоненты, и межсетевыми экранами между каждым слоем.
Зоны безопасности и средства контроля доступа будут физически определять, как и куда идет трафик. Но как решается, к 
каким ресурсам пользователи или устройства имеют доступ? Правила дорожного движения часто регулируются политикой 
безопасности компании или соответствием требованиям, а также средствами контроля безопасности, которые определяют 
разрешения на доступ.

Теперь мы создали систему для подхода к проектированию VLAN, но как мы можем практически реализовать и обеспечить их?
В следующей задаче мы рассмотрим несколько протоколов и приложений, которые можно использовать для реализации и 
обеспечения VLAN.

### Ответьте на вопросы ниже
Исходя из приведенной выше таблицы, в какой зоне будет находиться пользователь, подключающийся к публичному веб-серверу?
```commandline
External
```
Исходя из приведенной выше таблицы, в какой зоне будет находиться публичный веб-сервер?
```commandline
DMZ
```
Исходя из приведенной выше таблицы, в какой зоне следует разместить основной контроллер домена?
```commandline
Restricted
```

## Задание 4
Теперь, когда мы рассмотрели сегментацию и проектирование безопасной архитектуры, как мы ее реализуем? Если есть 
маршруты между VLAN, которые должны быть разделены, как соответствующий доступ ограничивается или предоставляется?

Политики помогают определить, как контролируется сетевой трафик. Политика сетевого трафика может определять, как 
маршрутизатор будет маршрутизировать трафик, прежде чем будут использоваться другие протоколы маршрутизации, и будет 
ли он это делать. IEEE (Институт инженеров по электротехнике и электронике) стандартизировал несколько политик 
управления доступом и трафиком, таких как QoS (Качество обслуживания) (802.11e). Существует еще много других 
политик маршрутизации и трафика, которые не стандартизированы IEEE, но широко используются всеми поставщиками, 
преследующими те же цели.

В рамках этой задачи основное внимание будет уделено фильтрации трафика и ознакомлению с концепциями сетевой политики.

#### Фильтрация трафика
Прежде чем формально определить, что такое фильтрация трафика, давайте обсудим один из наиболее распространенных 
стандартов определения фильтрации трафика: ACL ( s ) (Списки контроля доступа).

ACL используется как свободный стандарт для создания набора правил для различных реализаций и протоколов контроля 
доступа. В этой задаче мы будем использовать ACL в маршрутизаторе, чтобы решить , следует ли маршрутизировать или 
отбросить пакет на основе определенного списка.

ACL содержит ACE (Access Control Entry) или правила, которые определяют профиль списка на основе предопределенных 
критериев (исходный адрес, адрес назначения и т. д.).

После определения мы можем использовать ACL для нескольких реализаций, специфичных для поставщика. Например, Cisco 
использует ACL для фильтрации трафика, приоритетной или настраиваемой очередности и динамического контроля доступа.

Формально фильтрация трафика обеспечивает безопасность сети, проверку и сегментацию путем фильтрации сетевого 
трафика на основе заранее определенных критериев.

Теперь мы определили, что такое фильтрация трафика и как определяются критерии. Давайте рассмотрим, как мы можем 
реализовать ACL в фильтрациях трафика или политиках контроля доступа.

Чтобы получить практический опыт, мы рассмотрим политики, которые предлагает VyOS. Политика списка доступа VyOS — 
это самая базовая реализация фильтрации на платформе. Политика будет использовать ACL или списки префиксов для 
определения критериев фильтрации.

Давайте разберем, как VyOS создает ACL и определяет политику.

Создайте новую политику списка доступа, указав номер ACL (1 - 2699)
`set policy access-list <acl_number>`
Задайте описание списка доступа.
`set policy access-list <acl_number> description <text>`
Создайте новое правило (или ACE) в ACL и определите действие правила.
`set policy access-list <acl_number> rule <1-65535> action <permit|deny>
`
Определите критерии или параметры для применения/соответствия правила.
`set policy access-list <acl_number> rule <1-65535> <destination|source> <any|host|inverse-mask|network>
`
На этом этапе у нас есть ACL и ACE, которые активно применяются маршрутизатором.

Давайте подведем итоги: ACL определяется как номер ACL и состоит из отдельных правил или ACE, которые описывают 
поведение ACL. Каждый ACE может определять действие, пункт назначения/источник и конкретный адрес/диапазон для 
запуска ACE.

Ниже представлена диаграмма, показывающая допустимый SSH-запрос, разрешенный ACL.
```commandline
Internet Protocol Version 4, Src: 10.10.212.209, Dst: 10.10.212.209
    Protocol: TCP (6)
    Header checksum: 0xbfdd [validation disabled]
    [Header checksum status: Unverified]
    Source: 10.10.212.209
    Destination: 10.10.212.209
Transmission Control Protocol, Src Port: 35560, Dst Port: 22, Seq: 1578, Ack: 1670, Len: 148
    Source Port: 35560
    Destination Port: 22

set policy access-list 1 rule 1 action permit

set policy access-list 1 rule 1 source 10.10.212.209
```

Ниже представлена диаграмма, показывающая недействительный запрос SSH, отклоненный ACL.
```commandline
Internet Protocol Version 4, Src: 10.10.212.209, Dst: 10.10.212.209
    Protocol: TCP (6)
    Header checksum: 0xbfdd [validation disabled]
    [Header checksum status: Unverified]
    Source: 10.10.212.209
    Destination: 10.10.212.209
Transmission Control Protocol, Src Port: 35560, Dst Port: 22, Seq: 1578, Ack: 1670, Len: 148
    Source Port: 35560
    Destination Port: 2


set policy access-list 1 rule 1 action deny

set policy access-list 1 rule 1 source 10.10.212.209
```

При правильной реализации маршрутизатор должен теперь отбрасывать или принимать пакеты в зависимости от их адреса 
источника или назначения.

Но является ли это лучшим решением? Повторяя то, что было рассмотрено в задаче 3, что если мы хотим иметь публичный 
веб-сервер в DMZ и гарантировать, что только HTTP- трафик исходит из него? Что если определенным хостам нужно, чтобы 
определенные протоколы были открыты на сервере? Маршрутизатор может обеспечить только ограниченный объем 
расширяемости для безопасности.

В следующем задании мы продолжим отвечать на этот вопрос и рассмотрим, как можно подойти к решению этой проблемы.

#### Анализ пакетов и ACL
Теперь, когда мы понимаем структуру ACL и то, что он будет искать в пакете, давайте проанализируем несколько пакетов 
и политик ACL, чтобы определить, будут ли они приняты или отброшены.

Ниже приведена каждая необходимая политика пакетов и ACL ; ответьте на вопросы, используя указанные ниже ресурсы.

Пакет №1 (Нажмите для просмотра)
Политика ACL №1 (Нажмите для просмотра)
Пакет №2 (Нажмите для просмотра)
Политика ACL №2 (Нажмите для просмотра)
### Ответьте на вопросы ниже
Согласно соответствующей политике ACL, первый пакет будет отброшен или принят? 
```commandline
accept
```
Согласно соответствующей политике ACL, приведет ли второй пакет к отбрасыванию или принятию?
```commandline
drop
```

## Задание 5
Возвращаясь к вопросам, заданным в предыдущей задаче, мы должны сначала понять, что мы рассматриваем. Сетевые 
соображения часто включают размер, трафик и корреляцию данных; при рассмотрении протоколов и требований зоны нам 
нужно сместить фокус на трафик и корреляцию.

Корреляция трафика стандартизирована как состояние пакета, например (протокол, процесс, направление и т. д.)

Мы должны использовать межсетевой экран для анализа состояния пакета и применения политик на основе этого состояния.

### Брандмауэры
На самом высоком уровне базовые сетевые брандмауэры определяются в двух категориях: stateless и stateful. Категория 
протокола определяется на основе его способности учитывать состояние пакета. Например, ACL, используемые в 
предыдущей задаче, будут рассматриваться как протокол без состояния.

Файрвол с отслеживанием состояния может лучше сопоставлять информацию в сетевом подключении. Это позволяет файрволу 
фильтровать на основе протоколов, портов, процессов или другой информации с устройства и т. д. Для получения 
дополнительной информации посетите комнату Расширение вашей сети.

Перед настройкой брандмауэра нам нужно рассмотреть, как можно применить требования зон к правилам брандмауэра. Как 
можно определить различные действия на основе протокола и зоны источника/назначения? Пары зон!

#### Зона-Пары
Пары зон — это политика, основанная на направлениях и состоянии, которая будет обеспечивать трафик в отдельных 
направлениях для каждой VLAN, отсюда и пара зон. Например,  DMZ → LAN или  LAN → DMZ.

Каждая зона в данной топологии должна иметь отдельную пару зон друг для друга в топологии и каждом возможном 
направлении. Такой подход обеспечивает максимальную видимость с брандмауэра и радикально улучшает возможности 
фильтрации.

В этой задаче мы будем использовать VyOS в качестве примера настройки межсетевого экрана для сопряжения зон.

Прежде чем определять политику зонирования каждой пары, необходимо добавить общее имя и действие по умолчанию для 
каждой VLAN.

Вспомним из задачи два, что VLAN маршрутизируются через транк и разделяются через подинтерфейсы. Синтаксис, 
<interface>.<VLAN #>например,eth0.30

Ниже приведен пример настройки действия по умолчанию для DMZ и назначения VLAN общему имени зоны.
```commandline
set zone-policy zone dmz default-action drop
set zone-policy zone dmz interface eth0.30
```
Повторите этот процесс для каждого интерфейса VLAN или зоны, определенной в сети.

Теперь мы можем начать решать каждое направление зон-пар. Для этой задачи мы будем ссылаться на топологию ниже.

Сетевая диаграмма, показывающая межсетевой экран VyOS, подключенный к DMZ, LAN и WAN

Каждая зона будет иметь соответствующую пару для каждой другой зоны. Чтобы определить каждую пару зон, мы запишем 
каждую возможную пару и протоколы или действия, которые мы можем применить к паре зон.

Ниже приведен пример таблицы каждой пары зон в приведенной выше топологии и того, как могут выглядеть возможные 
протоколы/действия.

Это дает нам хорошее представление об ожидаемом поведении нашей сети и хороший план для начала настройки брандмауэра.

Помните: Не весь трафик — IPv4! В зависимости от конфигурации вашей сети вам также может потребоваться настроить 
правила IPv6!

Из-за заданного нами действия по умолчанию любые протоколы, возникающие в сети и не определенные, будут по умолчанию 
отброшены.

Мы не будем рассматривать каждый набор правил и пару зон; вместо этого мы рассмотрим одну пару зон в каждом 
направлении и проверим, что поведение работает так, как и ожидалось. В этом примере мы настроим пары зон LAN и WAN. 
После этого примера вы будете чувствовать себя уверенно, настраивая небольшое количество пар зон самостоятельно.

Для всех наборов правил брандмауэра VyOS мы должны начать с определения правил действия и состояния по умолчанию. Мы 
не будем рассматривать тонкости этой конфигурации, поскольку это не является целью этой комнаты. Вместо того чтобы 
повторять семь команд для создания каждого правила, мы положимся на конфигурацию VyOS для определения каждого 
правила. Ниже приведен пример базового набора правил VyOS. Он должен быть одинаковым в верхней части каждого 
создаваемого вами набора правил.
```commandline
name lan-wan {
  default-action drop
  enable-default-log
  rule 1 {
    action accept
    state {
      established enable
      related enable
    }
  }
  rule 2 {
    action drop
    log enable
    state {
      invalid enable
    }
  }
}
```
Теперь добавим правило для ICMP.
```commandline
rule 100 {
    action drop # Define the action for the rule
    log enable # Enable logging to track connection attempts in VyOS
    protocol ipv4-icmp # Protocol to monitor and enforce the action on
 }
```
Теперь, когда у нас есть наш первый набор правил для пары зон, давайте создадим правила для противоположного 
направления пары зон: WAN → LAN. Ниже приведен набор правил, необходимый для разрешения трафика ICMP.
```commandline
name wan-lan {
  default-action drop
  enable-default-log
  rule 1 {
    action accept
    state {
      established enable
      related enable
    }
  }
  rule 2 {
    action drop
    log enable
    state {
      invalid enable
    }
  }
	rule 100 {
    action accept
    log enable
    protocol ipv4-icmp
 }
}
```
Зона-пара теперь определена с соответствующими действиями и состояниями. Теперь мы можем объединить набор правил 
брандмауэра с ранее настроенной зоной.
Напомним: в начале этой задачи мы настроили политики зоны с соответствующим интерфейсом и общим именем.
Ниже приведен общий синтаксис для добавления пары зон.
`
set zone-policy zone <zone A> from <zone B> firewall <name> <ruleset name>
`
Ниже мы установим пару зон для пар LAN → WAN и WAN → LAN.
`
set zone-policy zone LAN from WAN firewall name lan-wan
set zone-policy zone WAN from LAN firewall name wan-lan
`
Теперь нам следует определить и применить наши первые пары зон. Чтобы протестировать нашу новую конфигурацию, мы 
можем попытаться отправить ping команду в обоих направлениях, чтобы убедиться, что брандмауэр отбрасывает или 
принимает наши пакеты ICMP.

Создание пары зон с нуля

Теперь, когда вы понимаете, как создать базовую политику зон-пар, запустите статический сайт, прикрепленный к этой 
задаче, нажав зеленую кнопку View Site. Используйте таблицу ниже, чтобы заполнить пробелы, предоставленные на 
статическом сайте.

### Ответьте на вопросы ниже
Какой флаг появляется после заполнения всех пробелов на статическом сайте?
```commandline
THM{M05tly_53cure}
```
## Задание 6
Чтобы приступить к этой задаче, давайте сначала начнем со сценария. В вашей организации есть надлежащее зонирование 
и маршруты. Зональная пара между DMZ и LAN позволяет устанавливать HTTPS-подключение. Конечно, брандмауэр должен 
принимать эти подключения... Как еще Сьюзи должна следить за установкой обновлений Facebook или Azure?

В этом сценарии предположим, что есть злоумышленник, который внедрил имплант через фишинг на машину локальной сети. 
Если предположить, что механизмы защиты хоста вышли из строя, как можно обнаружить и отслеживать имплант? Если их 
маяк использует HTTPS через DMZ. Это будет выглядеть как в первую очередь легитимный трафик для вашего брандмауэра 
и аналитиков.

Чтобы решить эту проблему, нам необходимо использовать проверку SSL/TLS для перехвата HTTPS-соединений.

#### Проверка SSL/TLS

Проверка SSL/TLS использует  SSL-прокси для перехвата протоколов, включая HTTP , POP3, SMTP или другой зашифрованный 
трафик SSL/TLS. После перехвата прокси-сервер расшифрует трафик и отправит его на обработку платформой  UTM  ( U 
nified  Threat Management  ). Решения UTM будут использовать глубокую проверку SSL, передавая расшифрованный трафик 
с прокси-сервера в другие  службы UTM, включая , помимо прочего, веб-фильтры или  IPS  ( Intrusion Prevention System 
), для обработки информации.

Это решение может показаться идеальным, но каковы недостатки? Некоторые из вас, возможно, уже заметили, что для 
этого требуется SSL-прокси или  MitM ( Man- in- t he- Middle ). Даже если брандмауэр или поставщик уже внедрили 
решение, оно все равно будет действовать как MiTM между вашими устройствами и внешним миром; что, если оно 
перехватит потенциально открытые текстовые пароли? Корпорация должна оценить плюсы и минусы этого решения в 
зависимости от его рассчитанного риска. Вы можете разрешить все приложения, которые, как вы знаете, безопаснее, 
чтобы предотвратить потенциальные недостатки, но это решение все равно будет иметь недостатки. Например, продвинутый 
субъект угроз может направить свой трафик через облачного провайдера или доверенный домен.

### Ответьте на вопросы ниже
Требуется ли для проверки SSL прокси-сервер типа «человек посередине»? (Да/Нет)
```commandline
Y
```
Какая платформа обрабатывает данные, отправленные с SSL-прокси?
```commandline
Unified Threat Management 
```

## Задание 7
#### DHCP- снупинг
Cisco определяет DHCP-отслеживание как «функцию безопасности, которая действует как межсетевой экран между 
ненадежными хостами и доверенными DHCP-серверами».

DHCP snooping был введен для борьбы с несанкционированными DHCP-серверами ; он будет проверять и ограничивать 
скорость DHCP- трафика по мере необходимости. Если хост не является доверенным, его трафик будет отфильтрован и 
ограничен по скорости.

Хотя DHCP — это протокол третьего уровня, DHCP snooping работает на коммутаторе на втором уровне. Коммутатор будет 
хранить ненадежные хосты с арендованными IP-адресами в базе данных привязки DHCP. База данных используется для 
проверки трафика и может использоваться другими протоколами, такими как динамическая проверка ARP, которую мы 
рассмотрим позже в этой задаче.

Мы знаем, как DHCP snooping будет собирать и хранить адреса, но как он определяет, что делать с трафиком? Ниже 
приведен список условий, которые протокол будет проверять, чтобы определить, следует ли отбрасывать пакет DHCP.

Любой пакет DHCP получен извне сети.
Исходный MAC-адрес и аппаратный адрес DHCP- клиента не совпадают.
Пакет A DHCPRELEASE или DHCPDECLINE получен на недоверенном интерфейсе, который не соответствует интерфейсу, который 
уже зарегистрирован в исходном адресе.
Пакет DHCP, включающий адрес ретрансляционного агента, который не является 0.0.0.0
Хотя IEEE в нескольких исследовательских работах признало DHCP snooping, стандартизации не существует. При этом, 
как правило, он не меняется между поставщиками, в отличие от других протоколов.

#### Динамическая проверка ARP
Cisco определяет проверку ARP как «функцию безопасности, которая проверяет пакеты протокола разрешения адресов (ARP)
в сети».

Проверка ARP будет проверять и ограничивать скорость пакетов ARP по мере необходимости; если MAC-адрес и IP-адрес 
пакета ARP не совпадают, протокол перехватит, зарегистрирует и отбросит пакет.

Проверка ARP использует базу данных привязки DHCP, заполненную в результате DHCP- отслеживания, в качестве списка 
IP-адресов привязки.

Подведем итог: база данных привязки DHCP предоставляет ожидаемую пару MAC- и IP-адресов ненадежных хостов; проверка 
ARP сравнит исходный IP-адрес и MAC-адрес с парой привязки; если они не совпадают, пакет будет отброшен.

Ниже представлена диаграмма, показывающая действительный запрос ARP , который соответствует как базе данных привязки,
так и информации запроса.
```commandline
Address Resolution Protocol (request)
    Hardware type: Ethernet (1)
    Protocol type: IPv4 (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: request (1)
    Sender MAC address: 02:c8:85:b5:5a:aa (02:c8:85:b5:5a:aa)
    Sender IP address: 10.10.0.1
    Target MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)
    Target IP address: 10.10.239.154 


Router# show ip dhcp snoop bind
MacAddress         IpAddress       Lease(sec) Type          VLAN Interface
------------------ --------------- ---------- ------------- ---- --------------------
02:c8:85:b5:5a:aa  10.10.0.1       23453      dhcp-snooping 10   GigabitEthernet1/1
01:02:03:04:05:06  2.2.2.2         69445      dhcp-snooping 20   GigabitEthernet2/1
```
Ниже представлена схема, показывающая недействительный ARP- запрос, который не соответствует базе данных привязки и 
запрашивает информацию (обратите внимание, что MAC-адрес отправителя был подделан).
```commandline
Address Resolution Protocol (request)
    Hardware type: Ethernet (1)
    Protocol type: IPv4 (0x0800)
    Hardware size: 6
    Protocol size: 4
    Opcode: request (1)
    Sender MAC address: 02:c8:85:bb:bb:bb (02:c8:85:bb:bb:bb)
    Sender IP address: 10.10.0.1
    Target MAC address: 00:00:00_00:00:00 (00:00:00:00:00:00)
    Target IP address: 10.10.239.154 


Router# show ip dhcp snoop bind
MacAddress         IpAddress       Lease(sec) Type          VLAN Interface
------------------ --------------- ---------- ------------- ---- --------------------
02:c8:85:b5:5a:aa  10.10.0.1       23453      dhcp-snooping 10   GigabitEthernet1/1
01:02:03:04:05:06  2.2.2.2         69445      dhcp-snooping 20   GigabitEthernet2/1
```
### Ответьте на вопросы ниже
Где DHCP Snooping хранит арендованные IP-адреса от ненадежных хостов?
```commandline
DHCP Binding Database
```
Будет ли коммутатор отбрасывать или принимать пакет DHCPRELEASE?
```commandline
Drop
```
Использует ли динамическая проверка ARP базу данных привязки DHCP? (Да/Нет)
```commandline
Y
```
Динамическая проверка ARP будет сопоставлять IP-адрес и какие другие детали пакета?
```commandline
MAC Address
```

## Задание 8
В этой комнате мы расширили общие требования к хорошо спроектированной сети, включив в них стандарты безопасности.

Мы обсудили подходы и решения для проблем, часто встречающихся на уровнях два и три модели OSI. Может показаться, 
что это не решает всех проблем, и каждая среда может иметь разные требования к тому, что она должна отслеживать и 
блокировать.

Чтобы продолжить изучение сетевой безопасности за пределами проектирования, пройдите комнату Протоколы сетевой 
безопасности . Вы выйдете за рамки обсуждаемых нами уровней и рассмотрите безопасность с седьмого по третий уровни, 
которые мы не обсуждали в этой комнате.

### Ответьте на вопросы ниже
Прочитайте вышеизложенное и продолжайте обучение!

```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)