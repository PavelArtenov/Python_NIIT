'''
Напишите программу, которая уничтожает файлы и папки по истечении заданного времени.
Вы указываете при запуске программы путь до директории, за которой нашему скрипту необходимо следить.
После запуска программа не должна прекращать работать, пока вы не остановите ее работу с помощью Ctrl+C
(подсказка: для постоянной работы программы необходим вечный цикл, например, "while True:",
при нажатии Ctrl+C автоматически остановится любая программа).
Программа следит за объектами внутри указанной при запуске папки и удаляет их тогда,
когда время их существования становится больше одной минуты для файлов и больше двух минуты для папок
(то есть дата создания отличается от текущего момента времени больше чем на одну/две минуту).
Ваш скрипт должен смотреть вглубь указанной папки.
Например, если пользователь создаст внутри нее папку, внутри нее еще одну, а внутри этой какой-то файл,
то этот файл должен удалиться первым (так как файлу положено жить только одну минуту, а папкам две).
Вам понадобятся библиотеки os и shutil. Внимательно перечитайте задание и учтите возможные ошибки.
'''

import os
import shutil
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Deleted directory", type=str)
path = parser.parse_args().directory


def time_del(directory):
    arr = os.listdir(directory)

    if (time.time() >= os.stat(directory).st_atime + 60):
        shutil.rmtree(directory)
        return

    for i in arr:
        stat = os.stat(directory + str(i))
        if ((os.path.isfile(directory + str(i))) and (time.time() >= stat.st_atime + 30)):

            os.remove(directory + str(i))

        if ((os.path.isdir(directory + str(i))) and (time.time() >= stat.st_atime + 60)):
            shutil.rmtree(dir + str(i))

        if (os.path.isdir(directory + str(i)) and os.path.exists(dir + str(i))):
            time_del(dir + str(i) + "/")


while True:
    try:
        time_del(path)
    except FileNotFoundError:
        print("File deleted")
        break
