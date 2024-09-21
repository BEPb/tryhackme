[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Nax](https://tryhackme.com/r/room/nax) 

Всего 1 заданиe:
## Задание 1
Сможете ли вы выполнить задание?
 Загрузка и настройка машины может занять до 5 минут.
Примечание : для этой комнаты требуется Metasploit 6.

### Ответьте на вопросы ниже
Какой скрытый файл вы нашли?
```commandline
PI3T.Png
```
Кто является создателем файла?
```commandline
Piet Mondrian
```
Если при запуске инструмента на загруженном изображении возникает ошибка, связанная с неизвестным форматом ppm, 
откройте его с помощью GIMP или другой программы для рисования, экспортируйте в формат ppm и повторите попытку!
```commandline
Ответ не нужен
```
Какое имя пользователя вы нашли?
```commandline
nagiosadmin
```
Какой пароль вы нашли?
```commandline
n3p3UQ&9BjLp4$7uhWdY
```
Какой номер CVE для этой уязвимости? Он будет в формате: CVE-0000-0000
```commandline
CVE-2019-15949
```
Теперь, когда мы нашли нашу уязвимость, давайте найдем наш эксплойт. Для этой части комнаты мы будем использовать 
модуль Metasploit, связанный с этим эксплойтом. Давайте продолжим и запустим Metasploit с помощью команды `msfconsole`.
```commandline
Ответ не нужен
```
После запуска Metasploit давайте найдем наш целевой эксплойт с помощью команды 'search applicationame'. Каков полный 
путь (начиная с explore) для модуля эксплуатации?
```commandline
exploit/linux/http/nagios_xi_plugins_check_plugin_authenticated_rce
```
Взломайте машину и найдите user.txt
```commandline
THM{84b17add1d72a9f2e99c33bc568ae0f1}
```
Найдите root.txt
```commandline
THM{c89b2e39c83067503a6508b21ed6e962}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)