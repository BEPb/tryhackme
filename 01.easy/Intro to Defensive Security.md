[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Intro to Defensive Security]() 

Всего 3 задания:
## Задание 1
Наступательная безопасность фокусируется на одном: взломе систем. Взлом систем может быть достигнут путем 
эксплуатации ошибок, злоупотребления небезопасными настройками и использования преимуществ неиспользуемых политик 
контроля доступа, среди прочего. Красные команды и тестировщики на проникновение специализируются на наступательной 
безопасности.   

Оборонительная безопасность в некоторой степени противоположна наступательной безопасности, поскольку она связана с 
двумя основными задачами: 

### Предотвращение вторжений
Обнаружение вторжений в случае их возникновения и правильное реагирование
Синие команды являются частью оборонительного ландшафта безопасности.


Некоторые из задач, связанных с оборонительной безопасностью, включают в себя:
- Осведомленность пользователей о кибербезопасности: обучение пользователей основам кибербезопасности помогает 
защитить их системы от различных атак.
- Документирование и управление активами: нам необходимо знать типы систем и устройств, которыми нам предстоит 
  управлять и которые необходимо защищать должным образом.
- Обновление и исправление систем: обеспечение правильного обновления и исправления всех известных уязвимостей 
  (слабых мест) компьютеров, серверов и сетевых устройств.
- Настройка превентивных устройств безопасности: брандмауэр и системы предотвращения вторжений ( IPS ) являются 
  важнейшими компонентами превентивной безопасности. Брандмауэры контролируют, какой сетевой трафик может поступать 
  внутрь, а какой может покидать систему или сеть. IPS блокирует любой сетевой трафик, который соответствует текущим 
  правилам и сигнатурам атак.  
- Настройка устройств регистрации и мониторинга: Без надлежащего регистрации и мониторинга сети невозможно обнаружить 
  вредоносные действия и вторжения. Если в нашей сети появляется новое несанкционированное устройство, мы должны знать об этом.
- Защитная безопасность — это гораздо больше, и приведенный выше список охватывает лишь несколько общих тем.

В этом номере мы рассмотрим:

- Центр безопасности операций ( SOC )
- Разведка угроз
- Цифровая криминалистика и реагирование на инциденты ( DFIR )
- Анализ вредоносного ПО

### Ответить на вопросы ниже
Какая команда фокусируется на оборонительной безопасности?

```commandline
Blue Team
```

## Задание 2
В этом задании мы рассмотрим две основные темы, связанные с оборонительной безопасностью:
- Центр безопасности операций ( SOC ), где мы занимаемся анализом угроз
- Цифровая криминалистика и реагирование на инциденты ( DFIR ), где мы также занимаемся анализом вредоносных программ

### Центр безопасности операций ( SOC )
Центр операций по безопасности ( SOC ) — это команда профессионалов в области кибербезопасности, которая отслеживает 
сеть и ее системы для обнаружения вредоносных событий кибербезопасности. Некоторые из основных областей интереса для 
SOC :  
- Уязвимости: Всякий раз, когда обнаруживается уязвимость (слабость) системы, необходимо исправить ее, установив 
соответствующее обновление или патч. Если исправление недоступно, следует принять необходимые меры, чтобы не 
  допустить его использования злоумышленником. Хотя устранение уязвимостей имеет жизненно важное значение для SOC, 
  оно не обязательно возлагается на них.  
- Нарушения политики: Мы можем рассматривать политику безопасности как набор правил, необходимых для защиты сети и 
  систем. Например, это может быть нарушением политики, если пользователи начнут загружать конфиденциальные данные 
  компании в онлайн-хранилище. 
- Несанкционированная активность: Рассмотрим случай, когда имя пользователя и пароль украдены, и злоумышленник 
  использует их для входа в сеть. SOC должен обнаружить такое событие и заблокировать его как можно скорее, прежде 
  чем будет нанесен дальнейший ущерб. 
- Сетевые вторжения: Независимо от того, насколько хороша ваша безопасность, всегда есть шанс вторжения. Вторжение 
  может произойти, когда пользователь нажимает на вредоносную ссылку или когда злоумышленник использует публичный 
  сервер. В любом случае, когда происходит вторжение, мы должны обнаружить его как можно скорее, чтобы предотвратить 
  дальнейший ущерб.  
Операции по обеспечению безопасности охватывают различные задачи по обеспечению защиты; одной из таких задач 
  является сбор информации об угрозах. 


