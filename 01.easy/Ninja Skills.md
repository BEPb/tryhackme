[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Ninja Skills](https://tryhackme.com/r/room/ninjaskills) 

Всего 1 заданиe:
## Задание 1
Давайте повеселимся с Linux. Разверните машину и начнем.

Настройка этого устройства может занять до 3 минут.

(Если вы предпочитаете подключиться к машине по SSH, используйте учетные данные new-user в качестве имени 
пользователя и пароля)

Ответьте на вопросы по следующим файлам:
- 8V2L
- bny0
- c4ZX
- D8B3
- FHl1
- oiMO
- PFbD
- rmfX
- SRSq
- uqyw
- v2Vb
- X1Uy
Цель — ответить на вопросы как можно эффективнее.

### Ответьте на вопросы ниже
Какой из перечисленных файлов принадлежит группе best-group (введите ответ через пробел в алфавитном порядке)
```commandline
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) 2>/dev/null
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -l {} \; 2>/dev/null
```
```commandline
D8B3 v2Vb
```
Какой из этих файлов содержит IP-адрес?
```commandline
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec grep -E -o “([0–9]{1,3}[\.]){3}[0–9]{1,3}” * {} \; 2>/dev/null
```
```commandline
oiMO
```
Какой файл имеет хэш SHA1 9d54da7584015647ba052173b84d45e8007eba94
```commandline
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec sha1sum {} \; 2>/dev/null
```
```commandline
c4ZX
```
Какой файл содержит 230 строк?
```commandline
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec wc -l {} \; 2>/dev/null
```
```commandline
bny0
```
Владелец какого файла имеет идентификатор 502?
```commandline
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -ln {} \; 2>/dev/null
```
```commandline
X1Uy
```
Какой файл может быть выполнен всеми?
```commandline
find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiM0 -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -l {} \; 2>/dev/null
```
```commandline
8V2L
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)