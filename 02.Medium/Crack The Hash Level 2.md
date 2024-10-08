[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)

# Комната [Crack The Hash Level 2](https://tryhackme.com/r/room/crackthehashlevel2) 

Всего 7 заданий:
## Задание 1
Взлом паролей является частью работы тестировщика на проникновение, но ему редко обучают на платформах испытаний. В 
этой комнате вы узнаете, как взламывать хэши, определять типы хэшей, создавать пользовательские списки слов, 
находить определенные списки слов, создавать правила мутаций и т. д.

Эта комната является духовным наследником Crack the Hash .

Я рекомендую вам выполнить задание « Взломать хэш», прежде чем пытаться выполнить это задание, поскольку оно сложнее 
и требует использования более продвинутых методов.

Однако в этой комнате есть курс по взлому хэшей, прежде чем вы столкнетесь с трудностями взлома. Возможно, будет 
хорошей идеей прочитать часть курса перед тем, как приступить к взлому хэшей, если вы новичок.

### Ответьте на вопросы ниже

```commandline
Ответ не нужен
```

## Задание 2
Часто первое, что вам нужно, когда вы сталкиваетесь с хешем, это попытаться определить, какой это тип хеша.
Существует много типов хеша, некоторые из них очень известны, например MD5 или SHA1, но другие менее известны, и существует несколько возможных типов хеша для заданного набора символов и длины.

### Ответьте на вопросы ниже
Haiti — это CLI-инструмент для определения типа хеша заданного хеша. Установите его.
```commandline
Ответ не нужен
```
Запустите Haiti на этом хэше:
`741ebf5166b9ece4cca88a3868c44871e8370707cf19af3ceaa4a6fba006f224ae03f39153492853`
Что это за гашиш?
```commandline
RIPEMD-320
```
Запустите Haiti на этом хэше:
`1aec7a56aa08b25b596057e1ccbcb6d768b770eaa0f355ccbd56aee5040e02ee`
```commandline
Ответ не нужен
```
Что такое код Hashcat Keccak-256?
```commandline
17800
```
Что такое код Keccak-256 John the Ripper?
```commandline
raw-keccak-256
```

## Задание 3
Для взлома хэшей вам часто понадобятся специальные словари, называемые списками слов.

**SecLists** — это коллекция списков различных типов, используемых во время оценок безопасности, собранных в одном 
месте. Типы списков включают имена пользователей, пароли, URL-адреса, шаблоны конфиденциальных данных, полезные 
нагрузки фаззинга, веб-шеллы и многое другое.

**wordlistctl** — это скрипт для извлечения, установки, обновления и поиска архивов списков слов с веб-сайтов, 
предлагающих списки слов, содержащие более 6300 доступных списков слов.

**CyberSecurity Inventory** от Rawsec — это список инструментов и ресурсов по теме CyberSecurity. Категория Cracking 
будет особенно полезна для поиска инструментов для генерации списков слов.

Примечание : в упражнении ниже мы увидим, как использовать wordlistctl для загрузки списка. Для примера я взял 
rockyou,который является известным списком слов, но если вы используете TryHackMe AttackBox или KaliLinux,он у вас 
уже должен быть `/usr/share/wordlists/`, поэтому вам не нужно загружать его снова. Это просто пример, чтобы показать 
вам, как работает wordlistctl.

### Ответьте на вопросы ниже
RockYou — известный список слов, содержащий большой набор часто используемых паролей, отсортированных по частоте.
Для поиска этого списка слов с помощью wordlistclt выполните:
```commandline
wordlistctl search rockyou
```
Какую опцию необходимо добавить к предыдущей команде для поиска в локальных архивах вместо удаленных?
```commandline
-l
```
Загрузите и установите список слов rockyou, выполнив следующую команду: `wordlistctl fetch -l rockyou`
```commandline
Ответ не нужен
```

Теперь снова найдите rockyou в вашем локальном архиве с помощью `wordlistctl search -l rockyou`

Вы должны увидеть, что список слов развернут на `/usr/share/wordlists/passwords/rockyou.txt.tar.gz`

Но список слов сжат в архив tar.gz, для его распаковки запустите `wordlistctl fetch -l rockyou -d`.
Если запустить `wordlistctl search -l rockyou` еще раз, по какому пути хранится список слов?
```commandline
/usr/share/wordlists/passwords/rockyou.txt
```

Вы можете выполнить поиск по списку слов по определенной теме (например, facebook) wordlistctl search facebookили 
просмотреть все списки слов из категории (например, fuzzing) `wordlistctl list -g fuzzing`.

Как называется первый список слов в категории имен пользователей?

```commandline
CommonAdminBase64
```