### Разведка угроз
В этом контексте разведка относится к информации, которую вы собираете о реальных и потенциальных врагах. Угроза — 
это любое действие, которое может нарушить или негативно повлиять на систему. Разведка угроз направлена на сбор 
информации, чтобы помочь компании лучше подготовиться к потенциальным противникам. Целью будет достижение защиты, 
основанной на информации об угрозах. У разных компаний разные противники. Некоторые противники могут стремиться 
украсть данные клиентов у мобильного оператора; однако другие противники заинтересованы в остановке производства на 
нефтеперерабатывающем заводе. Примерами противников являются киберармия национального государства, работающая по 
политическим причинам, и группа программ-вымогателей, действующая в финансовых целях. Основываясь на компании (цели),
мы можем ожидать противников.       

Разведке нужны данные. Данные должны быть собраны, обработаны и проанализированы. Сбор данных осуществляется из 
локальных источников, таких как сетевые журналы, и из общедоступных источников, таких как форумы. Обработка данных 
направлена на то, чтобы упорядочить их в формате, пригодном для анализа. Фаза анализа направлена на поиск 
дополнительной информации о злоумышленниках и их мотивах; более того, она направлена на создание списка 
рекомендаций и действенных шагов.    

Изучение ваших противников позволяет вам узнать их тактику, методы и процедуры. В результате разведки угроз мы 
идентифицируем субъекта угрозы (противника), прогнозируем его активность и, следовательно, сможем смягчить их атаки 
и подготовить стратегию реагирования.  

### Цифровая криминалистика и реагирование на инциденты ( DFIR )
В этом разделе речь идет о цифровой криминалистике и реагировании на инциденты ( DFIR ). Мы рассмотрим:

- Цифровая криминалистика
- Реагирование на инциденты
- Анализ вредоносного ПО
### Цифровая криминалистика
Криминалистика — это применение науки для расследования преступлений и установления фактов. С использованием и 
распространением цифровых систем, таких как компьютеры и смартфоны, возникла новая отрасль криминалистики для 
расследования связанных с ними преступлений: компьютерная криминалистика, которая позже превратилась в цифровую 
криминалистику .   

В оборонительной безопасности фокус цифровой криминалистики смещается на анализ доказательств атаки и ее 
исполнителей, а также других областей, таких как кража интеллектуальной собственности, кибершпионаж и владение 
несанкционированным контентом. Следовательно, цифровая криминалистика будет фокусироваться на различных областях, 
таких как:   
- Файловая система: Анализ цифрового криминалистического образа (низкоуровневой копии) хранилища системы позволяет 
получить большой объем информации, такой как установленные программы, созданные файлы, частично перезаписанные файлы 
  и удаленные файлы. 
- Системная память: если злоумышленник запускает свою вредоносную программу в памяти, не сохраняя ее на диске, 
  создание криминалистического образа (низкоуровневой копии) системной памяти — лучший способ проанализировать ее 
  содержимое и узнать об атаке. 
- Системные журналы: Каждый клиентский и серверный компьютер поддерживает различные файлы журналов о том, что 
  происходит. Файлы журналов предоставляют массу информации о том, что произошло в системе. Некоторые следы 
  останутся, даже если злоумышленник попытается очистить свои следы. 
- Сетевые журналы: журналы сетевых пакетов, прошедших через сеть, помогут ответить на большее количество вопросов о 
  том, происходит ли атака и что она влечет за собой.
### Реагирование на инциденты
Инцидент обычно относится к утечке данных или кибератаке; однако в некоторых случаях это может быть что-то менее 
критическое, например, неправильная конфигурация, попытка вторжения или нарушение политики. Примерами кибератаки 
являются действия злоумышленника, делающего нашу сеть или системы недоступными, порча (изменение) общедоступного 
веб-сайта и утечка данных (кража данных компании). Как бы вы отреагировали на кибератаку? Реагирование на инцидент 
определяет методологию, которой следует следовать для обработки такого случая. Цель состоит в том, чтобы уменьшить 
ущерб и восстановиться в кратчайшие сроки. В идеале вы должны разработать план, готовый к реагированию на инцидент.     

### Четыре основных этапа процесса реагирования на инциденты:

- Подготовка: Для этого требуется обученная и готовая к инцидентам команда. В идеале, различные меры принимаются для 
предотвращения инцидентов в первую очередь.
- Обнаружение и анализ: у команды есть необходимые ресурсы для обнаружения любого инцидента; более того, крайне важно 
  провести дополнительный анализ любого обнаруженного инцидента, чтобы узнать его серьезность.
