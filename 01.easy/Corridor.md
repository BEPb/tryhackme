[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Corridor](https://tryhackme.com/r/room/corridor) 

Всего 1 заданиe:
## Задание 1
При переходе в каждую комнату, ее Url содерижит хеш номера комнаты от 1 до 13, для получения флага нужно 
отредактировать этот хеш, хешом нулевой комнаты.
```commandline
nmap -sV -sC <IP>
echo -n "0" | md5sum
http://<IP>/REDACTED
```

```commandline
flag{2477ef02448ad9156661ac40a6b8862e}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)