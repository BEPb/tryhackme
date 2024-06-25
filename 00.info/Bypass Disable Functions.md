[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Bypass Disable Functions](https://tryhackme.com/r/room/bypassdisablefunctions) 

Всего 2 задания:
## Задание 1
#### What is a file upload vulnerability?

This vulnerability occurs in web applications where there is the possibility of uploading a file without being checked by a security system that curbs potential dangers. 

It allows an attacker to upload files with code (scripts such as .php, .aspx and more) and run them on the same server, more information in this room.

Why this room?

Among the typically applied measures is disabling dangerous functions that could execute operating system commands or start processes. Functions such as system() or shell_exec() are often disabled through PHP directives defined in the php.ini configuration file. Other functions, perhaps less known as dl() (which allows you to load a PHP extension dynamically), can go unnoticed by the system administrator and not be disabled. The usual thing in an intrusion test is to list which functions are enabled in case any have been forgotten.

One of the easiest techniques to implement and not very widespread is to abuse the mail() and putenv() functionalities. This technique is not new, it was already reported to PHP in 2008 by gat3way, but it still works to this day. Through the putenv() function, we can modify the environment variables, allowing us to assign the value we want to the variable LD_PRELOAD. Roughly LD_PRELOAD will allow us to pre-load a .so library before the rest of the libraries, so that if a program uses a function of a library (libc.so for example), it will execute the one in our library instead of the one it should. In this way, we can hijack or "hook" functions, modifying their behaviour at will.

Chankro: tool to evade disable_functions and open_basedir

Through Chankro, we generate a PHP script that will act as a dropper, creating on the server a .so library and the binary (a meterpreter, for example) or bash script (reverse shell, for example) that we want to execute freely, and that will later call putenv() and mail() to launch the process.

Install tool:

git clone https://github.com/TarlogicSecurity/Chankro.git
cd Chankro
python2 chankro.py --help

python chankro.py --arch 64 --input c.sh --output tryhackme.php --path /var/www/html

--arch = Architecture of system victim 32 o 64.
--input = file with your payload to execute
--output = Name of the PHP file you are going to create; this is the file you will need to upload.
--path = It is necessary to specify the absolute path where our uploaded PHP file is located. For example, if our file is located in the uploads folder DOCUMENTROOT + uploads. 



Now, when executing the PHP script in the web server, the necessary files will be created to execute our payload.


My command run successfully, and I created a file in the directory with the output of the command.

Credits.

All credit goes to Tarlogic for the script and explaining the method of the bypass.
Answer the questions below
Read the above.

```commandline
Ответ не нужен
```

## Задание 2

```commandline
Ответ не нужен
```

## Задание 3
 
```commandline
Ответ не нужен
```

## Задание 4
 
```commandline
Ответ не нужен
```

## Задание 5
```commandline
Ответ не нужен
```

## Задание 6

```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)