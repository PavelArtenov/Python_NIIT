'''
Напишите функцию to_roman, которая принимает целое число, а возвращает строку,
отображающую это число римскими цифрами. Например, на вход подается 6, вернет "VI".
Например, на вход подается 23, вернет "XXIII". Входные данные должны быть в диапазоне
от 1 до 5000, если подается число не в этом диапазоне или не число, то должны
выбрасываться ошибка типа NonValidInput. Этот тип ошибки вы должны создать сами.
Также необходимо в папке с файлом, содержащей вашу функцию, создать файл tests.py,
внутри которой необходимо определить тесты для вашей функции.
Тесты должны покрывать все возможные поведения функции,
включая порождения ошибки при плохих входных данных.
'''

class NonValidInput(Exception):
    pass


def to_roman(x):
    if ((x > 5000) or (x < 1)):
        raise NonValidInput

    one = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    ten = {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    hundred = {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
    thousand = {1: "M", 2: "MM", 3: "MMM", 4: "MMMM", 5: "MMMMM"}
    arr_roman = [one, ten, hundred, thousand]
    length = len(str(x))
    roman = []
    i = 0

    while (length > 0):
        num = x % 10
        x //= 10
        if (num != 0):
            roman.insert(0, arr_roman[i].get(num))
        length -= 1
        i += 1

    roman_number = "".join(roman)
    return roman_number


print(to_roman(4321))
