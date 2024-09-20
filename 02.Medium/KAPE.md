[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [KAPE](https://tryhackme.com/r/room/kape) 

Всего 8 заданий:
## Задание 1
Возвращаясь к Windows Forensics
В комнатах Windows Forensics 1 и Windows Forensics 2 мы узнали о различных артефактах, которые хранят информацию о 
действиях пользователя в системе. Мы также узнали, где находятся эти артефакты и как к ним можно получить доступ и 
интерпретировать их. Однако мы делали все это вручную. Во многих случаях судебный следователь не может позволить 
себе роскошь выполнять ручной анализ, который может занять много времени. В таких сценариях полезно иметь некоторые 
инструменты, помогающие автоматизировать сбор, очистку и обработку доказательств.

Цели обучения:
В этой комнате мы:

- Узнайте о КАПЭ
- Как работает КАПЭ
- Различные цели и модули, используемые KAPE
- Сбор и анализ криминалистических данных с использованием КАПЭ
### Ответьте на вопросы ниже
Я уже закончил занятия по курсам Windows Forensics 1 и Windows Forensics 2.
```commandline
Ответ не нужен
```

## Задание 2
Введение в КАПЭ:
Kroll Artifact Parser and Extractor (KAPE) анализирует и извлекает артефакты криминалистики Windows. Это 
инструмент, который может значительно сократить время, необходимое для реагирования на инцидент, предоставляя 
артефакты криминалистики из работающей системы или устройства хранения данных намного раньше, чем завершится процесс 
создания образа.

KAPE служит двум основным целям: 1) собирать файлы и 2) обрабатывать собранные файлы в соответствии с 
предоставленными опциями. Для достижения этих целей KAPE использует концепцию целей и модулей. Цели можно определить 
как криминалистические артефакты, которые необходимо собрать. Модули — это программы, которые обрабатывают собранные 
артефакты и извлекают из них информацию. Мы узнаем о них в следующих задачах.

### Как это работает
KAPE является расширяемым и высоконастраиваемым. По сути, двоичный файл KAPE собирает файлы и обрабатывает их в 
соответствии с предоставленной конфигурацией.

Коллекция файлов (целей) KAPE добавляет файлы в очередь и копирует их в два прохода. В первом проходе он копирует 
файлы, которые может. Это работает для файлов, которые ОС не заблокировала. Остальные файлы передаются во вторичную 
очередь. Вторичная очередь обрабатывается с использованием другой техники, которая использует необработанные чтения 
с диска для обхода блокировок ОС и копирования файлов. Скопированные файлы сохраняются с исходными временными 
метками и метаданными и хранятся в аналогичной структуре каталогов.

После сбора данных KAPE может обрабатывать их с помощью модулей. Модули могут быть независимыми двоичными файлами, 
которые работают с собранными данными и обрабатывают их для извлечения информации. Например, KAPE соберет и 
скопирует файл Prefetch в наше целевое место назначения во время сбора данных. Запуск модуля Prefetch Parser (PECmd) 
на этой цели извлечет файл prefetch и сохранит его в файле CSV.


Как показано на изображении выше, KAPE может извлекать цели из Live-системы, смонтированного образа или утилиты 
F-response. KAPE не требует установки. Он портативен и может использоваться из сетевых расположений или 
USB-накопителей. Чтобы продолжить, нажмите кнопку Start Machine в правом верхнем углу, чтобы запустить подключенную 
виртуальную машину в режиме разделенного экрана. Кроме того, вы можете войти в машину, используя следующие учетные 
данные:

Имя пользователя : thm-4n6
Пароль : 123

В прикрепленной виртуальной машине вы найдете KAPE на рабочем столе в папке с названием KAPE. В этой папке вы 
найдете следующие файлы и каталоги:

В этом каталоге вы можете увидеть два двоичных файла, kape.exe и gkape.exe. Первый — это CLI-версия KAPE, а второй — 
GUI-версия (обозначается префиксом 'g').

gkape.settings хранит настройки по умолчанию для версии GUI.

Get-KAPEUpdate.ps1, как следует из названия, — это скрипт Powershell, который проверяет и загружает обновления.