## Задание 4
Наконец, вам понадобится инструмент для взлома, вот два самых распространенных из них:
- ХэшКэт
- Джон Потрошитель (увеличенная версия)


Существует несколько способов взлома, которые вы можете использовать:

- Режим списка слов, который заключается в переборе всех слов, содержащихся в словаре. Например, список 
распространенных паролей, список имен пользователей и т. д.
- Инкрементальный режим, который заключается в переборе всех возможных комбинаций символов в качестве паролей. Это 
  мощный, но гораздо более долгий способ, особенно если пароль длинный.
- Режим правил, который заключается в использовании режима списка слов путем добавления в него некоторого шаблона или 
  искажения строки. Например, добавление текущего года или добавление общего специального символа.

Существует 2 способа выполнения перебора на основе правил:

- Создание пользовательского списка слов и использование с ним классического режима списка слов.
- Используя общий список слов, сообщите инструменту взлома, что нужно применить к нему некоторые специальные правила 
  искажения.


 Второй вариант гораздо более мощный, так как вы не будете тратить гигабайты, сохраняя тонны списков слов и тратить 
  время на создание тех, которые вы будете использовать только один раз. Вместо того, чтобы иметь несколько 
  интересных списков и применять различные правила искажения, которые вы можете повторно использовать для разных 
  списков слов.

John the Ripper уже включает в себя различные правила искажения, но вы можете создать свои собственные и применять 
их к списку слов при взломе:

```commandline
$ john hash.txt --wordlist=/usr/share/wordlists/passwords/rockyou.txt rules=norajCommon02
```

Вы можете обратиться к синтаксису правил списка слов Джона Потрошителя для создания своих собственных правил.
Я дам вам основные идеи правил мутации, конечно, некоторые из них можно объединить вместе.
- Мутация границ — часто используемые комбинации цифр и специальных символов могут быть добавлены в конце или в 
начале, или и там, и там.
- Причудливая мутация — буквы заменяются похожими на них специальными символами.
- Мутация регистра - программа проверяет все варианты заглавных/строчных букв для любого символа
- Мутация порядка — порядок символов обратный
- Повторяющаяся мутация — одна и та же группа символов повторяется несколько раз.
- Мутация гласных — гласные пропускаются или пишутся с заглавной буквы
- Мутация Strip - удаляется один или несколько символов
- Мутация обмена — некоторые персонажи меняются местами.
- Дублирующая мутация — некоторые символы дублируются
- Мутация разделителя — между символами добавляются разделители.

### Ответьте на вопросы ниже
В зависимости от вашего дистрибутива конфигурация John может находиться в `/etc/john/john.conf` и/или 
`/usr/share/john/john.conf`.  Чтобы найти установочный каталог JtR, запустите `locate john.conf`, затем создайте 
`john-local.conf` в том же каталоге (в моем случае `/usr/share/john/john-local.conf`) и создайте здесь наши правила.
```commandline
Ответ не нужен
```

Давайте используем список 10 000 самых используемых паролей из SecLists ( `/usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt`) и сгенерируем простую мутацию границы, добавив все комбинации из 2 цифр в конце каждого пароля.
Давайте отредактируем `/usr/share/john/john-local.conf` и добавим новое правило:
`[Список.Правил:THM01]
$[0-9]$[0-9]`
```commandline
Ответ не нужен
```
Теперь давайте взломаем хеш SHA1 2d5c517a4f7a14dcb38329d228a7d18a3b78ce83, нам просто нужно записать хеш в текстовый файл и указать тип хеша, список слов и имя нашего правила. john hash.txt --format=raw-sha1 --wordlist=/usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt --rules=THM01

Какой был пароль?
```commandline
moonligh56
```

## Задание 5
Как я уже говорил в предыдущих правилах искажения задач, они позволяют избежать траты дискового пространства и 
времени, но в некоторых случаях создание собственного списка слов может оказаться более разумной идеей:
- Вы часто будете повторно использовать список слов, его создание сэкономит вычислительную мощность, а не использование правила искажения.
- Вы хотите использовать список слов с несколькими инструментами
- Вы хотите использовать инструмент, который поддерживает списки слов, но не искажает правила
- Вы находите синтаксис пользовательского правила Джона слишком сложным
### Ответьте на вопросы ниже
Допустим, мы знаем, что пароль, который мы хотим взломать, касается собак. Мы можем загрузить список собачьих бегов 
`wordlistctl fetch -l dogs -d ( /usr/share/wordlists/misc/dogs.txt)`. Затем мы можем использовать Mentalist для 
генерации некоторых мутаций.
```commandline
Ответ не нужен
```
Мы можем загрузить наш список слов для собак в Mentalist, добавить некоторые правила Case, Substitution, Append/Prepend.
Здесь мы переключим регистр одного символа из двух и заменим все s на знак доллара.

