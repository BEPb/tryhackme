[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Sudo Security Bypass](https://tryhackme.com/r/room/sudovulnsbypass) 

Всего 2 задания:
## Задание 1
Для развертывания этой виртуальной машины вы должны быть подключены к сети TryHackMe с помощью файла конфигурации 
OpenVPN. Если вы не знаете, как это сделать, сначала быстро загляните в комнату OpenVPN. 

После подключения нажмите зеленую кнопку «Развернуть», чтобы запустить экземпляр машины, и мы можем приступить к работе!

(Обратите внимание, что полная загрузка виртуальных машин может занять несколько минут)

Для входа в машину вы будете использовать SSH. В Linux это делается из терминала командой, которая выглядит так:
```commandline
ssh -p <port-number> <username>@<remote-machine-ip>
```

В Windows вы обычно используете программное обеспечение, например  PuTTY. Затем вы входите в систему следующим образом:



Какой бы метод вы ни использовали, вам будет предложено ввести пароль, после ввода которого вы сможете удаленно 
выполнять команды на машине. 

### Ответить на вопросы ниже
Развернуто!
```commandline
Ответ не нужен
```

## Задание 2
CVE-2019-14287 — это уязвимость, обнаруженная в программе Sudo Unix исследователем, работающим в Apple: Джо 
Венниксом. По совпадению, он также нашел уязвимость, о которой мы поговорим в следующей комнате этой серии. Этот 
эксплойт с тех пор был исправлен, но все еще может присутствовать в старых версиях Sudo (версии < 1.8.28), поэтому 
на него стоит обратить внимание!

Для тех, кто может быть не знаком с ней: sudo — это команда в unix, которая позволяет вам запускать программы от 
имени других пользователей. Обычно это происходит по умолчанию для суперпользователя (root), но также возможно 
запускать программы от имени других пользователей, указав их имя пользователя или UID. Например, sudo обычно 
используется так: sudo <command>, но вы можете вручную выбрать выполнение от имени другого пользователя, например 
так:  sudo -u#<id> <command>. Это означает, что вы будете притворяться другим пользователем при выполнении выбранной 
команды, что может дать вам более высокие права, чем вы могли бы иметь в противном случае. Например:


В этом примере у моей учетной записи пользователя не было прав на чтение файла  /root/root.txt, поэтому я 
использовал sudo, чтобы временно предоставить себе права root для чтения файла. 

Как и многие команды в системах Unix, sudo можно настроить, отредактировав файл конфигурации в вашей системе. В этом 
случае этот файл называется  /etc/sudoers. Редактирование этого файла напрямую не рекомендуется из-за его важности 
для установки ОС, однако вы можете безопасно редактировать его с помощью команды  sudo visudo, которая проверяет при 
сохранении, чтобы убедиться в отсутствии неправильных конфигураций.   

Уязвимость, которая нас интересует для этой задачи, возникает в очень специфическом сценарии. Допустим, у вас есть 
пользователь, которому вы хотите предоставить дополнительные разрешения. Вы хотите разрешить этому пользователю 
выполнить программу, как если бы он был любым другим пользователем, но вы  не  хотите, чтобы он выполнил ее как root.
Вы можете добавить эту строку в файл sudoers:   
```commandline
<user> ALL=(ALL:!root) NOPASSWD: ALL
```

Это позволит вашему пользователю выполнить любую команду как другой пользователь, но (теоретически) не позволит ему 
выполнить команду как суперпользователь/администратор/рут. Другими словами, вы можете притвориться любым 
пользователем, кроме администратора.  

Теоретически.

На практике, используя уязвимые версии Sudo, вы можете обойти это ограничение и в любом случае запускать программы 
как root, что, очевидно, отлично подходит для повышения привилегий! 

С указанной выше конфигурацией использование  sudo -u#0 <command> (UID root всегда равен 0) не сработает, так как 
нам не разрешено выполнять команды как root. Если мы попытаемся выполнить команды как пользователь 0, мы получим 
ошибку. Введите  CVE -2019-14287.  

Джо Венникс обнаружил, что если указать UID -1 (или его беззнаковый эквивалент: 4294967295), Sudo неправильно 
прочтет это как 0 (т. е. root). Это означает, что, указав UID -1 или 4294967295, вы сможете выполнить команду как 
root,  несмотря на то, что вам явно запрещено это делать . Стоит отметить, что это  сработает только  в том случае, 
если вам были предоставлены не-root разрешения sudo для команды, как в конфигурации выше.    

На практике это применяется следующим образом: `sudo -u#-1 <command>`

#### Теперь твоя очередь.

Подключитесь по SSH к машине, которую вы развернули ранее, используя порт 2222.

Учетные данные следующие:

Имя пользователя:  tryhackme
Пароль:  tryhackme

Если вы используете Linux , команда будет выглядеть так:
```commandline
ssh -p 2222 tryhackme@MACHINE_IP
```

### Ответить на вопросы ниже
Какую команду разрешено запускать с помощью sudo?


```commandline
/bin/bash
```
Какой флаг в /root/root.txt?
```commandline
THM{l33t_s3cur1ty_bypass}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)