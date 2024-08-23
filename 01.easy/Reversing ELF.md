[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Reversing ELF](https://tryhackme.com/r/room/reverselfiles) 

Всего 8 заданий:
## Задание 1
Давайте начнем с базовой разминки. Сможете ли вы запустить исполняемый файл?

### Ответьте на вопросы ниже
Что такое флаг?
Используя команду file , я вижу, что это двоичный файл ELF. Используя команду chmod, сделать файл исполняемым,
а затем запустить двоичный файл ELF, чтобы получить флаг. 
```commandline
file crackme1
chmod +x crackme1
./crackme1
```
```commandline
flag{not_that_kind_of_elf}
```

## Задание 2
Найдите суперсекретный пароль! и используйте его, чтобы получить флаг
### Ответьте на вопросы ниже
Какой суперсекретный пароль?
В задании представлен двоичный файл ELF, для получения флага которого требуется пароль.
```commandline
file crackme2
strings crackme2
./crackme2 password
```
```commandline
super_secret_password
```
Что такое флаг?
```commandline
flag{if_i_submit_this_flag_then_i_will_get_points}
```

## Задание 3
Используйте базовые навыки обратного проектирования, чтобы получить флаг.

### Ответьте на вопросы ниже
Что такое флаг?
Предоставляется двоичный файл ELF, который требует пароль для извлечения флага. Пароль можно извлечь, используя тот 
же подход, что и в случае с crackme2, но с дополнительным шагом. Используя команду strings, я нашел строку в 
кодировке base64.
```commandline
chmod 777 crackme3
./crackme3
strings crackme3
echo “ZjByX3kwdXJfNWVjMG5kX2xlNTVvbl91bmJhc2U2NF80bGxfN2gzXzdoMW5nNQ==” | base64 -d
```
```commandline
f0r_y0ur_5ec0nd_le55on_unbase64_4ll_7h3_7h1ng5
```

## Задание 4
Проанализировать и найти пароль к двоичному файлу?

### Ответьте на вопросы ниже
Какой пароль?
```commandline
chmod 777 crackme4
./crackme3
r2 -d ./crackme4
```
- Проанализируйте программу - `ааа`
- списки функций - `afl`
- есть основная функция `pdf @main`
- Это похоже на функцию сравнения `pdf @main`
- Установить точку останова база 
```commandline
db 0x004006d5
ood ‘argement’
```
- Выполнить до точки останова
```commandline
dc
pdf @sym.compare_pwd
```
Давайте проверим значение
```commandline
px @rdi
```
```commandline
my_m0r3_secur3_pwd
```

## Задание 5
Каковы будут входные данные файла для получения выходных данных Good game ?

### Ответьте на вопросы ниже
Каковы входные данные?
```commandline
chmod 777 crackme5
./crackme5
strings crackme5
r2 -d ./crackme5
aaa
afl
pdf @main
db 0x0040082f
dc
pdf @main
px @rsi
```
```commandline
OfdlDSA|3tXb32~X3tX@sX`4tXtz
```

## Задание 6
Проанализируйте двоичный файл для простого пароля

### Ответьте на вопросы ниже
Какой пароль?
```commandline
./crackme6
strings crackme6
r2 -d ./crackme6
aaa
afl
pdf @main
pdf @sym.compare_pwd
pdf @sym.my_secure_test
```
```commandline
1337_pwd
```

## Задание 7
Проанализируйте двоичный файл, чтобы получить флаг
### Ответьте на вопросы ниже
Что такое флаг?
```commandline
./crackme7
strings crackme7
pdf @main
```
```commandline
flag{much_reversing_very_ida_wow}
```

## Задание 8
Проанализируйте двоичный файл и получите флаг

### Ответьте на вопросы ниже
Что такое флаг?
```commandline
./crackme8
strings crackme8
r2 -d ./crackme8
pdf @main
```
```commandline
flag{at_least_this_cafe_wont_leak_your_credit_card_numbers}
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)