ChangeLog.txt и Documentation говорят сами за себя. Мы рассмотрим Targets и Modules в следующих задачах.

### Ответьте на вопросы ниже
Какой двоичный файл из kape.exe и gkape.exe используется для запуска графической версии KAPE?
```commandline
gkape.exe
```

## Задание 3
В лексиконе KAPE, Targets это артефакты, которые необходимо собрать из системы или образа и скопировать в указанное 
нами место назначения. Например, как мы узнали в последней комнате, Windows Prefetch — это криминалистический 
артефакт для доказательства выполнения, чтобы мы могли создать Target для него. Аналогично, мы также можем создать  
Targets для кустов реестра. Короче говоря, Targets копировать файлы из одного места в другое.

Когда мы откроем Targets каталог KAPE, вот что мы увидим:

Последние четыре файла внизу — это руководства и шаблоны для создания Targets и Compound Targets наши собственные. Мы 
обсудим это Compound Targets позже в этой задаче. Как вы видите, цели сгруппированы в разные каталоги. Давайте 
проверим каталог, Windows чтобы увидеть, что у нас есть:

Мы можем видеть различные файлы расширения .tkape. Вот как Target определяется a для KAPE. Файл TKAPE содержит 
информацию об артефакте, который мы хотим собрать, например, путь, категорию и маски файлов для сбора. В качестве 
примера ниже показано, как Target определяется Prefetch.

Этот файл TKAPE сообщает KAPE о необходимости сбора файлов с файловой маской *.pfиз указанного пути 
`C:\Windows\prefetch` и `C:\Windows.old\prefetch`. 

Обратите внимание, что C:\Windows.oldздесь также указан путь. Этот путь содержит файлы, сохраненные после обновления 
Windows до новой версии. Для судебно-медицинского анализа мы также можем найти интересные исторические артефакты из 
этого каталога.

Комплексные цели:
KAPE также поддерживает Compound Targets. Это те Targets, которые являются соединениями нескольких других целей. Как 
упоминалось в предыдущих задачах, KAPE часто используется для быстрого сбора и анализа сортировки. Цель KAPE не 
будет достигнута, если нам придется собирать каждый артефакт по отдельности. Поэтому Compound Targetsпомогите нам 
собрать несколько целей, дав одну команду. Примеры Compound Targetsвключают !BasicCollection, !SANS_triageи 
KAPEtriage. Мы можем просмотреть Compound Targetsна пути KAPE\Targets\Compound. На следующем изображении показано, 
как Compound Targetвыглядит для доказательства выполнения:

Вышеуказанная команда Compound Target соберет доказательства выполнения из Prefetch, RecentFileCache, AmCache и 
Syscache Targets.

!Неполноценный
В этом каталоге содержатся Targetsобъекты, которые вы хотите сохранить в экземпляре KAPE, но не хотите, чтобы они 
отображались в списке активных целей. 

!Местный
Если вы создали что-то Targets, что не хотите синхронизировать с репозиторием KAPE Github, вы можете поместить их в 
этот каталог. Это могут быть Targets те, которые специфичны для вашей среды. Аналогично, все, чего нет в репозитории 
Github, когда мы обновляем KAPE, будет перемещено в этот !Local каталог.

### Ответьте на вопросы ниже
Какое расширение файла у KAPE Targets?
```commandline
.tkape
```
Какой тип  Targetволи мы используем, если хотим собрать несколько артефактов с помощью одной команды?
```commandline
Compound Targets
```

## Задание 4
Modules, в лексиконе KAPE, запускать определенные инструменты для предоставленного набора файлов. Их цель не 
копировать файлы из одного места в другое, а скорее запустить некоторую команду и сохранить вывод. Обычно вывод 
имеет форму файлов CSV или TXT.

Вот как Modulesвыглядит каталог в KAPE :

