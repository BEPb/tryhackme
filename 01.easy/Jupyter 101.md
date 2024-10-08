[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Jupyter 101](https://tryhackme.com/r/room/jupyter101) 

Всего 8 заданий:
## Задание 1
Наука о данных — очень широкая, огромная тема, к которой (по моему мнению) нелегко подступиться и которую гораздо 
сложнее освоить. Она имеет огромное множество применений во всех типах отраслей! Вот несколько реальных примеров 
того, где наука о данных может быть найдена изо дня в день: 
- Рекомендации  контента на Netflix и YouTube на основе вашей предыдущей истории просмотров
- Обнаружение мошенничества в банковской сфере
- Обнаружение вторжений для кибербезопасности
- Прогнозирование погоды / Предсказание
- Показатели эффективности продаж компании
- Планирование маршрута в Google Maps.


Он также идет рука об руку с машинным обучением/искусственным интеллектом.

Несмотря на то, что в следующей комнате используется Python, я постарался объяснить любой код как можно подробнее. 
Сам код довольно прост, так что если вы не знакомы с Python, вы все равно сможете без проблем разобраться! 

Надеюсь, что следующая комната станет для вас дружественным введением в среду «Jupyter Notebook», которая является 
чрезвычайно полезным приложением в мире науки о данных. 

Более того, я надеюсь, что задачи ниже являются практичным и увлекательным подходом к очень распространенной 
библиотеке "Pandas", где данные обрабатываются. Наконец, фреймворк "Matplotlib" - моя любимая часть, где мы можем 
визуализировать все данные, с которыми мы работали!  

Это мой первый выпуск комнаты, поэтому, пожалуйста, извините меня, если я что-то упустил. Если есть интерес к темам 
из этой комнаты , я создам дальнейший контент, где мы будем гораздо глубже разбираться и применять знания для 
решения практических задач (если позволит моя учеба в университете, а также то, что я в целом суперсумасброден). Но 
в то же время, я надеюсь, вам понравится!   

Если у вас есть какие-либо отзывы, вопросы, проблемы или идеи на будущее, которые вы хотели бы обсудить, свяжитесь с 
нами: 

Дискорд : @CMNatic#9812

Я часто посещаю TryHackMe Discord, но в любом случае, пожалуйста, не стесняйтесь писать мне в этом Discord!

Всего доброго и спасибо за рыбу!

~ CMNatic

Выражаем благодарность MuirlandOracle за его ценные отзывы во время тестирования!

### Ответьте на вопросы ниже
Давайте назад!
```commandline
Ответ не нужен
```

## Задание 2
Jupyter — это веб-платформа, часто используемая для анализа данных/построения графиков, машинного обучения, где код хранится в «блокнотах», которые можно импортировать/экспортировать и совместно использовать во многих форматах, таких как LaTex, HTML, PDF и многих других!


Среда Jupyter Notebook — не самая простая в установке и развертывании вещь в мире. Обычно вам нужно предоставить файлы конфигурации, среды Python и всякие забавные вещи. Я проделал всю работу и сделал облачное развертывание Jupyter, которое запускается при загрузке.

Jupyter хорош тем, что позволяет импортировать/экспортировать любые созданные вами блокноты или любые другие  блокноты, созданные другими людьми .

Из-за природы Jupyter довольно сложно что-либо сломать. Но если вы хотите восстановить предоставленные Notebooks - вы можете просто повторно развернуть экземпляр!

### Ответьте на вопросы ниже
Прочитайте вспомогательные материалы.
```commandline
Ответ не нужен
```

## Задание 3
луйста, подождите 5 минут, пока экземпляр полностью загрузится, прежде чем пытаться получить к нему доступ. Если вы 
не можете получить к нему доступ в течение 5 минут, пожалуйста, «Terminate» и повторно «Deploy» 

Когда вы запустите экземпляр и перейдете к нему, вам будет представлен экран входа в систему, подобный следующему:
                           

Jupyter использует протоколы аутентификации и токены для управления пользователями, что является головной болью в 
управлении. Я не смог найти работающего решения, чтобы полностью удалить это, поэтому я сделал все возможное, чтобы 
обойти это.  

Используйте пароль: tryhackme

Если вы успешно вошли в систему, вам будет представлено следующее:

Вы готовы к работе!

Выдержка из сопроводительного материала :

«Jupyter напрямую взаимодействует с файловой системой операционной системы (при условии, что у пользователя, от 
имени которого он запущен, есть необходимые разрешения!). Это означает, что вы можете создавать и загружать файлы и 
перемещаться по папкам — как если бы вы делали это на самом хосте.  Аналогично, все, что вы удаляете на хосте — 
удаляется и на Jupyter... вы поняли...»   

Мы рассмотрим это позже...

### Ответьте на вопросы ниже
Я вошел в систему!
```commandline
Ответ не нужен
```

## Задание 4
Войдите в каталог «WhatIsJupyter» , запустите « WhatIsJupyter.ipynb » и прочитайте.

Вопросов нет, но я подробно расскажу о некоторых вариантах использования Jupyter и о том, почему кто-то может использовать его вместо IDLE, такого как PyCharm! 

### Ответьте на вопросы ниже
Запустить Jupyter
```commandline
Ответ не нужен
```

## Задание 5
Перейдите в каталог « UnderstandingJupyterNotebooks » , запустите « UnderstandingHowJupyterExecutes.ipynb » и прочитайте аннотации, которые я сделал, чтобы понять, как ответить на этот вопрос.

### Ответьте на вопросы ниже
Как действуют «клетки»?
```commandline
Interpreter
```
Каким будет значение In[#] первой ячейки при ее первом запуске? (Где # будет числовым значением)
```commandline
1
```
Какую комбинацию клавиш можно нажать, чтобы выполнить ячейку?
```commandline
Shift + Enter
```
Если бы вы снова выполнили первую ячейку, каким стало бы значение In[#]?  (Где # было бы числовым значением)
```commandline
2
```
## Задание 6
Как уже упоминалось в пошаговом руководстве, Jupyter напрямую взаимодействует с файловой системой операционной 
системы. Например, создавая файлы, папки и/или блокноты. 

Эти файлы отражаются в операционной системе, на которой работает Jupyter. Каталог, который вы видите после входа в 
Jupyter, по сути, является «корневым» каталогом Jupyter.  

Однако, просто потому что это "корневой" каталог, это не значит, что это каталог Operating Systems /root/. Это 
просто каталог, где Jupyter был запущен или куда ему было сказано установить во время конфигурации. 

В данном случае я указал Jupyter запуститься в домашнем каталоге пользователя «thm», куда вы позже войдете и сами 
все увидите. 

Давайте войдем в экземпляр, заменив все IP-адреса на рисунках ниже на адрес экземпляра, который вы развернули.

Имя пользователя: thm

Пароль: tryhackme
Порт: 22

Вы можете войти через Linux :

Или через приложение Windows, например Putty

Теперь, после успешного входа, давайте посмотрим, что происходит, используя ls.

Затем мы создаем новый файл с помощью touch , в данном случае «LookAtMe.Txt»

Возвращаясь к экземпляру Jupyter в вашем веб-браузере, мы теперь можем видеть, что файл, который мы только что создали, виден в Jupyter.!

При открытии файла я вставил туда текст, написанный с помощью Jupyter:

Давайте проверим это изменение (после сохранения в Файл -> Сохранить ), если это не было сделано автоматически.

Та-дам! И вот оно.

Jupyter напрямую использует разрешения пользователя Linux. Таким образом, вы сможете читать/писать/изменять только 
те файлы, которые вы (пользователь, от имени которого запущен сервер Jupyter) в каталоге (который был указан в 
конфигурации или из которого он запущен)  

### Ответьте на вопросы ниже
Следуйте инструкциям выше.
```commandline
Ответ не нужен
```

## Задание 7
Pandas — фантастическая библиотека для обработки данных. Она позволяет нам читать данные из самых разных форматов, 
таких как файлы CSV, JSON, базы данных и многое другое! 

Наборы данных часто очень большие. Хотя их содержимое может быть нам полезно, это содержимое может быть не в том 
формате, который нам нужен! И нам не обязательно нужны все значения — только некоторые из них. Давайте начнем... 

Перейдите в каталог «IntroToPandas»  на экземпляре Jupyter и запустите «IntroToPandas.ipynb». Пожалуйста, прочтите 
аннотации. 

### Ответьте на вопросы ниже
Каковы два основных типа данных в Pandas?
```commandline
Series and Dataframes
```
Как называется функция Pandas, которая считывает CSV-файл?
```commandline
read_csv
```
Назовите функцию Pandas, которую вы бы использовали, если бы хотели отобразить только первые несколько строк.
```commandline
head
```
Назовите функцию Pandas, которую вы бы использовали, если бы хотели отобразить только последние несколько строк.
```commandline
tail
```
Какая функция Pandas даст вам численное значение количества столбцов и строк, содержащихся в наборе данных?
```commandline
shape
```

## Задание 8
Перейдите в каталог «IntroToMatplotlib»  на экземпляре Jupyter и запустите «IntroToMatplotlib.ipynb». Пожалуйста, 
прочтите аннотации.

### Ответьте на вопросы ниже
Как отобразить график? 
```commandline
plot()
```
Как бы вы обозначили ось «x» на графике?
Примечание: не добавляйте скобки () для этого ответа.
```commandline
xlabel
```
Как бы вы обозначили ось «Y» на графике?
Примечание: не добавляйте скобки () для этого ответа.
```commandline
ylabel
```
Как бы вы добавили «Название» к сюжету?
Примечание: не добавляйте скобки () для этого ответа.
```commandline
title
```
Какое слово вы бы использовали, чтобы изменить цвет графика?
```commandline
color
```
Как бы вы обозначили ось «z» на графике?
Примечание: не добавляйте скобки () для этого ответа.
```commandline
zlabel
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)