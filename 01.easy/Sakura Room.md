[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Sakura Room](https://tryhackme.com/r/room/sakura) 

Всего 6 заданий:
## Задание 1
Фон
Эта комната предназначена для тестирования широкого спектра различных методов OSINT . После небольшого исследования 
большинство начинающих практиков OSINT смогут выполнить эти задачи. Эта комната проведет вас через образец 
расследования OSINT , в котором вам будет предложено определить ряд идентификаторов и другой информации, чтобы 
помочь поймать киберпреступника. Каждый раздел будет включать в себя некоторый предлог, который поможет вам в 
правильном направлении, а также один или несколько вопросов, на которые необходимо ответить, чтобы продолжить 
расследование. Хотя все флаги постановочные, эта комната была создана с использованием практических знаний, 
полученных в результате руководства и оказания помощи в расследованиях OSINT как в государственном, так и в частном 
секторе.        

ПРИМЕЧАНИЕ: Все ответы можно получить с помощью пассивных методов OSINT. НЕ пытайтесь использовать какие-либо 
активные методы, такие как обращение к владельцам учетных записей, сброс пароля и т. д., для решения этих проблем.  


Если у вас есть другие вопросы, комментарии или предложения, свяжитесь с нами по адресу @OSINTDojo в Twitter.


Инструкции
Готовы начать? Введите «Поехали!» в поле ответа ниже, чтобы продолжить.

### Ответьте на вопросы ниже
Вы готовы начать?
```commandline
Let's Go!
```

## Задание 2
Фон
Недавно OSINT Dojo оказалась жертвой кибератаки. Похоже , что нет никаких серьезных повреждений, и, похоже, нет 
никаких других существенных признаков компрометации ни одной из наших систем. Однако в ходе судебно-медицинского 
анализа наши администраторы обнаружили изображение, оставленное киберпреступниками. Возможно, оно содержит какие-то 
подсказки, которые позволят нам определить, кто были нападавшие?

Мы скопировали изображение, оставленное злоумышленником, вы можете просмотреть его в своем браузере здесь . 

Инструкции
Изображения могут содержать кладезь информации, как на поверхности, так и встроенной в сам файл. Вы можете найти 
такую информацию, как время создания фотографии, какое программное обеспечение использовалось, информацию об 
авторе и авторских правах, а также другие метаданные, значимые для расследования. Чтобы ответить на следующий вопрос,
вам нужно будет тщательно проанализировать изображение, найденное администраторами OSINT Dojo, чтобы получить 
основную информацию о злоумышленнике.    

### Ответьте на вопросы ниже
Под каким именем пользователя скрывается злоумышленник?
```commandline
SakuraSnowAngelAiko
```

## Задание 3
#### Фон
Похоже, что наш злоумышленник допустил фатальную ошибку в своей операционной безопасности. Похоже, они также 
повторно использовали свое имя пользователя на других платформах социальных сетей. Это должно значительно облегчить 
нам сбор дополнительной информации о них путем поиска их других учетных записей в социальных сетях.    

#### Инструкции
Большинство цифровых платформ имеют поле для имени пользователя. Многие люди привязываются к своим именам 
пользователей и могут использовать их на нескольких платформах, что позволяет легко находить другие аккаунты, 
принадлежащие тому же человеку, если имя пользователя достаточно уникально. Это может быть особенно полезно на таких 
платформах, как сайты по поиску работы, где пользователь с большей вероятностью предоставит реальную информацию о 
себе, например, свое полное имя или информацию о местоположении.     
 

Быстрый поиск в авторитетной поисковой системе может помочь найти соответствующие имена пользователей на других 
платформах, и также существует большое количество специализированных инструментов, которые существуют для той же 
цели. Имейте в виду, что иногда платформа не отображается ни в результатах поисковой системы, ни в 
специализированных поисках имен пользователей из-за ложных отрицательных результатов. В некоторых случаях вам нужно 
вручную проверить сайт самостоятельно, чтобы быть на 100% уверенным, существует ли учетная запись или нет. Чтобы 
ответить на следующие вопросы, используйте имя пользователя злоумышленника, найденное в Задании 2, чтобы расширить 
расследование OSINT на другие платформы, чтобы собрать дополнительную идентификационную информацию о злоумышленнике. 
Будьте осторожны с любыми ложными положительными результатами!        

### Ответьте на вопросы ниже
Какой полный адрес электронной почты использовал злоумышленник?
```commandline
SakuraSnowAngel83@protonmail.com
```
Каково полное настоящее имя злоумышленника?
```commandline
Aiko Abe
```

## Задание 4
#### Фон
Похоже, киберпреступник знает, что мы за ним следим. Когда мы исследовали его аккаунт на Github, мы заметили 
признаки того, что владелец аккаунта уже начал редактировать и удалять информацию, чтобы сбить нас со следа. 
Вероятно, они удаляли эту информацию, потому что она содержала какие-то данные, которые могли бы помочь нашему 
расследованию. Возможно, есть способ получить исходную информацию, которую они предоставили?    

#### Инструкции
На некоторых платформах отредактированный или удаленный контент может быть невосстановимым, если страница не была 
кэширована или заархивирована на другой платформе. Однако другие платформы могут обладать встроенной 
функциональностью для просмотра истории изменений, удалений или вставок. При наличии эта история аудита позволяет 
следователям находить информацию, которая была когда-то включена, возможно, по ошибке или недосмотру, а затем 
удалена пользователем. Такой контент часто бывает весьма ценным в ходе расследования. Чтобы ответить на приведенные 
ниже вопросы, вам нужно будет выполнить более глубокое погружение в учетную запись Github злоумышленника для любой 
дополнительной информации, которая могла быть изменена или удалена. Затем вы будете использовать эту информацию для 
отслеживания некоторых криптовалютных транзакций злоумышленника.        

### Ответьте на вопросы ниже
Для какой криптовалюты у злоумышленника есть криптовалютный кошелек?
```commandline
Ethereum
```
Какой адрес криптовалютного кошелька злоумышленника?
```commandline
0xa102397dbeeBeFD8cD2F73A89122fCdB53abB6ef
```
Из какого майнингового пула злоумышленник получал выплаты 23 января 2021 года по всемирному координированному времени?
```commandline
Ethermine
```
Какую еще криптовалюту злоумышленник обменял, используя свой криптовалютный кошелек?
```commandline
Tether
```

## Задание 5
#### Фон
Как мы и думали, киберпреступник полностью осознает, что мы собираем информацию о них после их атаки. Они даже были 
настолько наглы, что написали в OSINT Dojo в Twitter и насмехались над нами за наши усилия. Учетная запись Twitter, 
которую они использовали, похоже, использует другое имя пользователя, чем то, которое мы отслеживали ранее, может 
быть, есть какая-то дополнительная информация, которую мы можем найти, чтобы получить представление о том, куда они 
направляются дальше?    

Мы сделали скриншот сообщения, отправленного нам злоумышленником, вы можете просмотреть его в своем браузере. здесь .

#### Инструкции

Хотя многие пользователи используют свое имя пользователя на разных платформах, не редкость, что пользователи также 
имеют альтернативные учетные записи, которые они держат полностью отдельно, например, для расследований, троллинга 
или просто как способ отделить свою личную и публичную жизнь. Эти альтернативные учетные записи могут содержать 
информацию, не отображаемую в других учетных записях, и также должны быть тщательно исследованы. Чтобы ответить на 
следующие вопросы, вам нужно будет просмотреть скриншот сообщения, отправленного злоумышленником в OSINT Dojo в 
Twitter, и использовать его для поиска дополнительной информации в учетной записи злоумышленника в Twitter. Затем 
вам нужно будет проследить за зацепками из учетной записи Twitter в Dark Web и другие платформы, чтобы обнаружить 
дополнительную информацию.       

### Ответьте на вопросы ниже
Какой текущий никнейм злоумышленника в Twitter?
```commandline
SakuraLoverAiko
```
Каков URL-адрес места, где злоумышленник сохранил свои SSID и пароли WiFi?
```commandline
http://deepv2w7p33xa4pwxzwi2ps4j62gfxpyp44ezjbmpttxz3owlsp4ljid.onion

```
Каков BSSID домашней сети WiFi злоумышленника?

```commandline
84:af:ec:34:fc:f8
```

## Задание 6
#### Фон
Судя по их твитам, похоже, наш киберпреступник действительно направляется домой, как он и утверждал. В их аккаунте 
Twitter, похоже, есть много фотографий, которые должны позволить нам восстановить их маршрут обратно домой. Если мы 
проследим по следу из хлебных крошек, которые они оставили, мы сможем отследить их перемещения из одного места в 
другое вплоть до конечного пункта назначения. Как только мы сможем определить их конечные остановки, мы сможем 
определить, в какую правоохранительную организацию следует направить наши выводы.

#### Инструкции
В OSINT часто нет «дымящегося пистолета», который указывает на четкий и окончательный ответ. Вместо этого аналитик 
OSINT должен научиться синтезировать несколько фрагментов разведданных, чтобы сделать вывод о том, что вероятно, 
маловероятно или возможно. Используя все доступные данные, аналитик может принимать более обоснованные решения и, 
возможно, даже минимизировать размер пробелов в данных. Чтобы ответить на следующие вопросы, используйте информацию, 
собранную из учетной записи Twitter злоумышленника, а также информацию, полученную из предыдущих частей 
расследования, чтобы отследить злоумышленника до места, которое он называет домом.     

#### Ответьте на вопросы ниже
Какой аэропорт находится ближе всего к месту, фотографию которого злоумышленник выложил перед посадкой на свой рейс?
```commandline
DCA
```
В каком аэропорту злоумышленник совершил последнюю пересадку?
```commandline
HND
```
Какое озеро можно увидеть на карте, которой поделился злоумышленник, когда он совершал свой последний рейс домой?
```commandline
Lake Inawashiro
```
Какой город злоумышленник, скорее всего, считает своим «домом»?
```commandline
Hirosaki
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)