Подобно предыдущей задаче, мы видим руководства и шаблоны для создания Modulesи Compound Modules. Мы также видим 
каталоги !Disabled, !Localи Compound, которые похожи на те, что мы видели в предыдущей задаче. Мы не будем обсуждать 
их снова, так как мы обсуждали их в последней задаче. Мы видим, что большинство из них Modulesсгруппированы вместе в 
разных каталогах. Единственное, что мы находим отличающимся, это binкаталог. Мы обсудим это немного позже. А пока 
давайте откроем каталог Windows и посмотрим, что у нас там есть:

Здесь мы видим файлы с .mkape расширением. Они распознаются ModulesKAPE как. Давайте откроем файл MKAPE и посмотрим, 
как он структурирован. На следующем изображении показан файл Windows_IPConfig MKAPE.

Обратите внимание, что файл MKAPE сообщает KAPE об исполняемом файле, который должен быть запущен, параметрах 
командной строки исполняемого файла, формате экспорта выходных данных и имени файла для экспорта. Но что, если 
исполняемый файл, который мы хотим запустить, отсутствует в системе? Это приводит нас к bin каталогу.  

Каталог bin:
Каталог binсодержит исполняемые файлы, которые мы хотим запустить в системе, но которые изначально не присутствуют в 
большинстве систем. KAPE будет запускать исполняемые файлы либо из bin каталога, либо по полному пути. Примером 
файлов, которые следует хранить в bin каталоге, являются инструменты Эрика Циммермана, которые, как правило, 
отсутствуют в системе Windows. Мы широко использовали их в комнатах Windows Forensics.

Обратите внимание, что большинство представленных здесь двоичных файлов взяты из Tools Эрика Циммермана.

### Ответьте на вопросы ниже
Какое расширение у файлов Modules?
```commandline
.mkape
```
Как называется каталог, в котором хранятся двоичные файлы, которые могут отсутствовать в типичной системе, но 
требуются для конкретного модуля KAPE?
```commandline
bin
```

## Задание 5
Теперь, когда мы узнали о различных компонентах KAPE, давайте проведем тест-драйв. В прикрепленной виртуальной 
машине дважды щелкните, чтобы открыть файл gkape.exe. Вы увидите следующее окно:

Совет: если окно не отображается должным образом на разделенном экране, вы можете открыть его в полной вкладке 
браузера, нажав эту кнопку:

Здесь вы можете видеть, что есть разные опции, но большинство из них отключены. Чтобы собрать Targets Мы продолжим, 
включив  Use Target Options флажок. Это включит опции, присутствующие в левой половине окна:

Если мы хотим провести экспертизу на той же машине, на которой запущен KAPEC:\ , мы предоставим целевой источник. Мы 
можем выбрать целевой пункт назначения по нашему выбору. Все файлы сортировки будут скопированы в целевой пункт 
назначения, который мы предоставим.

Здесь Flush флажок удалит все содержимое целевого назначения, поэтому мы должны быть осторожны при его использовании.
Мы отключили флажок, Flush чтобы он не удалял данные, уже имеющиеся в каталогах.  Add %d добавит информацию о дате к 
имени каталога, в котором сохраняются собранные данные. Аналогично, Add %m добавит информацию о машине в целевой 
каталог назначения. Мы можем выбрать желаемый Target из списка, показанного выше. Панель поиска помогает нам быстро 
искать имена желаемых Target.

Мы можем выбрать, хотим ли мы обрабатывать теневые копии томов, включив Process VSCs. Мы можем установить 
transfer флажок, если хотим передавать собранные артефакты через сервер SFTP или контейнер S3. Для передачи файлы 
должны быть заключены в контейнер, который может быть Zip, VHD или VHDX. Аналогично, мы можем предоставить 
исключения на основе SHA-1, и KAPE не будет копировать исключенные файлы. При заключении в контейнер нам нужно будет 
указать, Base name который будет использоваться для всех созданных файлов. Это не требуется, если мы не передаем 
файлы или не заключаем их в контейнер.

На Current command line вкладке мы можем видеть, как добавляются или удаляются параметры командной строки при 
настройке пользовательского интерфейса. Это окно будет показывать больше параметров в командной строке по мере 
добавления параметров. Обратите внимание, что путь назначения в вашем случае будет отличаться от показанного на 
изображении. Обратите внимание на --tflush флаг здесь. Он означает, что при создании этой командной строки 
Flush флажок все еще был отмечен.

