# ege-24-25

ЕГЭ Информатика и ИКТ  

### БЕЛЯКОВ Андрей Юрьевич  

```txt  
Расписание пар:  
10:00 - 11:30  
11:45 - 13:15  
13:20 - 14:50  
``` 

[Наши планы](https://docs.google.com/spreadsheets/d/1Kw0XZmMWeDn3DAlK7mHgJYqDovw2AngaE7qRtOuJhSY/edit?usp=sharing) | [ДНИ ЗАНЯТИЙ](days.md) | [Карта знаний](knowledge-map.md)  

### Где будем брать задачи для тренировок:  

* [kompege](https://kompege.ru/)  
* [задачи ЕГЭ sdamgia](https://inf-ege.sdamgia.ru/)  
* [Yandex ЕГЭ](https://education.yandex.ru/ege?utm_source=platform&utm_medium=partner&utm_campaign=ege&utm_content=cege_link_kabanov&utm_term=20231101)  
* [Сайт Константина Полякова](https://kpolyakov.spb.ru/school/ege/tests.htm)  

### Дистанционные занятия тут:  

* [BBB](https://bbb.psaa.ru/rooms/l2z-d0s-9am-bdi/join)  
* [BBB6](https://bbb6.psaa.ru/b/qt6-06w-o09-6wz)  
* [Доска для рисования Yandex](https://boards.yandex.ru/whiteboard/?hash=fddc440dbd7996bf9be50478edafcd4f)  
* [Доска для рисования Google](https://jamboard.google.com/d/1xmh7Mrc_nAR3PmstdYa9nYTs9L2-kh0dS6ZtaswkQZU/edit?usp=sharing)  
* [Google Colab](https://colab.research.google.com/drive/1Ip_2tQ3MZDehmYG36aAHPFj_msrPgJCt?usp=sharing)  

### Анкетирование и Тестирование:  

* [Мои задачи на Stepik`е](https://stepik.org/course/63529/)  
* [EXAM](http://exam.1gb.ru/)  

Чем будем пользоваться:  

1) [Язык программирования **Python**](https://www.python.org/downloads/)  
2) [Редактор **IDLE** (Integrated Development and Learning Environment)](https://www.python.org/downloads/)  
3) [Редактор кода **VS Code**](https://code.visualstudio.com/)  
4) [Редактор кода **Wing**](https://wingware.com/downloads/wing-101)  
5) [Редактор кода **Thonny**](https://thonny.org/)  
6) [Среда разработки **PyCharm** Community](https://www.jetbrains.com/ru-ru/pycharm/download/)  
7) [Online Среда разработки Replit](https://replit.com/)  
8) [**Google Colab** for Python](https://colab.research.google.com/)  
9) [Учебная доска](https://jamboard.google.com/)  
10) [КУМИР](https://www.niisi.ru/kumir/dl.htm)  
11) https://pastebin.com/  

Дополнительно рекомендую:  

1. [Курс на Stepik`е для подготовки к ЕГЭ](https://stepik.org/50169/)  
2. [Тренировочные задачи по ЕГЭ в ЯндексРепетиторе](https://yandex.ru/tutor/subject/?subject_id=6)  
3. [Документация по библиотеке Turtle](https://docs-python.ru/standart-library/modul-turtle/)  

---  

> Узнать номер версии Питона: `python -V`  

## Базовые команды и функции  

### 1 Консоль: ввод-вывод  

- считать с клавиатуры строку  
`s = input()`  
`s = input("Введите строку - ")`

- считать с клавиатуры целое число  
`n = int(input())`  
`n = int(input("Введите целое число - "))`

- считать с клавиатуры вещественное число  
`n = float(input())`  
`n = float(input("Введите целое число - "))`

- вывести ответ в консоль  
```py
count = 10 
print(count)
print("count =", count)
print(f"count = {count}")
```

### 2 Файл: чтение из файла  

```py
# прочитать все строки из файла и вывести список строк  
f = open("filename.txt")
lines = f.readlines()
print(lines)
```

```py
# прочитать все строки из файла и вывести в консоль построчно  
f = open("filename.txt")
for line in f:
    print(line)
```

```py
# дан файл, в котором в каждой строке записано целое число
# считать все числа из файла и найти сумму чисел
sm = 0
for line in open("filename.txt"):
    sm += int(line)
print(f"sm = {sm}")
```

### 3

