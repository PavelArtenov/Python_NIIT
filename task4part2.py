'''
Напишите класс WrapStrToFIle, который будет иметь одно вычисляемое свойство (property) под названием content.
В конструкторе класс должен инициализовать атрибут filepath, путем присваивания результата функции mktemp
библиотеки tempfile. При попытке чтения свойства content должен внутри кода свойства открываться файл,
используя атрибут filepath (с помощью функции open,
из этого файла читается все содержимое и возвращается из свойства.
Если файл не существует, то возникает ошибка, поэтому должна быть обертка вокруг открытия
файла на чтение (try...except),  с помощью которого будет возвращаться 'Файл еще не существует'.
При присваивании значения свойству content файл по указанному пути должен открываться
на запись и записываться содержимое. Не забудьте закрывать файл после чтения или записи.
При удалении атрибута content, должен удаляться и файл. Продолжение на слайде ниже.
'''
import os
import tempfile

class WrapStrToFile:
    def __init__(self):
        # здесь инициализируется атрубут filepath, он содержит путь до файла хранилища
        self.filepath = tempfile.mktemp()
        print(self.filepath)



    @property
    def content(self):
        #попытка чтения из файла, в случае успеха возвращаем содержимое
        #в случае неудачи возвращаем "Файл еще не сущетсвует"
        try:
            file = open(self.filepath,"r")
            string = file.read()
            file.close()
            return string
        except FileNotFoundError:
            print("Файл еще не существует")



    @content.setter
    def content(self,value):
        #Запись в файл указанного содержимого
        try:
            file = open(self.filepath,"a")
            file.write(value + "\n")
        except FileNotFoundError:
            print("Не удалось осуществить запись в файл")
        else:
            file.close()


    @content.deleter
    def content(self):
        #удаляем файл через функцию unlink
        try:
            os.unlink(self.filepath)
        except OSError:
            print("Нет такого файла")



one = WrapStrToFile()
print(one.content)
one.content = "Text file"
print(one.content)
one.content = "Text file 2"
print(one.content)
del one.content