При установке флажка «Использовать параметры модуля» правая сторона окна KAPE также будет включена.

При использовании как Target, так и Module Options предоставление Module Source не требуется. Выбранные модули будут 
использовать Target destination в качестве источника.

Остальные параметры модулей аналогичны параметрам целей, поэтому мы не будем вдаваться в подробности.

Ниже вы увидите, как выглядит конфигурация, когда KAPE полностью настроен для сбора целей и их обработки с 
использованием модулей.

Мы выбрали KapeTriage составной Target и !EZParser составной Module. В командной строке ниже показана команда CLI, 
которая будет запущена. Execute! Кнопка в правом нижнем углу выполнит команду. Disable flush warnings Флажок под ней 
не будет предупреждать нас, когда мы используем Flush флаги. Когда мы нажмем Execute!Мы увидим, что откроется окно 
командной строки и покажем нам журналы, пока KAPE выполняет свои задачи. Выполнение займет несколько минут, так как 
он соберет все данные, а затем запустит на них процессы модуля. После завершения он покажет нам общее время 
выполнения, и мы можем нажать любую клавишу, чтобы закрыть командное окно.
```commandline
D:\Kape\kape.exe
KAPE version 1.1.0.1 Author: Eric Zimmerman (kape@kroll.com)

KAPE directory: D:\KAPE
Command line: --tsource C: --tdest C:\Users\Umair\Desktop\kape --target KapeTriage --mdest C:\Users\Umair\Desktop\4n6-2 --module !EZParser --gui

System info: Machine name: UMAIR-THINKBOOK, 64-bit: True, User: Umair OS: Windows10 (10.0.22000)

Using Target operations
Found 14 targets. Expanding targets to file list...
Target 'ApplicationEvents' with Id '2da16dbf-ea47-448e-a00f-fc442c3109ba' already processed. Skipping!
Target 'ApplicationEvents' with Id '2da16dbf-ea47-448e-a00f-fc442c3109ba' already processed. Skipping!
Target 'ApplicationEvents' with Id '2da16dbf-ea47-448e-a00f-fc442c3109ba' already processed. Skipping!
Target 'ApplicationEvents' with Id '2da16dbf-ea47-448e-a00f-fc442c3109ba' already processed. Skipping!
Target 'ApplicationEvents' with Id '2da16dbf-ea47-448e-a00f-fc442c3109ba' already processed. Skipping!
Found 3,059 files in 4.257 seconds. Beginning copy...
        Deferring 'C:\Windows\System32\winevt\logs\Application.evtx' due to IOException...
        Deferring 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4Operational.evtx' due to IOException...
        Deferring 'C:\Windows\System32\winevt\Logs\Microsoft-Windows-Windows Defender%4WHC.evtx' due to IOException...
        Deferring 'C:\ProgramData\Microsoft\Windows Defender\Support\MPDetection-20220126-183133.log' due to IOException...
        Deferring 'C:\ProgramData\Microsoft\Windows Defender\Support\MPDeviceControl-20211016-164735.log' due to IOException...
        Deferring 'C:\ProgramData\Microsoft\Windows Defender\Support\MPLog-10172021-040927.log' due to IOException...
        Deferring 'C:\ProgramData\Microsoft\Windows Defender\Support\MpWppTracing-20220210-070038-00000003-ffffffff.bin' due to IOException...
        Deferring 'C:\Windows\System32\winevt\logs\HardwareEvents.evtx' due to IOException...
        Deferring 'C:\Windows\System32\winevt\logs\IntelAudioServiceLog.evtx' due to IOException...
        Deferring 'C:\Windows\System32\winevt\logs\Internet Explorer.evtx' due to IOException...
.
.
.
.
Executing remaining modules...
        Running 'EvtxECmd\EvtxECmd.exe': -d C:\Users\Umair\Desktop\kape --csv C:\Users\Umair\Desktop\4n6-2\EventLogs
        Running 'JLECmd.exe': -d C:\Users\Umair\Desktop\kape --csv C:\Users\Umair\Desktop\4n6-2\FileFolderAccess -q
        Running 'LECmd.exe': -d C:\Users\Umair\Desktop\kape --csv C:\Users\Umair\Desktop\4n6-2\FileFolderAccess -q
        Running 'PECmd.exe': -d C:\Users\Umair\Desktop\kape --csv C:\Users\Umair\Desktop\4n6-2\ProgramExecution -q
        Running 'RBCmd.exe': -d C:\Users\Umair\Desktop\kape --csv C:\Users\Umair\Desktop\4n6-2\FileDeletion -q
        Running 'RECmd\RECmd.exe': -d C:\Users\Umair\Desktop\kape --bn BatchExamples\Kroll_Batch.reb --nl false --csv C:\Users\Umair\Desktop\4n6-2\Registry -q
        Running 'SBECmd.exe': -d C:\Users\Umair\Desktop\kape --csv C:\Users\Umair\Desktop\4n6-2\FileFolderAccess -q
        Running 'SQLECmd\SQLECmd.exe': -d C:\Users\Umair\Desktop\kape --csv C:\Users\Umair\Desktop\4n6-2\SQLDatabases
        Running 'SrumECmd.exe': -d C:\Users\Umair\Desktop\kape -k --csv C:\Users\Umair\Desktop\4n6-2\SystemActivity
        Running 'SumECmd.exe': -d C:\Users\Umair\Desktop\kape\Windows\System32\LogFiles\SUM --csv C:\Users\Umair\Desktop\4n6-2\SUMDatabase
Executed 18 processors in 192.2738 seconds

Total execution time: 258.1812 seconds


Press any key to exit
```
Обратите внимание, что на бэкэнде KAPE работает kape.exe в командной строке. Мы можем проверить файлы, созданные KAPE 
, как только он завершит их обработку. На снимке ниже показан наш Module destination. Обратите внимание, как KAPE 
обработал файлы в соответствии с различными категориями.

