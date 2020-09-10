# Модуль 2a. Управление потоком выполнения
По-умолчанию в Python команды выполняются одна за одной сверху вниз. Последовательность запуска команд в программе называется «поток выполнения» (Flow of execution). 
Программы, в которых все команды выполняются одна за одной называются *линейными программами*.
В программировании существует всего 2 структуры, которые изменяют поток выполнения: 
- ветвления (оператор выбора)
- циклы.  
Обе данные структуры (и цикл и оператор выбора) используют *логические выражения.* 
## Логические выражения
Логические выражения - это набор значений и *операторов*, результатом выполнения которых будет значения типа boolean (True - правда или False - ложь).
Например: 3>3 (Fales), 7>=2 (False), 2*2==4 (True)
## Логические операторы
Чаще всего используются такие логические операторы:


- Равно	==	
- Не равно	!=	
- Больше	>	
- Меньше	<	
- Больше или равно	>=	
Меньше или равно	<=
## Булева алгебра
## Булева алгебра
В Python існує булевський (логічний) тип даних. Змінні цього типу мають лише два значення: 
`True` (істина) та `False` (хибність). 
Для булевського типу даних визначені логічні операції логічного та (`and`), логічного або (`or`), логічного ні (`not`).
Результати даних операцій наведені в таблиці.


### and
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">A</th>
    <th class="tg-c3ow">B</th>
    <th class="tg-c3ow">A and B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">True</td>
  </tr>
  <tr>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">False</td>
  </tr>
  <tr>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">False</td>
  </tr>
  <tr>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">False</td>
  </tr>
</tbody>
</table>

### or
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">A</th>
    <th class="tg-c3ow">B</th>
    <th class="tg-c3ow">A or B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">True</td>
  </tr>
  <tr>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">True</td>
  </tr>
  <tr>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">True</td>
  </tr>
  <tr>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">False</td>
  </tr>
</tbody>
</table>

#### not
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">A</th>
    <th class="tg-c3ow">not A</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">True</td>
    <td class="tg-c3ow">False</td>
  </tr>
  <tr>
    <td class="tg-c3ow">False</td>
    <td class="tg-c3ow">True</td>
  </tr>
</tbody>
</table>


### Створення змінних булівського типу
```python
a = True
b = False
c = a and b
d = a or b 
e = not a
print(c)    # False
print(d)    # True
print(e)    # False
```

### Об'єкт типу `None`
В Python існує спеціальний об'єкт `None` для тих випадків, коли ми хочемо створити об'єкт
який не має ні значення, ні типу, пустий об'єкт.

```python
a = None
print(a)
``` 

Функція, яка нічого не повертає насправді повертає `None`. В деяких випадках, коли ми хочемо вказати
на факт, що результат роботи коду невизначений можна використовувати `None`.


## Условное выполнение
## Последовательность условий
## Вложенные условия
## Перехват исключений с использованием try и except

Виключення в Python &mdash; це помилки на рівні механізму запуску програми (інтерпретатору), які викликані неможливістю виконати той чи інший оператор, з будь-яких причин (змінна не існує,
синтаксична помилка, відсутній атрибут, операція ділення на нуль, тощо).

Наприклад, наш скрипт очікує даних від користувача в форматі цілого числа. Однак, користувач може ввести будь-який символ (наприклад рядок 'a'), в такому разі, при спробі конвертувати введений символ в число, станеться помилка:

```python
val = 'a' #навмисно робимо  значення змінної val таким, що викличе помилку
print("Ви ввели: ", int(val)) # цей код викликає помилку
```
В даному випадку програма припинить свою роботу і користувач так і не дізнається, що привело до цього збою. Проте ми можемо обробити цю помилку (така помилка називається `ValueError`).

`ValueError`, це помилка (виключення), що стається у випадку неможливості конвертувати передане значення у необхідний тип даних.  

В нашому прикладі (введено 'а') інтерпретатору намагається перетворити рядок на `int` (ціле число), але як конвертувати рядок `'a'` в число він не знає і викликає виключення з цього приводу.

