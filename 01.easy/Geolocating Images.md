[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Geolocating Images](https://tryhackme.com/r/room/geolocatingimages) 

Всего 8 заданий:
## Задание 1
В этом уроке вы узнаете, как геолоцировать изображения — от простых до гораздо более сложных задач.



Наша первая мысль о геолокации изображений: «Где в Интернете появляется это изображение?»

В конце концов, изображение может находиться на сайте под названием « ILoveEgypt.com »!



Для этого мы используем программу обратного поиска изображений. В интернете их много, но порядок от хорошего к худшему такой:



Яндекс
Яндекс
Яндекс
....

101. Яндекс
102. Bing

103. Гугл



Причина, по которой Google находится на 103 месте, а не в первых 101 результатах, заключается в том, что Яндекс в миллион раз лучше.

«Яндекс» для Google — то же самое, что гоночный автомобиль «Формулы-1» для машины за 200 долларов, которую вы пригнали своему другу Ивану, утверждающему, что машина не украдена, но за вами всю неделю следит полиция.



Это действительно как день и ночь. Невозможно сравнивать. Сначала используйте Яндекс, а потом еще сотню раз. Затем после Яндекса используйте Bing. Затем Google. Я не могу достаточно подчеркнуть, насколько шутлив обратный поиск изображений Google.  Это должно быть вашим последним средством.



Когда вы делаете обратный поиск изображений с помощью Google, Google пытается найти точное совпадение с этим изображением. С Yandex это почти как если бы Yandex сразу знал, что изображено на вашем изображении, и показывал вам другие изображения того же самого, чтобы подкрепить идею, что он знает.



Вот забавный эксперимент. Сфотографируйте себя прямо сейчас. У вас наверняка есть другие фотографии в сети. Обратный 
поиск изображений Google, скорее всего, никогда вас не найдет, если вы никогда не загружали изображение. 

Яндекс, скорее всего, сможет определить, кто вы, и показать вам другие ваши изображения.

Яндекс использует ИИ для обратного поиска изображений, в то время как складывается впечатление, что Google выполняет 
простую операцию «if IMG_0657 = [Позиция 1 в базе данных изображений]: return» по всем имеющимся у него изображениям. 

Более подробную информацию о сравнении «Яндекс», «Bing» и «Google» можно найти в анализе Bellingcat:

https://www.bellingcat.com/resources/how-tos/2019/12/26/guide-to-using-reverse-image-search-for-investigations/

Все изображения, необходимые для этого пошагового руководства, находятся в zip-архиве.

### Ответьте на вопросы ниже
Загрузить zip-файл
```commandline
Ответ не нужен
```

## Задание 2
Где изображение 1?

(Воспользуйтесь обратным поиском Google и насладитесь всеми самолетами, которые он вам покажет, что, кстати, не является правильным ответом).

Попробуйте обратный поиск картинок Яндекса. Посмотрите на различия!

### Ответьте на вопросы ниже
Где в мире находится изображение 1? Ответ — название страны.

```commandline
China
```

## Задание 3
Хорошо, теперь мы знаем, какую программу обратного поиска изображений использовать. Давайте попробуем теперь 
посмотреть на картинку, чтобы выяснить, где она находится! 

Допустим, у нас есть веб-камера, найденная на Shodan.io :

https://padcam.liverpool.ac.uk/cgi-bin/guestimage.html



Где эта камера?

Первое, что мы замечаем, — это странный герб и заголовок с черной полосой (и, возможно, текстом) под ним.

Второе — это логотип «Kaplan».

Третье — рядом со зданием из бетона стоит стеклянное здание.

И наконец, у нас есть то, что похоже на шоссе рядом со стеклянным зданием. Поскольку это веб-камера, мы можем видеть 
быстро движущиеся автомобили! 

Ввод этого в программу обратного поиска изображений ничего не показывает.

Теперь, что важно отметить, это название веб-камеры. URL указывает на Liverpool.ac.uk , что является университетом в Ливерпуле.

Если бы у нас был только IP-адрес, мы могли бы попытаться геолоцировать его с помощью онлайн-инструмента, проверив номер ASN или найдя его на Shodan.

Поиск в Google "Kaplan University of Liverpool" приводит нас к новостной статье о новом здании. Если взглянуть на 
изображение, оно выглядит примерно так же, как то, что мы видели. 


Ряды длинных стаканов с небольшим выступом.

К счастью для нас, «Ливерпуль» подписал изображение.

"The proposed new Liverpool International College facility"

Если мы поищем в Google Liverpool International College, то получим:

https://www.google.com/maps/place/University+of+Liverpool+International+College/@53.4062447,-2.9625347,17z/data=!4m5!3m4!1s0x487b211eda1b2f5f:0xc226c2ccfb209504!8m2!3d53.4060784 !4д -2,9605928

Который наш дом! Но он еще не построен... Что это значит?

В правом нижнем углу Google сообщает, что изображение было сделано в июне 2019 года.

Итак, карты Google еще не обновились.

Если мы повернем камеру на картах Google, то увидим, где должна находиться веб-камера прямой трансляции.

Где-то в этом здании!

При геолокации изображения мы хотим указать крупные ориентиры, которые можно легко найти на карте. Схемы дорог, названия компаний, Эмпайр-стейт-билдинг.

### Ответьте на вопросы ниже

```commandline
Ответ не нужен
```

## Задание 4
Где было сделано изображение 2? В частности, я ищу название места, где, скорее всего, установлена веб-камера. Вы 
узнаете это, когда увидите! 

Пожалуйста, не используйте для этого обратный поиск изображений!

### Ответьте на вопросы ниже
Где было сделано изображение 2?
```commandline
Wrigleyville Sports
```

## Задание 5
Ого, поздравляю! Я нашел веб-камеру на Shodan.io и сделал этот снимок экрана, вы только что геолоцировали свое первое изображение 😎

Важно знать, что есть, а что нет в стране. Например, маловероятно, что обычная католическая церковь появится в местах, где буддизм/ислам являются самой популярной религией.

Язык, используемый в магазинах и транспортных средствах, также имеет значение. Мы можем использовать Google translate, чтобы предсказать, какой язык это может быть.

По какой стороне дороги находятся автомобили, номерные знаки (обычно можно узнать, из какой страны или штата принадлежит номерной знак), разметка на дороге (в разных странах разметка разная), стиль светофоров, выбор одежды прохожих.

Чтобы быть хорошим в геолокации, мы должны открыть глаза на все, что может быть. В вашей стране, например, может быть принято носить пальто в зимний период. Однако в других странах это может быть не так (например, в Австралии).

Даже самая незначительная вещь, о которой мы обычно не задумываемся, может подсказать нам возможное местонахождение.

Один из наиболее очевидных способов геолокации изображения — это просмотр деталей изображения. Содержит ли оно данные EXIF ?

А как насчет места публикации? Есть ли в социальных сетях теги местоположения?

### Ответьте на вопросы ниже
Прочитайте вышеуказанный материал
```commandline
Ответ не нужен
```
## Задание 6
Пожалуйста, не пытайтесь использовать обратный поиск изображений для этого! Обратите особое внимание на то, что находится на изображении.

Я хочу, чтобы вы ответили названием места, куда смотрит веб-камера.

Примечание: название этого местоположения на Google Maps не является правильным ответом. Если вы возьмете это 
название местоположения и вставите его обратно в поиск, вы обнаружите, что их около миллиона. Чтобы усложнить задачу,
я ищу название, которое конкретно идентифицирует это местоположение. Когда вы вводите это название, оно будет 
единственным, которое появится на Google Maps.   

### Ответьте на вопросы ниже
Где было сделано изображение 3?
```commandline
Meudon Observatory
```

## Задание 7
Посмотрите на изображение 4. Что вы видите? Что вы можете наблюдать? 

### Ответьте на вопросы ниже
Где сделано изображение 4?
```commandline
Abbey Road
```

## Задание 8
И это всё!

Дополнительную информацию о геолокации можно найти на сайте Bellingcat:

https://www.bellingcat.com/news/2020/01/21/geolocating-venezuelan-lawmakers-in-europe

Или почаще играйте в Geoguesser!

https://geoguessr.com/

### Ответьте на вопросы ниже
Проверьте ссылки выше!


```commandline
Ответ не нужен
```
[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)