Давайте соберем данные сортировки с помощью  KAPETriage пакета, обработаем их с помощью !EZParser модуля и ответим на 
вопросы ниже. Затем мы можем перейти к изучению KAPE CLI в следующем задании.

### Ответьте на вопросы ниже
Какую цель мы выбрали для сбора на предпоследнем скриншоте выше?
```commandline
KapeTriage
```

Какой модуль мы выбрали для обработки на предпоследнем снимке экрана выше?
```commandline
!EZParser
```
Какую опцию необходимо выбрать, чтобы добавить информацию о дате и времени к имени папки сортировки?
```commandline
%d
```
Какую опцию необходимо выбрать, чтобы добавить информацию о машине в имя папки сортировки?
```commandline
%m
```
## Задание 6
Хотя мы использовали GUI в предыдущей задаче, KAPE — это инструмент командной строки. Поэтому, чтобы в полной мере 
использовать KAPE, важно знать, как использовать его через командную строку.

Для получения списка всех различных переключателей, которые можно использовать с KAPE, откройте PowerShell с 
повышенными правами (запуск от имени администратора), перейдите по пути, где находится двоичный файл KAPEkape.exe, 
и введите. Вы увидите что-то вроде этого в качестве вывода.

Администратор: Командная строка
```commandline
D:\KAPE>kape.exe

KAPE version 1.1.0.1 Author: Eric Zimmerman (kape@kroll.com)

        tsource         Target source drive to copy files from (C, D:, or F:\ for example)
        target          Target configuration to use
        tdest           Destination directory to copy files to. If --vhdx, --vhd or --zip is set, files will end up in VHD(X) container or zip file
        tlist           List available Targets. Use . for Targets directory or name of subdirectory under Targets.
        tdetail         Dump Target file details
        tflush          Delete all files in 'tdest' prior to collection
        tvars           Provide a list of key:value pairs to be used for variable replacement in Targets. Ex: --tvars user:eric would allow for using %user% in a Target which is replaced with eric at runtime. Multiple pairs should be separated by ^
        tdd             Deduplicate files from --tsource (and VSCs, if enabled) based on SHA-1. First file found wins. Default is TRUE

        msource         Directory containing files to process. If using Targets and this is left blank, it will be set to --tdest automatically
        module          Module configuration to use
        mdest           Destination directory to save output to
        mlist           List available Modules. Use . for Modules directory or name of subdirectory under Modules.
        mdetail         Dump Module processors details
        mflush          Delete all files in 'mdest' prior to running Modules
        mvars           Provide a list of key:value pairs to be used for variable replacement in Modules. Ex: --mvars foo:bar would allow for using %foo% in a module which is replaced with bar at runtime. Multiple pairs should be separated by ^
        mef             Export format (csv, html, json, etc.). Overrides what is in Module config

        sim             Do not actually copy files to --tdest. Default is FALSE
        vss             Process all Volume Shadow Copies that exist on --tsource. Default is FALSE

        vhdx            The base name of the VHDX file to create from --tdest. This should be an identifier, NOT a filename. Use this or --vhd or --zip
        vhd             The base name of the VHD file to create from --tdest. This should be an identifier, NOT a filename. Use this or --vhdx or --zip
        zip             The base name of the ZIP file to create from --tdest. This should be an identifier, NOT a filename. Use this or --vhdx or --vhd

        scs             SFTP server host/IP for transferring *compressed VHD(X)* container
        scp             SFTP server port. Default is 22
        scu             SFTP server username. Required when using --scs
        scpw            SFTP server password
        scd             SFTP default directory to upload to. Will be created if it does not exist
        scc             Comment to include with transfer. Useful to include where a transfer came from. Defaults to the name of the machine where KAPE is running

        s3p             S3 provider name. Example: spAmazonS3 or spGoogleStorage. See 'https://bit.ly/34s9nS6' for list of providers. Default is 'spAmazonS3'
        s3r             S3 region name. Example: us-west-1 or ap-southeast-2. See 'https://bit.ly/3aNxXhc' for list of regions by provider
        s3b             S3 bucket name
        s3k             S3 Access key
        s3s             S3 Access secret
        s3st            S3 Session token
        s3kp            S3 Key prefix. When set, this value is used as the beginning of the key. Example: 'US1012/KapeData'
        s3o             When using 'spOracle' provider, , set this to the 'Object Storage Namespace' to use
        s3c             Comment to include with transfer. Useful to include where a transfer came from. Defaults to the name of the machine where KAPE is running

        s3url           S3 Presigned URL. Must be a PUT request vs. a GET request

        asu             Azure Storage SAS Uri
        asc             Comment to include with transfer. Useful to include where a transfer came from. Defaults to the name of the machine where KAPE is running

        zv              If true, the VHD(X) container will be zipped after creation. Default is TRUE
        zm              If true, directories in --mdest will be zipped. Default is FALSE
        zpw             If set, use this password when creating zip files (--zv | --zm | --zip)

        hex             Path to file containing SHA-1 hashes to exclude. Only files with hashes not found will be copied

        debug           Show debug information during processing
        trace           Show trace information during processing

        gui             If true, KAPE will not close the window it executes in when run from gkape. Default is FALSE

        ul              When using _kape.cli, when true, KAPE will execute entries in _kape.cli one at a time vs. in parallel. Default is FALSE

        cu              When using _kape.cli, if true, KAPE will delete _kape.cli and both Target/Module directories upon exiting. Default is FALSE

        sftpc           Path to config file defining SFTP server parameters, including port, users, etc. See documentation for examples
        sftpu           When true, show passwords in KAPE switches for connection when using --sftpc. Default is TRUE

        rlc             If true, local copy of transferred files will NOT be deleted after upload. Default is FALSE
        guids           KAPE will generate 10 GUIDs and exit. Useful when creating new Targets/Modules. Default is FALSE
        sync            If true, KAPE will download the latest Targets and Modules from specified URL prior to running. Default is https://github.com/EricZimmerman/KapeFiles/archive/master.zip

        ifw             If false, KAPE will warn if a process related to FTK is found, then exit. Set to true to ignore this warning and attempt to proceed. Default is FALSE


        Variables: %d = Timestamp (yyyyMMddTHHmmss)
                   %s = System drive letter
                   %m = Machine name

Examples: kape.exe --tsource L: --target RegistryHives --tdest "c:\temp\RegistryOnly"
          kape.exe --tsource H --target EvidenceOfExecution --tdest "c:\temp\default" --debug
          kape.exe --tsource \\server\directory\subdir --target Windows --tdest "c:\temp\default_%d" --vhdx LocalHost
          kape.exe --msource "c:\temp\default" --module LECmd --mdest "c:\temp\modulesOut" --trace --debug

          Short options (single letter) are prefixed with a single dash. Long commands are prefixed with two dashes

          Full documentation: https://ericzimmerman.github.io/KapeDocs/


D:\KAPE>

```
Из скриншота выше видно, что при сборе Targets требуются переключатели tsource, target и . Аналогично, при обработке 
файлов с использованием Modules требуются переключатели и . Остальные переключатели являются необязательными в 
соответствии с требованиями сбора.tdestmodulemdest

