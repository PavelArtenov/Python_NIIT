'''
Напишите программу, которая выводит вместо чисел, кратных трем слово «Fizz»,
а вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»
'''

def FizzBuzz(arr):
    for num in arr:
        string = ""

        if (num % 3 == 0 and num != 0):
            string = "Fizz"

        if (num % 5 == 0 and num != 0):
            string += "Buzz"

        if string != "":
            index = arr.index(num)
            arr.pop(index)
            arr.insert(index, string)

    return arr


print(FizzBuzz([1, 2, 3, 4, 15, 5, 6, 7, 8, 9, 10, 30, 22, 19]))