Затем мы можем обработать и сохранить вновь созданный список слов.
Также возможно экспортировать правила John/Hashcat.
```commandline
Ответ не нужен
```
Взломайте следующий хеш md5 с помощью списка слов, сгенерированного на предыдущих шагах.
`ed91365105bba79fdab20c376d83d752`
```commandline
mOlo$$u$
```
Теперь давайте используем CeWL для генерации списка слов с веб-сайта. Это может быть полезно для извлечения большого количества слов, связанных с темой пароля.
```commandline
Ответ не нужен
```
Например, чтобы загрузить все слова с example.org с глубиной 2, выполните:
`cewl -d 2 -w $(pwd)/example.txt https://example.org`
Глубина — это номер уровня ссылок, по которому будет следовать поисковый робот.

Какое последнее слово в списке?
```commandline
information
```
С TTPassGen мы можем создавать списки слов с нуля. Создайте первый список слов, содержащий все 4-значные значения PIN-кода.

`ttpassgen --rule '[?d]{4:4:*}' pin.txt`
```commandline
Ответ не нужен
```
Сгенерируйте список всех комбинаций строчных букв длиной от 1 до 3.

`ttpassgen --rule '[?l]{1:3:*}' abc.txt`
```commandline
Ответ не нужен
```
Затем мы можем создать новый список слов, который будет комбинацией нескольких списков слов. Например, объединить список слов PIN-кода и список буквенных слов, разделенных тире.

`ttpassgen --dictlist 'pin.txt,abc.txt' --rule '$0[-]{1}$1' combination.txt`

Будьте осторожны, объединение списков слов быстро приводит к созданию огромных файлов, в данном случае combination.txt имеет размер 1,64 ГБ.
```commandline
$ wc pin.txt
10000 10000 50000 шт.txt

$ wc abc.txt
18278 18278 72384 abc.txt

$ wc комбинация.txt
 182780000 182780000 1637740000 комбинация.txt
```

```commandline
Ответ не нужен
```
Взломайте этот md5-хеш с помощью combination.txt.
`e5b47b7e8df2597077e703c76ee86aee`
```commandline
1551-li
```

## Задание 6
Вам придется взломать несколько хешей. Для каждого хеша вам будет предоставлен короткий сценарий, который поможет 
вам создать правила искажения, построить список слов или найти некоторые специализированные данные, которые вам 
понадобятся для взлома хеша.

Сценарии размещены на сайте: Советник по паролям (http://MACHINE_IP), каждый совет соответствует одному из следующих 
хэшей (в том же порядке).

### Ответьте на вопросы ниже
Совет № 1b16f211a8ad7f97778e5006c7cecdf31
```commandline
Zachariah1234*
```
Совет №27463fcb720de92803d179e7f83070f97
```commandline
Angelita35!
```
Совет №3f4476669333651be5b37ec6d81ef526f
```commandline
Tl@xc@l@ncing0
```
Совет № 4a3a321e1c246c773177363200a6c0466a5030afc
```commandline
DavIDgUEtTApAn
```
Совет №5d5e085772469d544a447bc8250890949
```commandline
uoy ot miws ot em rof peed oot ro ediw oot si revir oN
```
Совет № 6377081d69d23759c5946a95d1b757adc
```commandline
+17215440375
```
Совет №7ba6e8f9cd4140ac8b8d2bf96c9acd2fb58c0827d556b78e331d1113fcbfe425ca9299fe917f6015978f7e1644382d1ea45fd581aed6298acde2fa01e7d83cdbd
```commandline
!@#redrose!@#
```
Совет №89f7376709d3fe09b389a27876834a13c6f275ed9a806d4c8df78f0ce1aad8fb343316133e810096e0999eaf1d2bca37c336e1b7726b213e001333d636e896617
```commandline
hackinghackinghackinghacking
```
Совет №9$6$kI6VJ0a31.SNRsLR$Wk30X8w8iEC2FpasTo0Z5U7wke0TpfbDtSwayrNebqKjYWC4gjKoNEJxO/DkP.YFTLVFirQ5PEh4glQIHuKfA/
```commandline
kakashi1
```

## Задание 7
Надеюсь, вам понравилась комната.
Чтобы узнать больше обо мне ( noraj ), посетите pwn.by/noraj.
Вы можете найти мои другие комнаты THM в моем профиле THM.

ПопробуйтеHackMe
### Ответьте на вопросы ниже
Спасибо
```commandline
Ответ не нужен
```

[>> вернуться на главную страницу](https://github.com/BEPb/tryhackme/blob/master/README.md)