## Механізм обробки виключень

Для обробки виключень існує оператор `try ... except ...`. Синтаксично, цей оператор починається з ключового слова `try:` (спробувати) і продовжується 
блоком коду на наступному рядку, який виділений відступом.

Далі йде блок обробки виключень `except` (окрім), де можна вказати одне, 
або більше виключень, після яких виконати наступний блок коду.

В нашому прикладі обробка користувацького вводу виглядатиме наступним чином:

```python
val = 'a'
try:
    print("Ви ввели: ", int(val))
except ValueError:
    print("Введено некоректний символ")
```

## Власні виключення
Більшість виключень в Python детально описані та формують читабельний і детальний звіт стосовно
причини, що викликала неможливість виконання операції.
Однак, для зручності, програміст може створити свої класи помилок, щоб згодом обробляти їх певним чином.

Для __створення__ **власного виключення** достатньо створити клас, який успадковує `Exception` &mdash; це батьківський клас всіх виключень в Python.

```python
class IncorrectInput(Exception): #Назва власного виключення може бути будь-якою
    pass
```
Якщо синтаксис вимагає наявність оператора, але нам не потрібно нічого виконувати, то оператор `pass` стане у нагоді. Бо оператор `pass`, як раз створений нічого не виконувати.

Щоб __викликати__ *власне виключення* існує оператор `raise`: 

```python
   def validate(self, value):
        try:
            self.value = float(value)
        except ValueError: 
            raise IncorrectInput()
```

Але для того, щоб зрозуміти яке виключення спрацювало, краще додавати повідомлення про це:

```python
   def validate(self, value):
        try:
            self.value = float(value)
        except ValueError: 
            raise IncorrectInput(f"value {value} can't be converted to float")
```

## Упражнения

# Модуль 2b. итерации
## Цикли
Цикли - це алгоритмічні керуючі конструкції, 
які дозволяють виконувати певні операції (тіло циклу) декілька разів.


### Цикл while

Цикл `while` дозволяє виконувати оператори, які знаходяться в тілі циклу доти, доки виконується умова,
що вказана в циклі. Наприклад, цикл `while`, що виводить числа від 1 до 5

```python
a = 1
while a <= 5:
    print(a)
    a += 1
```

Умовою може бути будь-який вираз, або змінна Python, що може бути приведена до типу `bool`.

## «Бесконечные циклы» и break
## Завершение итерации с помощью continue
## Comprehensions (list, dict, set).
## Определение циклов с помощью for
### Цикл for
В Python, цикл `for` використовується для перебору будь-яких контейнерів, 
або ітерованих об’єктів, наприклад, списків. 
Оператори, які знаходяться в тілі циклу будуть виконані стільки разів, скільки елементів є в списку. 

При цьому, на кожному кроці спеціальна змінна отримує значення одного з елементів списку.

Роботу циклу `for` можна порівняти з тим що, ви по черзі візьмете кожен фрукт з корзини 
і проговорите його назву (корзиною в даному випадку буде виступати список рядків з назвами фруктів, 
а проговоренням буде виступати виведення відповідних рядків на екран)

```python
fruits = ['apple', 'pear', 'apricot', 'orange', 'plum']
for fruit in fruits:
    print(fruit)
```

Цикл `for` на практиці використовується для формування нових переліків на основі вже існуючих. 
Наприклад, з існуючого переліку (з числами від 1 до 10) перенесемо в новий перелік лише ті числа, 
що кратні 3.

Визначення кратності забезпечується за рахунок оператору `%` ("залишок від ділення"). 
Тобто, якщо залишок від ділення числа на 3 дорівнює нулю, то таке число кратне 3.

Також важливою особливістю є те, що 0 відповідає логічному значенню `False` тобто вирази 
`a % 3 == 0` та `not a % 3` будуть еквівалентними.

Приклад роботи такого оператору:

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for elem in a:
    if not elem % 3:
       result.append(elem)

print(result)   # Виведе [3, 6, 9]
```

## Обход списков с помощью цикла for
## Упражнения