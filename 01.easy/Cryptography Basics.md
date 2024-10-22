

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Cryptography Basics](https://tryhackme.com/r/room/cryptographybasics) 

Всего 7 заданий:
## Задание 1
Вы когда-нибудь задумывались, как предотвратить чтение ваших сообщений третьими лицами? Как ваше приложение или веб-браузер могут создать безопасный канал с удаленным сервером? Под безопасностью мы подразумеваем, что никто не может прочитать или изменить передаваемые данные; кроме того, мы можем быть уверены, что подключаемся к настоящему серверу. Благодаря криптографии эти требования выполняются.

Криптография закладывает основу нашего цифрового мира. В то время как сетевые протоколы сделали возможным общение устройств, разбросанных по всему миру, криптография сделала возможным доверие к этому общению.

Эта комната — первая из трех вводных комнат о криптографии. Нет никаких предварительных условий для обучения, кроме базовых навыков использования командной строки Linux. Если вы не уверены, пожалуйста, рассмотрите возможность присоединиться к пути Pre Security .

Основы криптографии (эта комната)
Основы криптографии с открытым ключом
Основы хеширования

#### Цели обучения
Завершив эту комнату, вы узнаете следующее:

- Ключевые термины криптографии
- Важность криптографии
- Цезарь Шифр
- Стандартные симметричные шифры
- Распространенные асимметричные шифры
- Базовая математика, обычно используемая в криптографии
### Ответьте на вопросы ниже
Я готов начать изучать криптографию!
   
```commandline
Ответ не нужен
```

## Задание 2
Конечной целью криптографии является обеспечение безопасной связи в присутствии противников. Термин «безопасный» 
включает конфиденциальность и целостность передаваемых данных. Криптографию можно определить как практику и изучение 
методов безопасной связи и защиты данных там, где мы ожидаем присутствия противников и третьих лиц. Другими словами, 
эти противники не должны иметь возможности раскрыть или изменить содержимое сообщений.

Криптография используется для защиты конфиденциальности, целостности и подлинности. В этом веке вы ежедневно 
используете криптографию, и вы почти наверняка читаете это через зашифрованное соединение. Рассмотрим следующие 
сценарии, в которых вы бы использовали криптографию:  

- Когда вы входите в TryHackMe, ваши учетные данные шифруются и отправляются на сервер, чтобы никто не мог получить 
их, перехватив ваше соединение.
- При подключении по SSH ваш SSH- клиент и сервер устанавливают зашифрованный туннель, поэтому никто не может 
  подслушать ваш сеанс.
- Когда вы осуществляете онлайн-банкинг, ваш браузер проверяет сертификат удаленного сервера, чтобы подтвердить, что 
  вы общаетесь с сервером вашего банка, а не злоумышленника.
- Когда вы загружаете файл, как вы проверяете, что он был загружен правильно? Криптография предлагает решение с 
  помощью хэш-функций, чтобы подтвердить, что ваш файл идентичен оригинальному.
- Как вы можете видеть, вам редко приходится напрямую взаимодействовать с криптографией, но ее решения и последствия 
  присутствуют повсюду в цифровом мире. Рассмотрим случай, когда компания хочет обрабатывать информацию о кредитных 
  картах и обрабатывать связанные с ними транзакции. При обработке кредитных карт компания должна следовать и 
  обеспечивать соблюдение Стандарта безопасности данных индустрии платежных карт (PCI DSS). В этом случае PCI DSS 
  обеспечивает минимальный уровень безопасности для хранения, обработки и передачи данных, связанных с кредитами 
  карт. Если вы проверите PCI DSS для крупных организаций, вы узнаете, что данные должны быть зашифрованы как при 
  хранении (в состоянии покоя), так и при передаче (в движении).

Точно так же, как обработка данных платежных карт требует соблюдения PCI DSS, обработка медицинских записей требует 
соблюдения их соответствующих стандартов. В отличие от кредитных карт, стандарты обработки медицинских записей 
различаются в разных странах. Примеры законов и нормативных актов, которые следует учитывать при обработке 
медицинских записей, включают HIPAA (Закон о переносимости и подотчетности медицинского страхования) и HITECH 
(Технологии медицинской информации для экономического и клинического здравоохранения) в США, GDPR (Общий регламент 
по защите данных) в ЕС, DPA (Закон о защите данных) в Великобритании. Хотя этот список не является исчерпывающим, он 
дает представление о правовых требованиях, которые поставщики медицинских услуг должны учитывать в зависимости от 
своей страны. Эти законы и нормативные акты показывают, что криптография является необходимостью, которая должна 
присутствовать, но обычно скрыта от прямого доступа пользователя.

### Ответьте на вопросы ниже
Какой стандарт требуется для обработки информации о кредитных картах?


```commandline
PCI DSS
```

## Задание 3
Давайте начнем с иллюстрации, прежде чем вводить ключевые термины. Начнем с открытого текста, который мы хотим 
зашифровать. Открытый текст — это читаемые данные; это может быть что угодно: от простого «привет», фотографии кошки,
информации о кредитной карте или медицинских записей. С точки зрения криптографии, все это сообщения «открытого 
текста», ожидающие шифрования. Открытый текст передается через функцию шифрования вместе с соответствующим ключом; 
функция шифрования возвращает зашифрованный текст. Функция шифрования является частью шифра; шифр — это алгоритм для 
преобразования открытого текста в зашифрованный текст и наоборот.

Функция шифрования принимает открытый текст и ключ в качестве входных данных и возвращает зашифрованный текст в 
качестве выходных данных. 

Чтобы восстановить открытый текст, мы должны передать шифротекст вместе с соответствующим ключом через функцию 
расшифровки, которая даст нам исходный открытый текст. Это показано на иллюстрации ниже.  

Функция расшифровки принимает зашифрованный текст и ключ в качестве входных данных и возвращает открытый текст в 
качестве выходных данных. 

Мы только что ввели несколько новых терминов, и нам нужно их выучить, чтобы понимать любой текст о криптографии. 
Термины перечислены ниже: 

- Открытый текст — это исходное, читаемое сообщение или данные до того, как они будут зашифрованы. Это может быть 
документ, изображение, мультимедийный файл или любые другие двоичные данные.
- Шифротекст — это зашифрованная, нечитаемая версия сообщения после шифрования. В идеале мы не можем получить никакой 
  информации об исходном открытом тексте, кроме его приблизительного размера.
- Шифр — это алгоритм или метод преобразования открытого текста в шифротекст и обратно. Шифр обычно разрабатывается 
  математиком.
- Ключ — это строка битов, которую шифр использует для шифрования или дешифрования данных. В общем случае 
  используемый шифр является общедоступным знанием; однако ключ должен оставаться секретным, если только он не 
  является общедоступным ключом в асимметричном шифровании. Мы рассмотрим асимметричное шифрование в более поздней 
  задаче.  
- Шифрование — это процесс преобразования открытого текста в зашифрованный текст с использованием шифра и ключа. В 
  отличие от ключа, выбор шифра раскрывается.
- Расшифровка — это обратный процесс шифрования, преобразование зашифрованного текста обратно в открытый текст с 
  использованием шифра и ключа. Хотя шифр будет общедоступным, восстановление открытого текста без знания ключа 
  должно быть невозможным (неосуществимым). 

### Ответьте на вопросы ниже
Как вы называете зашифрованный открытый текст?
```commandline
ciphertext
```
Как называется процесс, возвращающий открытый текст?
```commandline
decryption
```

## Задание 4
История криптографии долгая и восходит к Древнему Египту в 1900 году до нашей эры. Однако одним из самых простых 
исторических шифров является шифр Цезаря из первого века до нашей эры. Идея проста: сдвинуть каждую букву на 
определенное число, чтобы зашифровать сообщение.  

Рассмотрим следующий пример:

Открытый текст:TRYHACKME
Ключ: 3 (Предположим, что это сдвиг вправо на 3.)
Шифр: Шифр Цезаря
Мы можем легко вычислить, что T становится W, R становится U, Y становится B и так далее. Как вы заметили, как 
только мы достигаем Z, мы начинаем все сначала, как показано на рисунке ниже. Следовательно, мы получаем 
зашифрованный текст WUBKDFNPH.  

Шифр Цезаря сдвигает каждую букву на определенное число, чтобы зашифровать сообщение.

Для расшифровки нам понадобится следующая информация:

Шифрованный текст:WUBKDFNPH
Ключ: 3
Шифр: Шифр Цезаря
Шифр Цезаря сдвигает каждую букву на определенное число, чтобы расшифровать сообщение.

Для шифрования мы сдвигаем вправо на три; для расшифровки мы сдвигаем влево на три и восстанавливаем исходный 
открытый текст, как показано на изображении выше. Однако, если кто-то дает вам зашифрованный текст и говорит, что он 
был зашифрован с помощью шифра Цезаря, восстановление исходного текста будет тривиальной задачей, поскольку 
существует всего 25 возможных ключей. Английский алфавит состоит из 26 букв, и сдвиг на 26 сохранит букву неизменной;
следовательно, 25 допустимых ключей для шифрования с помощью шифра Цезаря. На рисунке ниже показано, как будет 
успешно выполнено расшифровывание, если перебрать все возможные ключи; в этом случае мы восстановили исходное 
сообщение с помощью K e y  = 5. Следовательно, по сегодняшним стандартам, где шифр общеизвестен, шифр Цезаря 
считается небезопасным. 

Шифр Цезаря уязвим к атакам методом перебора.

Вы встретите гораздо больше исторических шифров в фильмах и книгах по криптографии. Вот некоторые примеры:

Шифр Виженера XVI века
Машина «Энигма» времен Второй мировой войны
Одноразовый блокнот времен холодной войны
### Ответьте на вопросы ниже
Зная, что сообщение XRPCTCRGNEIбыло зашифровано с помощью шифра Цезаря, каков исходный открытый текст?


```commandline
ICANENCRYPT
```

## Задание 5
Две основные категории шифрования — симметричное и асимметричное .

#### Симметричное шифрование
Симметричное шифрование , также известное как симметричная криптография , использует один и тот же ключ для шифрования и дешифрования данных, как показано на рисунке ниже. Хранение ключа в секрете является обязательным; это также называется криптографией с закрытым ключом . Кроме того, передача ключа предполагаемым сторонам может быть сложной задачей, поскольку для этого требуется защищенный канал связи. Поддержание секретности ключа может быть значительной проблемой, особенно если получателей много. Проблема становится более серьезной в присутствии сильного противника; рассмотрим, например, угрозу промышленного шпионажа.

Симметричное шифрование использует общий секретный ключ для шифрования и дешифрования.

Рассмотрим простой случай, когда вы создали защищенный паролем документ, чтобы поделиться им с коллегой. Вы можете легко отправить зашифрованный документ по электронной почте своему коллеге, но, скорее всего, вы не сможете отправить ему пароль по электронной почте. Причина в том, что любой, у кого есть доступ к его почтовому ящику, получит доступ как к защищенному паролем документу, так и к его паролю. Поэтому вам нужно придумать другой способ, то есть канал, чтобы поделиться паролем. Если вы не придумаете безопасный, доступный канал, одним из решений будет личная встреча и сообщение ему пароля.

Примерами симметричного шифрования являются DES (стандарт шифрования данных), 3DES (тройной DES) и AES (расширенный стандарт шифрования).

DES был принят в качестве стандарта в 1977 году и использует 56-битный ключ. С развитием вычислительной мощности в 1999 году ключ DES был успешно взломан менее чем за 24 часа, что послужило мотивацией для перехода на 3DES.
3DES — это DES, примененный три раза; следовательно, размер ключа составляет 168 бит, хотя эффективная безопасность составляет 112 бит. 3DES был скорее специальным решением, когда DES больше не считался безопасным. 3DES был объявлен устаревшим в 2019 году и должен быть заменен на AES ; однако его все еще можно встретить в некоторых устаревших системах.
AES был принят в качестве стандарта в 2001 году. Размер его ключа может составлять 128, 192 или 256 бит.
Существует множество других симметричных шифров шифрования, используемых в различных приложениях; однако они не 
приняты в качестве стандартов. 

#### Асимметричное шифрование
В отличие от симметричного шифрования, которое использует один и тот же ключ для шифрования и дешифрования, 
асимметричное шифрование использует пару ключей, один для шифрования, а другой для дешифрования, как показано на 
рисунке ниже. Для защиты конфиденциальности асимметричное шифрование или асимметричная криптография шифрует данные с 
помощью открытого ключа; поэтому его также называют криптографией с открытым ключом.

Асимметричное шифрование использует открытый ключ получателя для шифрования и закрытый ключ получателя для расшифровки.

Примерами являются RSA, Diffie-Hellman и криптография на основе эллиптических кривых (ECC). Два ключа, участвующие в 
процессе, называются открытым ключом и закрытым ключом. Данные, зашифрованные открытым ключом, могут быть 
расшифрованы закрытым ключом. Ваш закрытый ключ должен храниться в тайне, отсюда и название.

Асимметричное шифрование, как правило, медленнее, и многие асимметричные шифры шифрования используют более длинные 
ключи, чем симметричное шифрование. Например, RSA использует 2048-битные, 3072-битные и 4096-битные ключи; 
2048-битный — это рекомендуемый минимальный размер ключа. Диффи-Хеллман также имеет рекомендуемый минимальный размер 
ключа 2048 бит, но использует 3072-битные и 4096-битные ключи для повышенной безопасности. С другой стороны, ECC 
может достичь эквивалентной безопасности с более короткими ключами. Например, с 256-битным ключом ECC обеспечивает 
уровень безопасности, сравнимый с 3072-битным ключом RSA.

Асимметричное шифрование основано на определенной группе математических задач, которые легко вычислить в одном 
направлении, но крайне сложно в обратном. В этом контексте крайне сложно означает практически неосуществимо. 
Например, мы можем положиться на математическую задачу, решение которой с использованием современных технологий 
заняло бы очень много времени, например, миллионы лет.

Мы рассмотрим различные асимметричные шифры шифрования в следующей комнате. Сейчас важно отметить, что асимметричное 
шифрование предоставляет вам открытый ключ, которым вы делитесь со всеми, и закрытый ключ, который вы храните в 
тайне и в безопасности.

Краткое изложение новых терминов
Алиса и Боб — вымышленные персонажи, которые обычно используются в примерах криптографии для представления двух 
сторон, пытающихся безопасно общаться. Симметричное шифрование — это метод, в котором один и тот же ключ 
используется как для шифрования, так и для дешифрования. Следовательно, этот ключ должен оставаться в безопасности и 
никогда не должен быть раскрыт никому, кроме предполагаемой стороны. Асимметричное шифрование — это метод, в котором 
используются два разных ключа: открытый ключ для шифрования и закрытый ключ для дешифрования.
### Ответьте на вопросы ниже
Стоит ли доверять DES? (Да/Нет)
```commandline
Nay
```
Когда AES был принят в качестве стандарта шифрования?
```commandline
2001
```

## Задание 6
Строительные блоки современной криптографии лежат в математике. Чтобы продемонстрировать некоторые базовые алгоритмы, мы рассмотрим две математические операции, которые используются в различных алгоритмах:

Операция XOR
Операция по модулю
Операция XOR
XOR , сокращение от «исключающее ИЛИ», — логическая операция в двоичной арифметике, которая играет важную роль в различных вычислительных и криптографических приложениях. В двоичной системе XOR сравнивает два бита и возвращает 1, если биты различны, и 0, если они одинаковы, как показано в таблице истинности ниже. Эта операция часто обозначается символом ⊕ или ^.

```commandline
А	Б	А ⊕ Б
0	0	0
0	1	1
1	0	1
1	1	0
```
Если вы впервые работаете с таблицей истинности, то это таблица, которая показывает все возможные результаты. Таблица истинности XOR выше содержит все четыре случая: 0 ⊕ 0 = 0, 0 ⊕ 1 = 1, 1 ⊕ 0 = 1 и 1 ⊕ 1 = 0.

Рассмотрим пример, в котором мы хотим применить XOR к двоичным числам 1010 и 1100. В этом случае мы выполняем операцию побитно: 1 ⊕ 1 = 0, 0 ⊕ 1 = 1, 1 ⊕ 0 = 1 и 0 ⊕ 0 = 0, в результате чего получается 0110.

Вы можете задаться вопросом, как XOR может играть какую-либо роль в криптографии. XOR обладает несколькими интересными свойствами, которые делают его полезным в криптографии и обнаружении ошибок. Одним из ключевых свойств является то, что применение XOR к значению с самим собой дает 0, а применение XOR к любому значению с 0 оставляет его неизменным. Это означает, что A ⊕ A = 0, и A ⊕ 0 = A для любого двоичного значения A. Кроме того, XOR является коммутативным, т. е. A ⊕ B = B ⊕ A. И он ассоциативен, т. е. (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C).

Давайте посмотрим, как можно использовать вышеизложенное в криптографии. Мы покажем, как XOR может использоваться в качестве базового симметричного алгоритма шифрования. Рассмотрим двоичные значения P и K, где P — открытый текст, а K — секретный ключ. Зашифрованный текст — C = P ⊕ K.

Теперь, если мы знаем C и K, мы можем восстановить P. Начнем с C ⊕ K = (P ⊕ K) ⊕ K. Но мы знаем, что (P ⊕ K) ⊕ K = P ⊕ (K ⊕ K), потому что XOR ассоциативен. Кроме того, мы знаем, что K ⊕ K = 0; следовательно, (P ⊕ K) ⊕ K = P ⊕ (K ⊕ K) = P ⊕ 0 = P. Другими словами, XOR служил простым симметричным алгоритмом шифрования. На практике это сложнее, так как нам нужен секретный ключ такой же длины, как и открытый текст.

Операция по модулю
Другая математическая операция, с которой мы часто сталкиваемся в криптографии, — это оператор по модулю, обычно записываемый как % или как m o d . Оператор по модулю, X % Y , — это остаток от деления X на Y. В наших повседневных вычислениях мы больше фокусируемся на результате деления, чем на остатке. Остаток играет важную роль в криптографии.

Вам нужно работать с большими числами при решении некоторых криптографических упражнений. Если ваш калькулятор не справляется, мы предлагаем использовать язык программирования, такой как Python. Python имеет встроенный intтип, который может обрабатывать целые числа произвольного размера и автоматически переключается на большие типы по мере необходимости. Во многих других языках программирования есть специальные библиотеки для больших целых чисел. Если вы предпочитаете решать свои математические задачи онлайн, рассмотрите WolframAlpha .

Давайте рассмотрим несколько примеров.

- 25%5 = 0, потому что 25 деленное на 5 равно 5 с остатком 0, т.е. 25 = 5 × 5 + 0
- 23%6 = 5, потому что 25 деленное на 6 равно 3, с остатком 5, т.е. 23 = 3 × 6 + 5
- 23%7 = 2, потому что 23 деленное на 7 равно 3 с остатком 2, т.е. 23 = 3 × 7 + 2
Важно помнить о модуле, что он необратим. Если нам дано уравнение x %5 = 4 , бесконечные значения x будут удовлетворять этому уравнению.

Операция по модулю всегда возвращает неотрицательный результат, меньший делителя. Это означает, что для любого целого числа a и положительного целого числа n результат a % n всегда будет в диапазоне от 0 до n  − 1 .

### Ответьте на вопросы ниже
Сколько будет 1001 ⊕ 1010?
```commandline
0011
```
Что такое 118613842%9091 ?
```commandline
3565
```
Что такое 60%12 ?
```commandline
0
```

## Задание 7
В этой комнате мы узнали о важности криптографии и некоторых проблемах, которые она решает. Мы также познакомили вас 
с симметричными и асимметричными шифрами шифрования. Наконец, мы объяснили операции XOR и modulo. В следующей 
комнате, Основы криптографии с открытым ключом , мы рассмотрим различные асимметричные криптосистемы и увидим, как 
они решают проблемы, с которыми мы сталкиваемся в цифровом мире.

### Ответьте на вопросы ниже
Прежде чем перейти к следующей комнате, убедитесь, что вы запомнили все ключевые термины и понятия, представленные в 
этой комнате.
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)