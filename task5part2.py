"""Консольная утилита, использующая argparse.
 Утилита принимает позиционный аргумент dirpath - это директория, внутри которой утилита создаст новую папку.
 Название новой папки будет зависеть от указанных опций. Если указана опция -y, то в назнании присуствует текущий год.
 Если -m, то номер текущего месяца. Если -d, то номер текущего дня. Опции можно комбинировать.
 Если папка с заданным названием уже существует, то выводится предупреждение.
 Если не указано ни одной опции, то утилита создает папку с именем 'unknown'."""

import argparse
import datetime
import os
import sys

parser = argparse.ArgumentParser()
dirpath = ""
date = datetime.datetime.now()
parser.add_argument("-year", "-y", action="store_true", help="add year")
parser.add_argument("-month", "-m", action="store_true", help="add month")
parser.add_argument("-day", "-d", action="store_true", help="add day")
parser.add_argument("path", type=str, help="dirpath")
args = parser.parse_args()

if len(sys.argv) == 2:
    try:
        os.mkdir(args.path + "Unknown")
    except OSError:
        print("Directory exists")

else:
    if (args.year):
        dirpath = str(date.year) + "-"

    if (args.month):
        dirpath += str(date.month) + "-"

    if (args.day):
        dirpath += str(date.day) + "-"

    try:
        os.mkdir(args.path + dirpath[:len(dirpath) - 1])
    except OSError:
        print("Directory exists")
