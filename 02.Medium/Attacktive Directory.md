

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Attacktive Directory](https://tryhackme.com/r/room/attacktivedirectory) 

Всего 8 заданий:
## Задание 1
м сначала нужно будет подключиться к нашей сети с помощью OpenVPN. Вот мини-руководство по подключению.

( Обратите внимание, что браузерная машина сможет получить доступ к этой машине, вам не нужно будет подключаться к VPN . )

### Ответьте на вопросы ниже
Перейдите на страницу доступа . Выберите нужный вам VPN-сервер и загрузите файл конфигурации.
```commandline
Ответ не нужен
```
Вернитесь на страницу доступа. Вы можете убедиться, что вы подключены, посмотрев на страницу доступа. Обновите 
страницу. Вы должны увидеть зеленую галочку рядом с надписью Connected. Она также покажет вам ваш внутренний IP-адрес. 
Теперь вы готовы приступить к взлому! 
```commandline
Ответ не нужен
```
В качестве альтернативы вы можете развернуть браузерный Kali или Attack Box и автоматически подключиться к сети 
TryHackMe. 
```commandline
Ответ не нужен
```
Подключившись к VPN, запустите машину и приступайте к взлому!
```commandline
Ответ не нужен
```

## Задание 2
#### Установка Impacket:
Независимо от того, используете ли вы Kali 2019.3 или Kali 2021.1, Impacket может быть сложно установить правильно. 
Вот несколько инструкций, которые могут помочь вам установить его правильно!
Примечание: Все инструменты, упомянутые в этой задаче, уже установлены на AttackBox. Эти шаги необходимы только в том случае, если вы настраиваете собственную VM . Impacket также может потребовать от вас использовать версию Python >=3.7. В AttackBox вы можете сделать это, запустив команду с помощью python3.9 <your command> .

Сначала вам нужно будет клонировать репозиторий Impacket Github на ваш ящик. Следующая команда клонирует Impacket в 
/opt/impacket: 

`git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket`

После клонирования репозитория вы увидите несколько файлов, связанных с установкой, requirements.txt и setup.py. 
Файл setup.py, который обычно пропускают во время установки, на самом деле устанавливает Impacket в вашу систему, 
чтобы вы могли использовать его и не беспокоиться о каких-либо зависимостях.  

Чтобы установить требования Python для Impacket:

`pip3 install -r /opt/impacket/requirements.txt`

После завершения установки требований мы можем запустить скрипт установки Python:

`cd /opt/impacket/ && python3 ./setup.py install`

После этого Impacket должен быть правильно установлен и готов к использованию!



Если у вас все еще возникают проблемы, попробуйте следующий скрипт и посмотрите, работает ли он:
```commandline
sudo git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket 
sudo pip3 install -r /opt/impacket/requirements.txt 
cd /opt/impacket/ 
sudo pip3 install . 
sudo python3 setup.py install
```

За правильные инструкции по установке Impacket спасибо Dragonar#0923 в THM Discord  <3



#### Установка Bloodhound и Neo4j

Bloodhound — еще один инструмент, который мы будем использовать при атаке на Attacktive Directory. Мы рассмотрим 
особенности инструмента позже, но сейчас нам нужно установить два пакета с Apt, это bloodhound и neo4j. Вы можете 
установить его с помощью следующей команды:  

`apt install bloodhound neo4j`

Теперь, когда все готово, можно приступать к работе!

#### Поиск неисправностей
Если у вас возникли проблемы с установкой Bloodhound и Neo4j, попробуйте выполнить следующую команду:

`apt update && apt upgrade`

Если у вас возникли проблемы с Impacket, обратитесь за помощью в TryHackMe Discord !

### Ответьте на вопросы ниже
Установите Impacket, Bloodhound и Neo4j
```commandline
Ответ не нужен
```

## Задание 3
Добро пожаловать в Attacktive Directory

Добро пожаловать, уважаемый пользователь!

Спасибо за то, что сделали мою первую комнату. Первоначально я создал эту комнату для своего выпускного проекта по 
программе обучения по кибербезопасности в 2019 году. С тех пор я сделал несколько других комнат, даже сеть для THM . 
В мае 2021 года я принял решение отремонтировать эту комнату и сделать ее более управляемой и менее сложной, чтобы у 
других было больше возможностей для обучения.  Надеюсь, вам понравится.

Любовь,

Призраки



Перечисление
Базовый подсчет начинается со сканирования nmap. Nmap — это относительно сложная утилита, которая на протяжении 
многих лет совершенствовалась для определения того, какие порты открыты на устройстве, какие службы запущены и даже 
какая операционная система запущена. Важно отметить, что не все службы могут быть обнаружены правильно и не 
перечислены в полном объеме. Несмотря на то, что nmap — это слишком сложная утилита, она не может перечислить все. 
Поэтому после начального сканирования nmap мы будем использовать другие утилиты, которые помогут нам перечислить 
службы, запущенные на устройстве.

Более подробную информацию о nmap можно найти в комнате nmap.

Примечания :  Флаги для каждой учетной записи пользователя доступны для отправки. Вы можете получить флаги для 
учетных записей пользователей через RDP (Примечание: формат входа в систему — spookysec.local\User в приглашении на 
вход в Windows) и администратора через Evil-WinRM.  

### Ответьте на вопросы ниже
Какой инструмент позволит нам перечислить порт 139/445?
```commandline
enum4linux
```
Каково имя NetBIOS-домена машины?
```commandline
THM-AD
```
Какой недействительный TLD люди обычно используют для своего домена Active Directory?
```commandline
.local
```

## Задание 4
Введение:

Работает целый ряд других служб, включая Kerberos . Kerberos — это ключевая служба аутентификации в Active Directory. Открыв этот порт, мы можем использовать инструмент Kerbrute (автор Ронни Флэтерс @ropnop ) для обнаружения пользователей, паролей и даже паролей методом подбора!

Примечание: Несколько пользователей сообщили мне, что последняя версия Kerbrute не содержит флага UserEnum. Если это относится к выбранной вами версии, попробуйте более старую версию!

Перечисление:

Для этого поля будут использоваться измененные списки пользователей и паролей, чтобы сократить время перечисления пользователей и взлома хэша паролей. НЕ рекомендуется перебирать учетные данные из-за политик блокировки учетных записей, которые мы не можем перечислить на контроллере домена.

### Ответьте на вопросы ниже
Какая команда в Kerbrute позволит нам перечислить допустимые имена пользователей?
```commandline
userenum
```
Какой примечательный аккаунт обнаружен? (Это должно вам броситься в глаза)
```commandline
svc-admin
```
Какой еще примечательный аккаунт был обнаружен? (Они должны вам броситься в глаза)
```commandline
backup
```

## Задание 5
Введение

После завершения перечисления учетных записей пользователей мы можем попытаться злоупотребить функцией в Kerberos с 
помощью метода атаки, называемого  ASREPRoasting. ASReproasting происходит, когда для учетной записи пользователя 
установлена привилегия «Не требуется предварительная аутентификация». Это означает, что учетной записи  не нужно 
предоставлять действительную идентификацию перед запросом билета Kerberos для указанной учетной записи пользователя.    

Получение билетов Kerberos

У Impacket  есть инструмент под названием "GetNPUsers.py" (расположенный в impacket/examples/GetNPUsers.py), который 
позволит нам запрашивать учетные записи ASReproastable из Key Distribution Center. Единственное, что необходимо для 
запроса учетных записей, — это действительный набор имен пользователей, которые мы перечислили ранее через Kerbrute.  

Помните:   Impacket также может потребовать от вас использовать версию Python >=3.7. В AttackBox вы можете сделать 
это, запустив команду с `python3.9 /opt/impacket/examples/GetNPUsers.py`. 

### Ответьте на вопросы ниже
У нас есть две учетные записи пользователей, из которых мы потенциально можем запросить тикет. Из какой учетной 
записи пользователя можно запросить тикет без пароля? 
```commandline
svc-admin
```
Глядя на страницу Wiki Hashcat Examples, какой тип хеша Kerberos мы получили из KDC? (Укажите полное имя)
```commandline
Kerberos 5 AS-REP etype 23
```
Какой режим хэширования?
```commandline
18200
```
Теперь взломайте хеш с помощью предоставленного списка измененных паролей. Какой пароль у учетных записей пользователей?
```commandline
management2005
```
## Задание 6
Перечисление:

С учетными данными пользователя мы теперь имеем значительно больше доступа в домене. Теперь мы можем попытаться перечислить любые акции, которые контроллер домена может выдавать.

### Ответьте на вопросы ниже
Какую утилиту можно использовать для сопоставления удаленных SMB-ресурсов?
```commandline
smbclient
```
Какой вариант будет листинговать акции?
```commandline
-L
```
Сколько удаленных общих ресурсов размещено на сервере?
```commandline
6
```
Есть один конкретный ресурс, к которому у нас есть доступ, содержащий текстовый файл. Какой это ресурс?
```commandline
backup
```
Каково содержание файла?
```commandline
YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw
```
Расшифруем содержимое файла, каково его полное содержимое?
```commandline
backup@spookysec.local:backup2517860
```

## Задание 7
Давайте синхронизируемся!

Теперь, когда у нас есть новые учетные данные пользователя, у нас может быть больше привилегий в системе, чем раньше.
Имя пользователя учетной записи "backup" заставляет нас задуматься. Для чего эта учетная запись резервного 
копирования?  

Ну, это резервная учетная запись для контроллера домена. Эта учетная запись имеет уникальное разрешение, которое 
позволяет синхронизировать все изменения Active Directory с этой учетной записью пользователя. Это включает хэши 
паролей  



Зная это, мы можем использовать другой инструмент в Impacket под названием "secretsdump.py". Это позволит нам 
извлечь все хэши паролей, которые может предложить эта учетная запись пользователя (синхронизированная с 
контроллером домена). Используя это, мы фактически получим полный контроль над доменом AD.

### Ответьте на вопросы ниже
Какой метод позволил нам сделать дамп NTDS.DIT?
```commandline
DRSUAPI
```
Что такое NTLM-хэш администратора?
```commandline
0e0363213e37b94221497260b0bcb4fc
```
Какой метод атаки позволит нам аутентифицироваться как пользователь без пароля?
```commandline
Pass The Hash
```
Какая опция инструмента Evil-WinRM позволит нам использовать хэш?
```commandline
-H
```

## Задание 8
Группа подачи флагов

Отправьте флаги для каждой учетной записи пользователя. Они могут быть расположены на рабочем столе каждого пользователя.

Если вам понравилась эта статья, вам также может понравиться мой пост в блоге!

### Ответьте на вопросы ниже
svc-администратор
```commandline
TryHackMe{K3rb3r0s_Pr3_4uth}
```
резервное копирование
```commandline
TryHackMe{B4ckM3UpSc0tty!}
```
Администратор
```commandline
TryHackMe{4ctiveD1rectoryM4st3r}
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)