[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [x86 Architecture Overview](https://tryhackme.com/r/room/x8664arch) 

Всего 7 заданий:
## Задание 1
Вредоносное ПО часто работает, злоупотребляя способом проектирования систем. Поэтому, чтобы понять, как работает 
вредоносное ПО, важно знать архитектуру систем, в которых оно работает. В этой комнате мы сделаем краткий обзор 
архитектуры x86 с точки зрения анализа вредоносного ПО. Обратите внимание, что может быть много деталей архитектуры 
x86, которые мы пропустим, но это потому, что они не связаны с анализом вредоносного ПО.

Цели обучения:
Подводя итоги, в этом зале мы рассмотрим следующие темы.

- Обзор архитектуры ЦП и ее компонентов
- Различные типы регистров ЦП и их использование
- Структура памяти, просматриваемая программой
- Компоновка стека и регистры стека

Итак, давайте погрузимся в тему и узнаем о вышеупомянутых темах.

### Ответьте на вопросы ниже
Пройдитесь по целям обучения
```commandline
Ответ не нужен
```

## Задание 2
Наиболее широко используемая архитектура ЦП происходит от архитектуры фон Неймана. Краткий обзор этой архитектуры 
представлен на диаграмме ниже. 

 Изображение, показывающее ЦП, содержащий все его компоненты, АЛУ, блок управления и регистры, а также основную 
 память и устройства ввода-вывода, которые находятся за пределами ЦП. 

На этой схеме показано, что ЦП состоит из трех компонентов: арифметико-логического устройства (АЛУ), блока 
управления и регистров. ЦП взаимодействует с памятью и устройствами ввода-вывода за пределами ЦП. Давайте узнаем о 
каждом из компонентов, упомянутых на схеме ниже.  

Блок управления:
Блок управления получает инструкции из основной памяти, изображенной здесь за пределами ЦП . Адрес следующей 
инструкции для выполнения хранится в регистре, называемом указателем инструкций или IP. В 32-битных системах этот 
регистр называется EIP, а в 64-битных системах он называется RIP.  

Арифметико-логическое устройство:
Арифметико-логическое устройство выполняет инструкцию, извлеченную из памяти. Результаты выполненной инструкции 
затем сохраняются либо в регистрах, либо в памяти. 

Регистры:
Регистры — это хранилище ЦП. Регистры, как правило, намного меньше основной памяти, которая находится вне ЦП , и 
помогают экономить время при выполнении инструкций, размещая важные данные в прямом доступе к ЦП .  

Память:
Память, также называемая основной памятью или оперативной памятью (ОЗУ), содержит весь код и данные для запуска 
программы. Когда пользователь запускает программу, ее код и данные загружаются в память, откуда ЦП получает к ней 
доступ по одной инструкции за раз.  

Устройства ввода/вывода:
Устройства ввода-вывода или устройства ввода-вывода — это все остальные устройства, которые взаимодействуют с 
компьютером. К таким устройствам относятся клавиатуры, мыши, дисплеи, принтеры, устройства хранения данных, такие 
как жесткие диски и USB-накопители и т. д.  

Короче говоря, когда программа должна быть выполнена, она загружается в память. Оттуда блок управления извлекает 
одну инструкцию за раз, используя регистр указателя инструкций, а арифметико-логический блок выполняет ее. 
Результаты сохраняются либо в регистрах, либо в памяти.  

### Ответьте на вопросы ниже
В какой части архитектуры фон Неймана хранятся код и данные, необходимые для работы программы?
```commandline
Memory
```
Какая часть ЦП хранит небольшие объемы данных?
```commandline
Registers
```
В какой единице измерения выполняются арифметические действия?
```commandline
Arithmetic Logic Unit
```

## Задание 3
Регистры являются средой хранения ЦП. ЦП может получать доступ к данным из регистров быстрее, чем к любой другой 
среде хранения; однако его ограниченный размер означает, что он должен использоваться эффективно. Для этой цели 
регистры делятся на следующие различные типы:  
- Указатель инструкций
- Регистры общего назначения
- Регистры флагов состояния
- Регистры сегмента
Давайте рассмотрим каждый из этих регистров по отдельности:

Указатель инструкций:
Указатель инструкций — это регистр, содержащий адрес следующей инструкции, которая должна быть выполнена ЦП. Его 
также называют счетчиком программ. Первоначально это был 16-битный регистр в процессоре Intel 8086 (откуда и 
произошел термин x86) и обозначался сокращенно как IP. В 32-битных процессорах указатель инструкций стал 32-битным 
регистром, называемым EIP или расширенным указателем инструкций. В 64-битных системах этот регистр стал 64-битным 
регистром, называемым RIP (здесь R обозначает регистр).

#### Регистры общего назначения
Регистры общего назначения в системе x86 являются 32-битными регистрами. Как следует из названия, они используются 
во время общего выполнения инструкций процессором. В 64-битных системах эти регистры расширены до 64-битных 
регистров. Они содержат следующие регистры.

`EAX или RAX:`
Это регистр аккумулятора. Результаты арифметических операций часто сохраняются в этом регистре. В 32-битных системах 
присутствует 32-битный регистр EAX, а в 64-битных системах присутствует 64-битный регистр RAX. Доступ к последним 16 
битам этого регистра можно получить, обратившись к AX. Аналогично, к нему можно обратиться и по 8 битам, используя 
AL для младших 8 бит и AH для старших 8 бит.Изображение, показывающее распределение различных регистров общего 
назначения

`EBX или RBX:`
Этот регистр также называется Базовым регистром, который часто используется для хранения Базового адреса для ссылки 
на смещение. Подобно EAX/RAX, к нему можно обращаться как к 64-битным RBX, 32-битным EBX, 16-битным BX и 8-битным BH 
и BL регистрам.

`ECX или RCX:`
Этот регистр также называется регистром счетчика и часто используется в операциях подсчета, таких как циклы и т. д. 
Подобно двум вышеуказанным регистрам, к нему можно обращаться как к 64-битному регистру RCX, 32-битному регистру ECX,
16-битному регистру CX и 8-битному регистру CH и CL.

`EDX или RDX:`
Этот регистр также называется регистром данных. Он часто используется в операциях умножения/деления. Подобно 
вышеуказанным регистрам, его можно адресовать как 64-битный RDX, 32-битный EDX, 16-битный DX и 8-битные регистры DH 
и DL.   

`ESP или RSP:`
Этот регистр называется указателем стека. Он указывает на вершину стека и используется совместно с регистром 
сегмента стека. Это 32-битный регистр, называемый ESP в 32-битных системах, и 64-битный регистр, называемый RSP в 
64-битных системах. К нему нельзя обращаться как к меньшим регистрам.  

`EBP или RBP:`
Этот регистр называется Base Pointer. Он используется для доступа к параметрам, переданным стеком. Он также 
используется вместе с регистром Stack Segment. Это 32-битный регистр, называемый EBP в 32-битных системах, и 
64-битный регистр, называемый RBP в 64-битных системах.  

`ESI или RSI:`
Этот регистр называется регистром индекса источника. Он используется для строковых операций. Он используется с 
регистром сегмента данных (DS) в качестве смещения. Это 32-битный регистр, называемый ESI в 32-битных системах, и 
64-битный регистр, называемый RSI в 64-битных системах.  

`ЭОД или РДО:`
Этот регистр называется регистром индекса назначения. Он также используется для строковых операций. Он используется 
с регистром дополнительного сегмента (ES) в качестве смещения. Это 32-битный регистр, называемый EDI в 32-битных 
системах, и 64-битный регистр, называемый RDI в 64-битных системах.  

`Р8-Р15:`
Эти 64-битные регистры общего назначения отсутствуют в 32-битных системах. Они были введены в 64-битных системах. 
Они также адресуемы в 32-битном, 16-битном и 8-битном режимах. Например, для регистра R8 мы можем использовать R8D 
для нижней 32-битной адресации, R8W для нижней 16-битной адресации и R8B для нижней 8-битной адресации. Здесь 
суффикс D обозначает Double-word, W обозначает Word, а B обозначает Byte.   

### Ответьте на вопросы ниже
Какой регистр хранит адрес следующей инструкции, которая должна быть выполнена?
```commandline
Instruction Pointer
```
Какой регистр в 32-битной системе также называется регистром счетчика?
```commandline
ECX
```
Какие регистры из рассмотренных выше отсутствуют в 32-битной системе?
```commandline
R8-R15
```

## Задание 4
#### Регистры флага состояния:
При выполнении выполнения иногда требуется некоторая индикация о статусе выполнения. Вот где появляются флаги состояния. Это один 32-битный регистр для 32-битных систем, называемый EFLAGS, который расширен до 64-бит для 64-битных систем и называется RFLAGS в 64-битной системе. Регистр флагов состояния состоит из отдельных однобитных флагов, которые могут быть либо 1, либо 0. Некоторые из необходимых флагов обсуждаются ниже:

#### Нулевой флаг:
Обозначаемый ZF, флаг Zero указывает, когда результат последней выполненной инструкции был равен нулю. Например, если выполняется инструкция, которая вычитает RAX из себя, результат будет равен 0. В этой ситуации ZF будет установлен в 1.

#### Флаг для переноски:
Флаг переноса, обозначенный как CF, указывает, когда последняя выполненная инструкция привела к числу, слишком большому или слишком маленькому для места назначения. Например, если мы сложим 0xFFFFFFFF и 0x00000001 и сохраним результат в 32-битном регистре, результат будет слишком большим для регистра. В этом случае CF будет установлен в 1.

#### Подписать флаг:
Флаг знака или SF указывает, является ли результат операции отрицательным или старший бит установлен в 1. Если эти 
условия выполняются, SF устанавливается в 1; в противном случае он устанавливается в 0. 

#### Флаг ловушки:
Флаг ловушки или TF указывает, находится ли процессор в режиме отладки. Когда TF установлен, ЦП будет выполнять одну 
инструкцию за раз для целей отладки. Это может использоваться вредоносным ПО для определения того, запущены ли они в 
отладчике.  

Регистры сегмента:
Регистры сегментов — это 16-битные регистры, которые преобразуют плоское пространство памяти в различные сегменты 
для более простой адресации. Существует шесть регистров сегментов, как поясняется ниже: 
- Сегмент кода:  регистр сегмента кода (CS) указывает на раздел кода в памяти.
- Сегмент данных: регистр сегмента данных (DS) указывает на раздел данных программы в памяти.
- Сегмент стека: регистр сегмента стека (SS) указывает на стек программы в памяти.

Дополнительные сегменты (ES, FS и GS): Эти дополнительные сегментные регистры указывают на различные разделы данных. 
Они и регистр DS делят память программы на четыре отдельных раздела данных.  

### Ответьте на вопросы ниже
Какой флаг используется программой для определения того, выполняется ли она в отладчике?
```commandline
Trap Flag
```
Какой флаг будет установлен, если старший бит в операции установлен в 1?
```commandline
Sign Flag
```
Какой сегментный регистр содержит указатель на раздел кода в памяти?
```commandline
Code Segment
```

## Задание 5
Когда программа загружается в память в операционной системе Windows, она видит абстрактное представление памяти. Это 
означает, что программа не имеет доступа ко всей памяти; вместо этого она имеет доступ только к своей памяти. Для 
этой программы это вся память, которая ей нужна. Ради краткости мы не будем вдаваться в подробности того, как 
операционная система выполняет абстракцию. Мы рассмотрим память так, как ее видит программа, поскольку это более 
актуально для нас при обратном проектировании вредоносного ПО.    

Диаграмма здесь представляет собой обзор типичной структуры памяти для программы. Как можно увидеть, память 
разделена на различные разделы, а именно, стек, куча, код и данные. Хотя мы показали четыре раздела в определенном 
порядке, это может отличаться от того, как они будут выглядеть всегда, например, раздел кода может быть ниже раздела 
данных.Изображение, показывающее структуру памяти, включая стек, кучу, код и данные   

Ниже представлен краткий обзор четырех разделов.

#### Код:
Раздел кода, как следует из названия, содержит код программы. В частности, этот раздел относится к текстовому 
разделу в файле Portable Executable, который включает инструкции, выполняемые CPU . Этот раздел памяти имеет 
разрешения на выполнение, что означает, что CPU может выполнять данные в этом разделе памяти программы.

#### Данные:
Раздел Data содержит инициализированные данные, которые не являются переменными и остаются постоянными. Он относится 
к разделу данных в файле Portable Executable. Он часто содержит глобальные переменные и другие данные, которые не 
должны изменяться во время выполнения программы.  

#### Куча:
Куча, также известная как динамическая память, содержит переменные и данные, созданные и уничтоженные во время 
выполнения программы. Когда создается переменная, для нее выделяется память во время выполнения. А когда эта 
переменная удаляется, память освобождается. Отсюда и название — динамическая память.  

Куча:
Стек является одной из важных частей памяти с точки зрения анализа вредоносных программ. Этот раздел памяти содержит 
локальные переменные, аргументы, переданные программе, и адрес возврата родительского процесса, вызвавшего программу.
Поскольку адрес возврата связан с потоком управления инструкций ЦП, стек часто становится целью вредоносных программ 
для перехвата потока управления. Вы можете посмотреть комнату Переполнения буфера , чтобы узнать, как это происходит.
Мы рассмотрим более подробную информацию о стеке в следующей задаче.    

### Ответьте на вопросы ниже
Когда программа загружается в память, имеет ли она полный вид системной памяти? Да или Нет?
```commandline
N
```
В каком разделе Памяти содержится код?
```commandline
Code
```
Какой раздел памяти содержит информацию, связанную с потоком управления программой?
```commandline
Stack
```
## Задание 6
Стек — это часть памяти программы, которая содержит аргументы, переданные программе, локальные переменные и поток 
управления программы. Это делает стек очень важным для анализа вредоносных программ и обратного проектирования. 
Вредоносные программы часто используют стек для захвата потока управления программы. Поэтому важно понимать стек, 
его структуру и его работу.   

Стек — это память типа Last In First Out (LIFO). Это означает, что последний элемент, помещенный в стек, первым 
извлекается. Например, если мы помещаем в стек элементы A, B и C, то при извлечении этих элементов первыми из стека 
будут элементы C, B, а затем A. Процессор использует два регистра для отслеживания стека. Один из них — указатель 
стека (ESP или RSP), а другой — базовый указатель (EBP или RBP).   

#### Указатель стека:
Указатель стека указывает на вершину стека. Когда любой новый элемент помещается в стек, местоположение указателя 
стека изменяется, чтобы учесть новый элемент, помещенный в стек. Аналогично, когда элемент выталкивается из стека, 
указатель стека подстраивается, чтобы отразить это изменение.   

#### Базовый указатель:
Базовый указатель для любой программы остается постоянным. Это адрес ссылки, по которому текущий программный стек 
отслеживает свои локальные переменные и аргументы.Изображение структуры стека, включая локальные переменные, 
указатель стека, базовый указатель, адрес возврата и аргументы, относительно адресного пространства памяти.  

#### Старый базовый указатель и обратный адрес:
Ниже базового указателя находится старый базовый указатель вызывающей программы (программы, которая вызывает текущую 
программу). А ниже старого базового указателя находится адрес возврата, куда указатель инструкций вернется после 
завершения выполнения текущей программы. Распространенный метод перехвата потока управления — переполнение локальной 
переменной в стеке таким образом, чтобы она перезаписала адрес возврата адресом по выбору автора вредоносной 
программы. Этот метод называется переполнением буфера стека.    

#### Аргументы:
Аргументы, передаваемые функции, помещаются в стек до начала выполнения функции. Эти аргументы находятся прямо под 
адресом возврата в стеке. 

#### Функция Пролог и Эпилог:
При вызове функции стек подготавливается к выполнению функции. Это означает, что аргументы помещаются в стек до 
начала выполнения функции. После этого в стек помещаются адрес возврата и старый базовый указатель. После того, как 
эти элементы помещаются в стек, адрес базового указателя изменяется на вершину стека (которая в это время будет 
указателем стека вызывающей функции). По мере выполнения функции указатель стека перемещается в соответствии с 
требованиями функции. Эта часть кода, которая помещает аргументы, адрес возврата и базовый указатель в стек и 
переставляет указатели стека и базы, называется прологом функции.      

Аналогично, Old Base Pointer выталкивается из стека и помещается в Base Pointer при выходе из функции. Адрес 
возврата выталкивается в Instruction Pointer, а Stack Pointer перестраивается так, чтобы указывать на вершину стека. 
Часть кода, которая выполняет это действие, называется Function Epilogue.   

Нажмите кнопку View Site в верхней части задачи, чтобы запустить статический сайт в разделенном виде.  Теперь 
перейдите на прикрепленный статический сайт и найдите флаг, правильно расположив стек.  

### Ответьте на вопросы ниже
Следуйте инструкциям на приложенном статическом сайте и найдите флаг. Что такое флаг?
```commandline
THM{SMASHED_THE_STACK}
```

## Задание 7
На этом мы завершаем эту комнату, посвященную основам архитектуры систем x86-64. В этой комнате мы узнали:
- Архитектура процессора фон Неймана
- Различные компоненты ЦП
- Различные типы регистров ЦП
- Память и ее различные разделы
- Размещение стека программы в памяти


Дайте нам знать, что вы думаете об этой комнате на нашем канале Discord или  в аккаунте Twitter . Увидимся.   

### Ответьте на вопросы ниже
Присоединяйтесь к обсуждению на наших социальных каналах
```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)