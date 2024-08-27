[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Lesson Learned?](https://tryhackme.com/r/room/lessonlearned) 

Всего 1 заданиe:
## Задание 1
Это относительно простая машина, которая пытается преподать вам урок, но, может быть, вы уже усвоили этот урок? 
Давайте выясним. 

Относитесь к этому ящику так, как будто это настоящая цель, а не CTF.

Пройдите экран входа и вы найдете флаг. Нет никаких кроличьих нор, никаких скрытых файлов, только страница входа и 
флаг. Удачи! 
 
Цель: http:// MACHINE_IP/

### Ответьте на вопросы ниже
Какой флаг?
```commandline
nmap -sV -sC <IP>
http://<IP>
' AND '1'='1' -- -
```
```commandline
THM{aab02c6b76bb752456a54c80c2d6fb1e}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)