Используя эту информацию, давайте создадим команду для выполнения той же задачи, которую мы выполнили в предыдущей 
задаче. т.е. соберем данные сортировки с помощью KapeTriageCompound Target и обработаем их с помощью !EZParser 
Compound Module. Поскольку мы не используем версию с графическим интерфейсом, мы начнем с ввода:
`kape.exe`
Чтобы добавить целевой источник, давайте добавим `--tsource` целевой путь:

`kape.exe --tsource C: `

Флаг --target будет использоваться для выбора Target флага --tdest для Target destination. Для простоты мы установим 
Target destination в каталог с именем target на рабочем столе. KAPE создаст новый каталог, если он еще не существует.
Наша командная строка теперь выглядит так:

`kape.exe --tsource C: --target KapeTriage --tdest C:\Users\thm-4n6\Desktop\target` 

Выполнение указанной выше команды соберет данные о сортировке, определенные в KapeTriage Target, и сохранит их в 
указанном месте назначения. Однако она не будет обрабатывать их или выполнять какие-либо другие действия с данными.

Если мы хотим очистить целевой пункт назначения, мы можем добавить --tflush, чтобы сделать это. Сейчас давайте 
перейдем к добавлению опций модуля. Если бы мы использовали источник модуля, мы бы использовали --msource флаг > 
аналогично флагу --tsource. Но в этом случае давайте используем целевой пункт назначения в качестве источника модуля.
Сделав это, нам не нужно будет добавлять его явно, и мы можем перейти к добавлению назначения модуля с помощью 
--mdest флага:

