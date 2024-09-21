[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Empline](https://tryhackme.com/r/room/empline) 

Всего 3 задания:
## Задание 1
Убедитесь, что вы подключены к  сети TryHackMe . Если вы не знаете, как это сделать, сначала пройдите комнату OpenVPN.
### Ответьте на вопросы ниже
Разверните машину!
```commandline
Ответ не нужен
```

## Задание 2
Соберите все флаги, чтобы завершить комнату.
### Ответьте на вопросы ниже
Пользователь.txt
```commandline
nmap -sSCV -T4 <IP>
echo "<IP> empline.thm job.empline.thm" >> /etc/hosts
gobuster dir -w /usr/share/wordlists/dirb/common.txt -v -k -u http://job.empline.thm -x php,js,conf,bak,txt,old | grep “Found”
# http://job.empline.thm/careers
# OpenCATS <= 0.9.4 RCE (CVE-2021-41560)

```
```commandline
91cb89c70aa2e5ce0e0116dab099078e
```
Корень.txt
```commandline
74fea7cd0556e9c6f22e6f54bc68f5d5
```

## Задание 3
Во-первых, я хотел бы поблагодарить вас за игру в эту машину. Надеюсь, вам было весело!

И еще, спасибо за отзыв о моей первой коробке ( Mustacchio ).

Завершение, большое спасибо Touklwez .

Хороший взлом!

### Ответьте на вопросы ниже
Спасибо!
```commandline
Ответ не нужен
```


[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)