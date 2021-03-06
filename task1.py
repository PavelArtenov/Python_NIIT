import random

"""Функция fio, которая принимает одну строку, состоящую из ФИО (например, "Ladoshkin Nikita Evgenievich") 
и возвращает словарь с ключами name, surname, patronymic (пример, {'name': 'Nikita', 'surname': 'Ladoshkin', 'patronymic': 'Evgenievich'})"""

str = "Artenov Pavel Sergeevich"


def fio(str):
    arr = str.split(' ')
    d = {'Surname': arr[0],'Name': arr[1],'Patronymic': arr[2]}
    return d


print(fio(str))

#_______________________________________________________________________________________________________________________________________________________________

"""Функция sort_str, которая принимает массив строк (['aaa', 'c', 'qq']) и возвращает массив этих строк, отсортированных по длине (['c', 'qq', 'aaa'])"""

arr_str = ['Компьютер ','—','это','самый','удивительный','инструмент','с','каким','я','когда-либо','сталкивался.','Это', 'велосипед','для','нашего','сознания.']


def sortByLength(inputStr):               #функция,которая возвращает объект,который будет сравниваться во время сортировки
        return len(inputStr)


def sort_str(arr_str):
    arr_str.sort(key=sortByLength)
    return arr_str

print(sort_str(arr_str))

#_______________________________________________________________________________________________________________________________________________________________
"""Упрощенная собственная реализация simple_range, которая примимает два числа (1, 5),
 а возвращает массив от первого числа включительно до второго невключительно ([1, 2, 3, 4])"""


x,y = 1,50


def simple_range(x,y):
    arr = []
    while(x < y):
        arr.append(x)
        x = x + 1
    return arr


print(simple_range(x,y))

#________________________________________________________________________________________________________________________________________________________________

"""Функция use_rand без параметров, которая получает результат ф-ии randint библиотеки random c аргументами 1 и 50,
 до тех пор, пока не получите число 42, затем вернете этот результат"""


def use_rand():
    x,y = 0,0                           #y - счетчик попыток
    while(x != 42):
        x = random.randint(1,50)
        y = y + 1
    print('Угадали с {} раза'.format(y))
    return x


print(use_rand())






        