- Сдерживание, искоренение и восстановление: После обнаружения инцидента крайне важно не допустить его влияния на 
  другие системы, устранить его и восстановить затронутые системы. Например, когда мы замечаем, что система заражена 
  компьютерным вирусом, мы хотели бы остановить (сдержать) распространение вируса на другие системы, очистить 
  (искоренить) вирус и обеспечить надлежащее восстановление системы.  
- Действия после инцидента: после успешного восстановления составляется отчет, а извлеченные уроки распространяются 
для предотвращения подобных инцидентов в будущем. 


### Анализ вредоносного ПО
`Malware` означает вредоносное программное обеспечение. Программное обеспечение относится к программам, документам и 
файлам, которые вы можете сохранить на диске или отправить по сети. Вредоносное программное обеспечение включает в 
себя множество типов, таких как:  

`Вирус` — это фрагмент кода (часть программы), который прикрепляется к программе. Он предназначен для 
распространения с одного компьютера на другой; более того, он работает, изменяя, перезаписывая и удаляя файлы после 
заражения компьютера. Результат варьируется от замедления работы компьютера до полной его неработоспособности.

`Троянский конь` — это программа, которая показывает одну желаемую функцию, но скрывает вредоносную функцию под ней. 
Например, жертва может загрузить видеоплеер с теневого веб-сайта, который дает злоумышленнику полный контроль над ее 
системой.  

`Ransomware` — вредоносная программа, которая шифрует файлы пользователя. Шифрование делает файлы нечитаемыми без 
знания пароля шифрования. Злоумышленник предлагает пользователю пароль шифрования, если пользователь готов заплатить 
«выкуп».  


Анализ вредоносного ПО направлен на изучение таких вредоносных программ с использованием различных средств:
- Статический анализ работает путем проверки вредоносной программы без ее запуска. Обычно для этого требуются прочные 
знания языка ассемблера (набор инструкций процессора, т. е. основные инструкции компьютера). 
- Динамический анализ работает путем запуска вредоносного ПО в контролируемой среде и мониторинга его активности. Он 
позволяет вам наблюдать, как вредоносное ПО ведет себя во время работы. 
### Ответить на вопросы ниже
Как бы вы назвали команду профессионалов в области кибербезопасности, которая отслеживает сеть и ее системы на 
предмет вредоносных событий? 

```commandline
Security Operations Center
```
Что означает аббревиатура DFIR?
```commandline
Digital Forensics and Incident Response
```
Какой вид вредоносного ПО требует от пользователя заплатить деньги за восстановление доступа к своим файлам?
```commandline
ransomware
```

## Задание 3
Какова типичная задача, которую вы будете выполнять в качестве аналитика безопасности? Нажмите «Просмотреть сайт», 
чтобы следить за тем, пока не получите флаг. (Если вы впервые получаете флаги, флаг можно рассматривать как строку 
текста, которую вы получаете после выполнения задачи. Пример флага — FLAG{WORDS_AND_MORE}.)  


### Посмотреть сайт
Вы являетесь частью Центра операций по безопасности ( SOC ), отвечающего за защиту банка. SOC этого банка использует 
систему управления информацией и событиями безопасности ( SIEM ). SIEM собирает информацию и события, связанные с 
безопасностью, из различных источников и представляет их через одну систему. Например, вы будете уведомлены, если 
будет неудачная попытка входа или попытка входа из неожиданного географического местоположения. Более того, с 
появлением машинного обучения SIEM может обнаружить необычное поведение, например, когда пользователь входит в 
систему в 3 часа ночи, когда он обычно входит в систему только в рабочее время.     

В этом упражнении мы будем взаимодействовать с SIEM для мониторинга различных событий в нашей сети и системах в 
режиме реального времени. Некоторые события типичны и безвредны; другие могут потребовать дальнейшего вмешательства 
с нашей стороны. Найдите событие, отмеченное красным, запишите его и щелкните по нему для дальнейшего изучения.  

Далее мы хотим узнать больше о подозрительной активности или событии. Подозрительное событие могло быть вызвано 
событием, например, локальным пользователем, локальным компьютером или удаленным IP-адресом. Для отправки и 
получения почты вам нужен физический адрес; аналогично, вам нужен IP-адрес для отправки и получения данных через 
Интернет. IP-адрес — это логический адрес, который позволяет вам общаться через Интернет. Мы проверяем причину 
триггера, чтобы подтвердить, является ли событие действительно вредоносным. Если оно вредоносное, нам необходимо 
предпринять соответствующие действия, например, сообщить об этом кому-то другому в SOC и заблокировать IP-адрес.     

### Ответить на вопросы ниже
Какой флаг вы получили, следуя инструкциям?
```commandline
THM{THREAT-BLOCKED}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)