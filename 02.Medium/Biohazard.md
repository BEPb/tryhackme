

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Biohazard](https://tryhackme.com/r/room/biohazard) 

Всего 5 заданий:
## Задание 1
Добро пожаловать в Biohazard room, CTF-игру в стиле головоломки. Собрать предмет, решить головоломку и избежать кошмара — вот ваш главный приоритет. Сможете ли вы выжить до конца?

Если у вас возникнут какие-либо вопросы, не стесняйтесь писать мне в Discord-канале.

### Ответьте на вопросы ниже
Разверните машину и начните кошмар.
```commandline
Ответ не нужен
```
Сколько открытых портов?
```commandline
nmap -sSVC -p- -oA nmap_full -v <IP>
```
```commandline
3
```
Как называется команда, которая действует?
```commandline
vim /etx/hosts
<IP> biohazard.thm
curl http://biohazard.thm
```
```commandline
STARS alpha team
```

## Задание 2
Соберите все необходимые предметы и перейдите на следующий уровень. Формат флага предмета:

Имя_элемента{32 символа}

Некоторые двери заперты. Используйте флаг предмета, чтобы открыть дверь.

Советы: лучше записывать всю информацию в блокнот.

### Ответьте на вопросы ниже
Что такое эмблема флага
```commandline
curl http://biohazard.thm/mansionmain/
curl http://biohazard.thm/diningRoom/
printf %s SG93IGFib3V0IHRoZSAvdGVhUm9vbS8= | base64 -d
# How about the /teaRoom/
curl http://biohazard.thm/teaRoom/ 
curl http://biohazard.thm/teaRoom/master_of_unlock.html 
http://biohazard.thm/diningRoom/emblem.php
```
```commandline
emblem{fec832623ea498e20bf4fe1821d58727}
```
Что такое флаг отмычки?
```commandline
curl http://biohazard.thm/teaRoom/ 
curl http://biohazard.thm/teaRoom/master_of_unlock.html 
```
```commandline
lock_pick{037b35e2ff90916a9abf99129c8e1837}
```
Что такое флаг нотной записи?
```commandline
curl http://biohazard.thm/artRoom/ 
curl http://biohazard.thm/artRoom/MansionMap.html
http://biohazard.thm/barRoom/ + lock_pick{037b35e2ff90916a9abf99129c8e1837}
curl http://biohazard.thm/barRoom357162e3db904857963e6e0b64b96ba7/
http://biohazard.thm/barRoom357162e3db904857963e6e0b64b96ba7/musicNote.html
printf %s 'NV2XG2LDL5ZWQZLFOR5TGNRSMQ3TEZDFMFTDMNLGGVRGIYZWGNSGCZLDMU3GCMLGGY3TMZL5' | base32 -d
```
```commandline
music_sheet{362d72deaf65f5bdc63daece6a1f676e}
```
Что такое золотой флаг-эмблема?
```commandline
http://biohazard.thm/barRoom357162e3db904857963e6e0b64b96ba7/barRoomHidden.php + music_sheet{362d72deaf65f5bdc63daece6a1f676e}
http://biohazard.thm/barRoom357162e3db904857963e6e0b64b96ba7/gold_emblem.php
```
```commandline
gold_emblem{58a8c41a9d08b8a4e38d02a4d7ff4843}
```
Что такое флаг ключа щита?
```commandline
http://biohazard.thm/diningRoom/ + gold_emblem{58a8c41a9d08b8a4e38d02a4d7ff4843}
http://biohazard.thm/diningRoom/emblem_slot.php
http://biohazard.thm/diningRoom/the_great_shield_key.html
```
```commandline
shield_key{48a7a9227cd7eb89f0a062590798cbac}
```
Что такое флаг «Голубая жемчужина»?
```commandline
curl http://biohazard.thm/diningRoom2F/
ctf-party 'Lbh trg gur oyhr trz ol chfuvat gur fgnghf gb gur ybjre sybbe. Gur trz vf ba gur qvavatEbbz svefg sybbe. Ivfvg fnccuver.ugzy' rot13
http://biohazard.thm/diningRoom/sapphire.html
```
```commandline
blue_jewel{e1d457e96cac640f863ec7bc475d48aa}
```
Какое имя пользователя FTP?
```commandline
echo "RlRQIHVzZXI6IGh1bnRlciwgRlRQIHBhc3M6IHlvdV9jYW50X2hpZGVfZm9yZXZlcg==" | base64 -d
```
```commandline
hunter
```
Какой пароль FTP?
```commandline
you_cant_hide_forever
```

## Задание 3
Получив доступ к FTP- серверу, вам предстоит решить еще одну головоломку.

### Ответьте на вопросы ниже
Где находится скрытый каталог, упомянутый Барри?
```commandline
ftp biohazard.thm
ls
exiftool ftp/001-key.jpg
exiftool -Comment ftp/002-key.jpg 
exiftool -Comment ftp/003-key.jpg
steghide extract -sf ftp/001-key.jpg 
cat key-001.txt
# cGxhbnQ0Ml9jYW
binwalk -e ftp/003-key.jpg
cat ftp/_003-key.jpg-1.extracted/key-003.txt 
# 3aXRoX3Zqb2x0
printf %s cGxhbnQ0Ml9jYW5fYmVfZGVzdHJveV93aXRoX3Zqb2x0 | base64 -d
gpg helmet_key.txt.gpg 
```
```commandline
/hidden_closet/
```
Пароль для зашифрованного файла
```commandline
plant42_can_be_destroy_with_vjolt
```
Что такое флаг ключа шлема?
```commandline
helmet_key{458493193501d2b94bbab2e727f8db4b}
```

## Задание 4
Закончили с головоломкой? Есть места, которые вы уже исследовали, но еще не посетили.

### Ответьте на вопросы ниже
Какое имя пользователя для входа в SSH?
```commandline
umbrella_guest
```
Какой пароль для входа в SSH?
```commandline
T_virus_rules
```
Кто лидер команды STARS Bravo?
```commandline
Enrico
```

## Задание 5
Время для финальной схватки. Сможете ли вы избежать кошмара?

### Ответьте на вопросы ниже
Где вы нашли Криса?
```commandline
jailcell
```
Кто предатель?
```commandline
weasker
```
Пароль для входа предателя
```commandline
stars_members_are_my_guinea_pig
```
Название конечной формы
```commandline
Tyrant
```
Корневой флаг
```commandline
3c5794a00dc56c35f2bf096571edf3bf
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)