`kape.exe --tsource C: --target KapeTriage --tdest C:\Users\thm-4n6\Desktop\Target --mdest C:\Users\thm-4n6\Desktop\module`

Мы только что использовали каталог с именем module в качестве назначения модуля.

Чтобы обработать целевой пункт назначения с помощью модуля, нам нужно указать имя модуля с помощью --module флага. 
Чтобы обработать его с помощью !EZParser модуля, мы добавим --module !EZParser, сделав нашу команду такой:

`kape.exe --tsource C: --target KapeTriage --tdest C:\Users\thm-4n6\Desktop\Target --mdest C:\Users\thm-4n6\Desktop\module --module !EZParser`

Обратите внимание, что для сбора данных KAPE нам потребуется запустить эту команду в оболочке с повышенными 
привилегиями (с правами администратора).

Мы можем изменить команду в соответствии с нашими потребностями и переключателями, предоставленными KAPE . Когда мы 
запустим эту команду, мы увидим похожее окно, как в предыдущей задаче. Вы можете проверить файлы, собранные KAPE 
Targets and Modules, после ее завершения.

Пакетный режим:
KAPE также может быть запущен в пакетном режиме. Это означает, что мы можем предоставить список команд для запуска 
KAPE_kape.cli в файле с именем . Затем мы сохраняем этот файл в каталоге, содержащем двоичный файл KAPE . При kape.
exeзапуске от имени администратора он проверяет, есть ли _kape.cliфайл в каталоге. Если да, он выполняет команды, 
указанные в cli-файле. Этот режим можно использовать, если вам нужно, чтобы кто-то запустил KAPE для вас, вы 
сохраните все команды в одной строке, и все, что вам нужно, это чтобы человек щелкнул правой кнопкой мыши и запустил 
kape.exe от имени администратора. Например, если нам нужно выполнить ту же задачу, что и ранее в этой задаче, с 
использованием пакетного режима, нам нужно будет создать файл _kape.cli со следующим содержимым:
```commandline
--tsource C: --target KapeTriage --tdest C:\Users\thm-4n6\Desktop\Target --mdest C:\Users\thm-4n6\Desktop\module --module !EZParser
```
При запуске kape.exeон выполнит те же задачи, что и при запуске через CLI выше.

