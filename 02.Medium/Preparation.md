[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Preparation](https://tryhackme.com/r/room/preparation) 

Всего 6 заданий:
## Задание 1
Добро пожаловать на подготовительный этап нашего модуля «Реагирование на инциденты».

В этом зале рассматривается подготовка к инцидентам безопасности и настройка ведения журнала для эффективного сбора 
артефактов и дополнительных доказательств до возникновения инцидента безопасности.

### Сценарий модуля
Наша организация SwiftSpend Financial (SSF) наняла вас в качестве специалиста по связям с общественностью для нашей 
команды реагирования на инциденты, которая находится в стадии завершения. Вы заметили, что до сих пор не было 
сделано абсолютно ничего для документирования базовой сети и системных действий — черт, да тут вообще почти нет 
документации!

Нам повезло, что существует хотя бы подобие основы системы обнаружения, поскольку ИТ-отдел следовал лучшим практикам 
безопасности (удивительно, не правда ли?), включая включение ведения журнала для наших конечных точек, разбиение 
наших различных отделов на подсети, обеспечение работы всех систем на PowerShell v5 и включение пересылки журнала 
событий.

Однако вы выявляете некоторые конфигурации, которые не были настроены, и считаете, что организация не полностью 
созрела в своих процедурах реагирования на инциденты.

Цели обучения
- Понять необходимость наличия возможности реагирования на инциденты.
- Понять потребность в процессе, людях и технологиях для реагирования на инциденты.
- Предварительные условия для комнаты

Прежде чем приступить к работе с этой комнатой, мы рекомендуем вам пройти курс обучения SOC уровня 1.

### Ответьте на вопросы ниже
Я готов подготовить организацию к реагированию на инциденты.
```commandline
Ответ не нужен
```

## Задание 2
#### Отчет о реагировании на инцидент
Зная, что мы занимаемся процессом реагирования на инциденты в этой комнате, вы, как ожидается, знакомы с тем фактом, 
что реагирование на инциденты обычно связано с концепциями цифровой криминалистики. Реагирование на инциденты, также 
известное как обработка инцидентов, представляет собой функцию кибербезопасности, которая использует различные 
методологии, инструменты и методы для обнаружения и управления враждебными атаками, минимизируя при этом воздействие,
время восстановления и общие эксплуатационные расходы. Для устранения атак требуется сдерживание заражений 
вредоносным ПО, выявление и устранение уязвимостей, а также поиск, управление и развертывание технического и 
нетехнического персонала.

Настройка возможностей реагирования на инциденты требует от организаций принятия ряда решений, включая конкретное 
определение термина «инцидент», чтобы соответствовать четкой области действия. Таким образом, мы можем различать 
события и инциденты следующим образом:

- Событие: Это наблюдаемое событие в системе или сети. Оно варьируется от подключения пользователя к файловому 
серверу, отправки пользователем электронных писем или блокировки заражения антивирусным ПО.
- Инцидент: это нарушение злоумышленником политик или практик безопасности с целью оказать негативное влияние на 
  организацию посредством таких действий, как кража данных, шифрование с помощью программ-вымогателей или отказ в обслуживании.

#### Процесс реагирования на инциденты
В качестве обзора мы рассмотрим ниже процесс IR . Этот процесс призван служить дорожной картой для лиц, реагирующих 
на инциденты, позволяя им адаптироваться по мере продвижения своих расследований и мер по смягчению последствий.

Оставшаяся часть комнаты будет посвящена первой фазе — подготовке , а все остальное будет рассмотрено в последующих 
комнатах.

Примечательный процесс IR состоит из следующих этапов:

- Подготовка: обеспечивает возможность организации эффективно реагировать на нарушение с помощью установленных 
  процедур.
- Идентификация: Необходимо отметить отклонения в работе и определить, могут ли они вызвать неблагоприятные 
  последствия.
- Анализ или определение области действия: организация определяет масштаб инцидента безопасности, включая выявление 
  затронутых систем, типа данных, находящихся под угрозой, и потенциального воздействия на организацию.
- Сдерживание: ограничение ущерба имеет первостепенное значение, поэтому необходимо изолировать затронутые системы и 
  сохранить вещественные доказательства.
- Устранение: Вредоносные артефакты и методы будут удалены, а затронутые системы восстановлены.
- Восстановление и извлеченные уроки: бизнес-операции должны быть возобновлены полностью после устранения всех угроз 
  и восстановления систем до полной функциональности. Кроме того, организация учитывает опыт, обновляет свои 
  возможности реагирования и проводит обновленное обучение на основе инцидента.  

#### Необходимость плана реагирования на инциденты
Возможности реагирования на инциденты выигрывают от организации процессов реагирования в последовательную 
методологию. Кроме того, информация, собранная в ходе процесса, усилит защиту от будущих атак на системы и данные. 
Вот где в игру вступает план реагирования на инциденты.

План  реагирования на инциденты (IRP) — это документ, в котором излагаются шаги, которые организация предпримет для 
реагирования на инцидент. IRP должен быть швейцарским армейским ножом организации, всесторонне охватывающим все 
аспекты процесса реагирования на инциденты, роли и обязанности, каналы связи между заинтересованными сторонами и 
метрики для оценки эффективности процесса IR.

Чтобы иметь эффективный план реагирования на инциденты, вам пришлось бы пройти через многочисленные итерационные 
процессы, создавая шаблоны и рефакторируя процесс. Это гарантирует, что вы сможете принимать данные об инцидентах и 
смягчать нарушения по мере их возникновения. Шаблоны также будут полезны при создании отчетов об инцидентах.

План реагирования на инцидент сопровождается использованием плейбуков. Плейбуков, которые предоставят организации 
действия и процедуры для выявления, сдерживания, искоренения, восстановления и отслеживания успешных мер по 
смягчению последствий инцидентов.


### Ответьте на вопросы ниже
Что такое наблюдаемое явление внутри системы?
```commandline
Event
```
Что считается нарушением политики и практики безопасности?
```commandline
Incident
```
На каком этапе реагирования на инциденты организации разрабатывают свои процедуры?
```commandline
Preparation
```
На каком этапе организация полностью возобновит свою деятельность и обновит свои возможности реагирования?
```commandline
Recovery and Lessons Learned
```

## Задание 3
Когда мы начинаем рассматривать первую фазу, важно знать, что цель подготовки к обработке инцидентов — убедиться, 
что ваша команда и организация готовы к обработке и восстановлению после инцидентов. На этапе подготовки следует 
охватить многочисленные элементы, включая людей, политику, технологии, коммуникацию и документацию.

#### Подготовка людей
Хорошо известно, что самая легкая и доступная точка атаки для любой организации — это ее люди. Ваши сотрудники и 
товарищи по команде — это враждебные цели, в основном с помощью социальной инженерии и фишинговых тактик. Поэтому 
важно эффективно подготовить свою команду к распознаванию и реагированию на инциденты до, во время и после них.

#### Создание CSIRT-команд
Вам необходимо создать группу реагирования на инциденты кибербезопасности (CSIRT), в которую войдут специалисты по 
бизнесу, техническим вопросам, юридическим вопросам и связям с общественностью с соответствующими навыками и 
полномочиями для принятия решений во время кибератаки. После создания группы ее членам потребуются соответствующие 
разрешения в рамках устоявшейся политики контроля доступа. Этот доступ должен быть хорошо организован и 
контролироваться, с надлежащими уведомлениями системных администраторов, когда CSIRT использует привилегированный 
доступ.

#### Сеансы обучения и оценки
Изображение, демонстрирующее ход тренировки.
Поскольку мы определили некоторые способы, которыми злоумышленники нацеливаются на людей, наиболее эффективным 
способом обеспечения их знаниями об этих атаках является постоянное обучение, оценка и повышение осведомленности. 
Проведение кампаний социальной инженерии, тестирование восприимчивости пользователей к фишинговым атакам и 
предоставление обучения по текущим вопросам будут иметь решающее значение для подготовки вашей команды.

Это обучение также касается ваших конечных пользователей и клиентов, которые будут выступать в качестве ваших 
датчиков и источников оповещения, когда они обнаружат что-то подозрительное, происходящее на их стороне. В этом 
случае обучающий контент, такой как Модуль анализа фишинга, который мы предоставляем, будет жизненно важен для 
внутренних и внешних заинтересованных сторон, чтобы знать, как обнаруживать и реагировать на фишинговые атаки.

Кроме того, обработчики инцидентов должны быть знакомы с инструментами криминалистической визуализации, как читать 
журналы аудита и выполнять анализ с использованием honeypots и уязвимых систем. Это позволит им выявлять 
подозрительные события при их возникновении и проводить практическую криминалистику при возникновении необходимости.

#### Подготовка документации
Изображение, демонстрирующее процесс документирования
Документация по инцидентам может стать спасением для организации. Собранная информация может быть использована в 
качестве доказательства в преступной кибератаке или может стать инструментом для разработки планов смягчения 
последствий и оценки извлеченных уроков. Это означает, что респондентам инцидентов необходимо развивать навыки 
ведения заметок и ориентированности на детали.

#### Политики
Определение принципов и рекомендаций для процессов безопасности имеет решающее значение при проведении подготовки. 
Это гарантирует, что методы обработки инцидента хорошо известны. Политики должны быть видны сотрудникам, 
пользователям и другим заинтересованным лицам, например, с помощью предупреждающих баннеров, которые будут 
информировать о запрете несанкционированных действий и ограничивать презумпцию конфиденциальности в организации.

Кроме того, политики должны определять полномочия организации по мониторингу сети и всех систем под ее крышей. 
Политики должны быть рассмотрены юридической группой и приведены в соответствие с местными законами и правилами о 
конфиденциальности.

#### План коммуникаций и цепочка поставок
Политики будут сопровождаться планом коммуникации, в котором будет указано, кто в команде CSIRT должен быть точкой 
контакта и какие процедуры должны соблюдаться. Например, в CSIRT могут быть сотрудники, которые всегда на связи, 
чтобы получать сообщения о предполагаемых инцидентах. Эти сообщения должны инициировать цепочку действий, включая 
время уведомления правоохранительных органов, сотрудников СМИ или третьих лиц. Кроме того, команда будет отслеживать 
поток информации и управлять формами и документами доказательств, такими как документы цепочки поставок. Эти 
документы предназначены для отслеживания потока информации, обработки доказательств и отчетности при рассмотрении 
любого инцидента. Шаблон такого документа можно загрузить из этой задачи выше.

#### Процедуры реагирования
Обработка инцидентов должна рассматриваться как организационная операция, гарантирующая каждому члену роль в 
предотвращении ущерба и возвращении к нормальной работе. Это означает, что процедуры по умолчанию должны быть 
определены и одобрены руководством. Эффективность и своевременность имеют решающее значение, когда защита 
безопасности нарушена; таким образом, упорядоченные процессы будут определять характер обработки нарушений.

### Ответьте на вопросы ниже
Как называется группа, которая занимается событиями, связанными с нарушениями кибербезопасности, и в которую входят 
люди с различными навыками и опытом?
```commandline
cyber security incident response team
```

Какие документы будут использоваться для сопровождения собранных доказательств и позволят отслеживать, кто проводит 
следственные процедуры?
```commandline
chain of custody documents
```

## Задание 4
Люди и политики, созданные CSIRT, потребуют поддержки инструментов и решений для защиты и обороны технологической 
инфраструктуры своей организации. Любая операция реагирования на инциденты включает организацию устройств, систем и 
технологий, которые будут способствовать предотвращению, обнаружению и смягчению любого происшествия. В результате, 
знание вашей технической инфраструктуры имеет важное значение для процесса реагирования на инциденты.

#### Классификация инвентаризации активов
Крайне важно определить высокоценные активы в организации вместе с их техническим составом. Это будет включать 
инфраструктуру, интеллектуальную собственность, данные клиентов и сотрудников, а также репутацию бренда. Защита этих 
активов гарантирует, что конфиденциальность, целостность и доступность услуг, данных и процессов организации не 
будут нарушены, что также поможет сохранить доверие. Кроме того, классификация активов будет полезна для определения 
приоритетов защитных и детективных мер для активов.

Пример инвентарного списка может быть следующим. Обратите внимание, что для надлежащего отслеживания желательно 
иметь инвентарные списки оборудования и программного обеспечения.

Техническое оснащение
После определения инвентаризации следует провести телеметрию сетевой инфраструктуры, что необходимо для реагирования 
на инциденты. Это означает отображение каждого сетевого устройства, облачной платформы, системы и приложения. 
Наличие этой инфраструктурной картины упрощает реализацию системных и сенсорных механизмов обнаружения. Эти 
механизмы включают в себя средства защиты от вредоносного ПО, инструменты обнаружения и реагирования на конечные 
точки ( EDR ), предотвращение потери данных ( DLP ), системы обнаружения и предотвращения вторжений (IDPS) и 
возможности сбора журналов.

Одним из ключевых аспектов сбора телеметрии является сетевое подсетирование. Это средство логической группировки 
сетевых устройств и IP-адресов с определенными разрешениями и политиками доступа и использования, использующее 
брандмауэры, демилитаризованные зоны и сегментацию IP-адресов. Эти телеметрические данные и сведения об инцидентах 
можно собирать и отслеживать с помощью таких инструментов, как TheHive Project . Однако следует отметить, что 
TheHive мог быть обновлен с момента выпуска комнаты.

Изображение, показывающее вид панели управления TheHive.

Возможности расследования
На изображении показан пример спасательного мешка, полезного для спасателей.

Для проведения любых расследований во время атаки или нарушения специалисты по реагированию на инциденты должны 
убедиться, что они могут проверить выполнение скриптов и установщиков на всех конечных точках и хостах в своей сети 
и реализовать технические возможности для облегчения сдерживания, анализа и репликации атак. Должны быть средства 
сбора криминалистических доказательств с использованием инструментов создания образов дисков и памяти, безопасного 
хранилища, доступного только CSIRT, и инструментов анализа, таких как песочницы. Сопровождать эти усилия должен 
пакет для обработки инцидентов. Этот пакет содержит все необходимые инструменты для реагирования на инциденты. 
Каждый комплект будет уникальным; однако, как специалисту по реагированию на инциденты, стоит иметь в своем арсенале 
следующие предметы:

- Средства массовой информации направляются для хранения собираемых доказательств.
- Программное обеспечение для создания образов дисков и проведения судебно-медицинской экспертизы, такое как FTK 
  Imager, EnCase и The Sleuth Kit.
- Сетевое подключение для зеркалирования и мониторинга трафика.
- Кабели и адаптеры, такие как USB, SATA, а также кард-ридеры для решения распространенных задач.
- Комплекты для ремонта ПК, включающие наборы отверток и пинцеты.
- Копии форм реагирования на инциденты и руководств по коммуникации.

### Ответьте на вопросы ниже
Как будет называться комплект, содержащий необходимые инструменты для реагирования на инциденты?
```commandline
Jump bag
```

## Задание 5
После настройки людей, процессов и проверок технологий для реагирования на инциденты вы должны знать, что происходит 
в цифровых активах вашей организации. Это гарантирует, что вы избежите цифровой забывчивости, имея видимость по всей 
сети.

Что подразумевает видимость? Видимость охватывает сбор данных аудита и журналов, мониторинг потоков разведданных об 
угрозах по новым тактикам, методам и процедурам противника (TTP) и прием рекомендаций по исправлению ошибок 
поставщиков. Эти источники информации позволяют организации обнаруживать, идентифицировать, оценивать, оповещать и 
смягчать несанкционированную и аномальную активность в сети. Внутренняя видимость вращается вокруг управления 
журналами, и наличие максимального покрытия должно быть частью стратегий киберустойчивости и обработки инцидентов. 
Напротив, внешняя видимость подразумевает осведомленность о том, что происходит в сообществе и ландшафте угроз.

Знание преимуществ, которые дает видимость в процессе обработки инцидентов, имеет важное значение. Ниже приведены 
некоторые из преимуществ:

- Предоставляет фактическую информацию о доступе к ресурсам, времени доступа и о том, кто осуществлял действие.
- Прозрачность посредством управления журналами может помочь повысить эффективность процессов, политик и процедур.
- Благодаря собранным данным журналов инциденты можно обрабатывать с использованием конкретных доказательств.
- Соблюдение нормативных требований упрощается благодаря сбору данных журналов.
- Держит вас в курсе новых угроз, TTP и сигнатур.
- Обеспечивает регулярное обновление систем.

#### Видимость через журналы
Каждое вычислительное устройство в сети организации может генерировать и хранить журналы. Задача агрегации журналов 
решается с помощью решений Security Information Event Management ( SIEM ) , которые предоставляют центральную 
платформу хранения и анализа. Журналы должны быть защищены от любых изменений после записи. Кроме того, как член 
команды CSIRT, вы должны знать, что сбор журналов позволяет другим этапам процесса реагирования на инциденты 
проходить максимально гладко.

К распространенным типам записей журнала, которые следует включить и отслеживать, относятся:

- Событие: эти журналы регистрируют информацию о событиях в системе или сети, например, попытки входа в систему, 
события приложений и сетевой трафик.
- Аудит: Они охватывают последовательную запись действий в системе, фиксируя, кто выполнил действие, какое действие 
  было инициировано и как отреагировала система. Существует два класса журналов аудита: Успех и Отказ .
- Ошибка: когда в системе возникает проблема, например, сбой обслуживания, события регистрируются в журналах ошибок.
- Отладка: во время тестирования систем и служб записываются журналы отладки, которые помогают находить проблемы и 
  облегчают устранение неполадок.

Записи журнала будут получены из различных источников в инфраструктуре организации. Некоторые известные источники 
  журналов включают:

- Сетевые журналы: в основном они собираются с сетевых устройств, таких как коммутаторы и маршрутизаторы, а также с 
помощью решений по захвату пакетов.
- Журналы периметра хоста: в основном они поддерживаются брандмауэрами, прокси-серверами и VPN-серверами. Они 
  содержат информацию о разрешенных и запрещенных действиях, передаваемую на хост-устройства организации.
- Системные журналы: эти журналы регистрируют события и службы, запускаемые операционной системой.
- Журналы приложений: Это журналы, собранные из приложений, работающих внутри. Они могут включать веб-приложения, 
  облачные сервисы, базы данных и фирменные инструменты.

#### Настройка видимости
Прежде чем погрузиться в содержимое настройки видимости, запустите виртуальную машину, нажав на зеленую кнопку " 
Start Machine" в правом верхнем углу этой задачи. Дайте ей около 4 минут, чтобы полностью загрузиться в Split 
View. Если машина не отображается, нажмите синюю кнопку "Show Split View" в правом верхнем углу этой комнаты.

Поскольку мы определили источники и типы журналов, которые необходимо собрать, CSIRT должна разработать процедуры и 
планы для настройки правильных инструментов и политик конфигурации в системах, указанных в инвентаризации активов, 
для сбора и объединения всех необходимых журналов. В системах Windows политики безопасности можно настроить с 
помощью локального или группового управления политиками, причем последнее используется для нескольких систем в 
Active Directory.

Давайте рассмотрим пример настройки политик для сеансов интерактивного входа, которые еще не определены, как вы 
можете видеть ниже. После загрузки виртуальной машины откройте Windows Administrative Tools через меню Start и 
найдите параметры Local Security Policy . Затем мы можем перейти к следующей политике: Security Settings -> Local 
Policies -> Security Options -> Interactive logon: Display user information when the session is locked.

Оказавшись здесь, вы обнаружите, что политика: Интерактивный вход в систему: Отображать информацию о пользователе, 
когда сеанс заблокирован, не определена. Цель этой политики — установить стандарт того, показывать ли 
идентификационные данные пользователя, такие как имя пользователя, учетная запись домена и адрес электронной почты, 
когда сеанс заблокирован. Для конфиденциальных систем, таких как те, которые используются финансовыми или кадровыми 
отделами, рекомендуется установить эту политику на опцию, которая не отображает никакой информации о пользователе, 
чтобы злоумышленники не узнали, чьи учетные данные использовались в последний раз.


А как быть с событиями, происходящими в системах? Нужны ли им протоколирование и видимость?

Вы можете перейти в связанную комнату, чтобы узнать больше о журналах событий Windows ; однако, рассматривая наш 
сценарий, вы обнаружите, что организация не внедрила мониторинг событий Windows.

В сетевых системах отключено ведение журнала событий, что является неотъемлемой частью обеспечения видимости, 
поскольку злоумышленники могут воспользоваться этой ситуацией, чтобы посеять хаос. Итак, как решить эту проблему?

Первое, что нужно проверить, — это текущая ситуация через Event Viewer. Откройте Event Viewer , закрепленный на 
панели задач, и вас встретит предупреждающий баннер, сообщающий, что служба Event Log недоступна. Это означает, что 
записи реестра для службы были изменены и их необходимо изменить, чтобы включить ее.

На изображении показано сообщение об ошибке, отображаемое при открытии средства просмотра событий, если оно отключено.

Перемещаясь по реестру через: `Windows Administrative Tools -> Registry Editor -> 
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\start`. Вы обнаружите, что значение ключа реестра 
установлено на 4, которое необходимо установить на 2, что означает перевод службы в режим автоматического запуска. 
Измените реестр и перезагрузите систему, чтобы изменения вступили в силу, что должно занять 3 минуты.


После перезагрузки системы вы можете открыть Windows Event Viewer и убедиться, что он работает. Мы можем проверить, 
что система записывает журналы, используя некоторые тесты Atomic Red Team, которые уже были загружены и установлены, 
чтобы имитировать инцидент. Откройте сеанс PowerShell и выполните следующие команды:

Тестовый запуск программы-вымогателя Atomic
```commandline
PS C:\Users\Administrator>Invoke-AtomicTest T1486 -ShowDetailsBrief

T1486-5 PureLocker Ransom Note

PS C:\Users\Administrator>Invoke-AtomicTest T1486-5
PathToAtomicsFolder = C:\AtomicRedTeam\atomics

Executing test: T1486-5 PureLocker Ransom Note
Done executing test: T1486-5 PureLocker Ransom Note
```

Навигация по журналам событий Windows, в разделе Application and Service Logs -> Microsoft -> Windows -> Sysmon -> 
Operational мы можем подтвердить, что наш тест прошел успешно, и для него была создана запись в журнале, выполнив 
поиск теста, который мы провели. Проще использовать функцию поиска для идентификации события из-за притока журналов,
записываемых с момента включения службы.

На изображении показана успешная запись журнала событий Process Create с помощью Sysmon.

### Ответьте на вопросы ниже
Каков идентификатор события для правила создания файла, связанного с тестом?
```commandline
11
```
Какой уровень безопасности по умолчанию назначается всем политикам в соответствии с политиками ограниченного 
использования программ?
```commandline
Unrestricted
```
Найдите папку Audit Policy в разделе Local Policies . Какой параметр был назначен для политики Audit logon events?
```commandline
Failure
```

## Задание 6
Подведение итоговИзображение, демонстрирующее выявление вредоносной активности на компьютере.
Создание процесса реагирования на инциденты жизненно важно для любой организации, и подготовка находится на переднем 
крае этого процесса. Как мы уже говорили в зале, этап подготовки жизненного цикла IR охватывает различные аспекты, 
связанные с людьми, политиками и технологиями.

Организовав свою организацию с помощью надлежащего обучения, определив правильные политики и процедуры, а также 
обеспечив прозрачность с помощью мониторинга журналов и событий, вы будете готовы противостоять любым попыткам 
злоумышленников.

Различные фреймворки в этой области охватывают лучшие практики реагирования на инциденты. Среди них — Computer 
Security Incident Handling Guide от NIST.

После того, как вы собрали информацию и настроили видимость, пришло время перейти к этапам идентификации и 
определения области действия жизненного цикла реагирования на инциденты.

### Ответьте на вопросы ниже
Системы и сети готовы. Время для выявления инцидентов.

```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)