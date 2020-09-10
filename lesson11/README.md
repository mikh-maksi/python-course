# Магічні методи 

В Python використовують спеціальні (**магічні**) методи, щоб використовувати такі можливості, як ми описали.
Метод `__init__`  задає значення при створенні елементу класу, а метод `__contains__` дозволяє перевірити, що клас містить певне значення.
Назви "магічних"  методів починаються і закінчуються двома символами `_`.  

[Детальний перелік магічних методів з поясненнями і прикладами](https://minhhh.github.io/posts/a-guide-to-pythons-magic-methods).  

У випадку з собакою ми отримаємо:
```python
class Dog:
    value = ''
    def __init__(self,value):
        self.value = value
    def __contains__(self, item):
        out = False
        if item == self.value:
            out = True
        return  out
```
Також ми можемо зменшити розмір коду, якщо використаємо оператор `in` , який перевіряє, чи входить одне значення до іншого
```python
class Dog:
    value = ''
    def __init__(self,value):
        self.value = value
    def __contains__(self, item):
        return item in self.value
```

## Методи доступу до елементів контейнера. 
## Визначення математичних операцій для об’єктів Python. 
## Context managers.
## Iterators
## Generators
## Інкапсуляція (Setters, getters, deletters).
## Використанням декораторів з класами.
## Properties, статичні методи.
## Інкапсуляція