Давайте ответим на вопросы ниже и приготовимся применить наши новые навыки в следующем задании.

### Ответьте на вопросы ниже
Запустите команду kape.exeв оболочке с повышенными правами. Посмотрите на различные переключатели и переменные. 
Какая переменная добавляет временную метку коллекции к целевому месту назначения?
```commandline
%d
```
Какая переменная добавляет информацию о машине к целевому месту назначения?
```commandline
%m
```
Какой переключатель можно использовать для отображения отладочной информации во время обработки?
```commandline
debug
```
Какой переключатель используется для вывода списка всех доступных целей?
```commandline
tlist
```
Какой флаг при использовании в пакетном режиме удалит файлы _kape.cli, цели и модули после завершения выполнения?
```commandline
cu
```

## Задание 7
Итак, теперь, когда мы узнали, как использовать KAPE, давайте применим это на практике. Для этой задачи вам понадобится использовать свои навыки, полученные в этой комнате и в предыдущих комнатах Windows Forensics 1 и Windows Forensics 2 .

Организация X имеет Политику допустимого использования для своих портативных устройств, включая ноутбуки. Эта политика запрещает пользователям подключать съемные или сетевые диски, устанавливать программное обеспечение из неизвестных мест и подключаться к неизвестным сетям. Похоже, один из пользователей нарушил эту политику. Можете ли вы помочь Организации X выяснить, нарушил ли пользователь Политику допустимого использования на своем устройстве? Машина пользователя подключена к комнате как виртуальная машина .

Перейдите в каталог KAPE, размещенный на рабочем столе в подключенной виртуальной машине . Запустите KAPE с нужными параметрами Target и Module и ответьте на следующие вопросы.

Совет:  для открытия CSV-файлов можно использовать EZviewer, расположенный в папке EZtools на рабочем столе.

### Ответьте на вопросы ниже
К этой виртуальной машине подключены два USB-накопителя. У одного из них серийный номер 0123456789ABCDE. Какой серийный номер у другого USB-устройства?
```commandline
1C6F654E59A3B0C179D366AE
```
7zip, Google Chrome и Mozilla Firefox были установлены из сетевого диска на виртуальной машине. Какова была буква 
диска и путь к каталогу, из которого были установлены эти программы?
```commandline
Z:\Setups
```
Каковы дата и время выполнения CHROMESETUP.EXE в формате ММ/ДД/ГГГГ ЧЧ:ММ?
```commandline
11/25/2021 03:33
```
Какой поисковый запрос был выполнен в системе?
```commandline
RunWallpaperSetup.cmd
```
Когда была впервые подключена сеть под названием «Сеть 3»?
```commandline
11/30/2021 15:44
```
KAPE был скопирован со съемного диска. Можете ли вы узнать, какая буква была у диска, с которого был скопирован KAPE?
```commandline
E:
```

## Задание 8
Уф! Windows Forensics продолжает становиться интереснее. 

Вы можете остаться и узнать, какие еще интересные артефакты вы нашли в VM. Вы можете сообщить нам, что вы нашли 
интересного в этой комнате, используя наш канал Discord или аккаунт Twitter.

Кроме того, вы можете попробовать запустить KAPE на своем компьютере и посмотреть, какую информацию вы сможете найти. 

### Ответьте на вопросы ниже
Прочитайте выше
```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)