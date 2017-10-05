'''
Напишите функцию odd_primes(end, start), которая ищет все простые числа в диапазоне от заданного числа
start (по умолчанию 3) до заданного числа end.
Запустите ее:
- Три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
- Также запустите ее три раза с теми же аргументами, но каждую в отдельной потоке с помощью  threading.Thread.
Не забудьте стартануть треды и дождаться их окончания.
- Также запустите ее три раза с теми же аргументами, но каждую в отдельной потоке с помощью  multiprocessing.Process.
Не забудьте стартануть процессы и дождаться их окончания.

Замерьте время исполнения каждого варианта. Подумайте над результатами.
И не запускайти эти скрипты в PyCharm в Debug режиме, это все замедлит.
'''

import random
import time
import threading
import multiprocessing


def odd_primes(start,end):
    arr = list (range(start,end,2))
    for i in arr:
        for j in arr:
            if (j<=i):
                continue
            else:
                if (j % i == 0):
                    arr.remove(j)

#1)Последовательный запуск
new_range = [[3,10000],
             [10001,20000],
             [20001,30000]]
start = time.time()
for i in range(3):
    odd_primes(new_range[i][0],new_range[i][1])
print("Execution in main thread = {}".format(time.time()-start))
#2)Запуск в отдельном потоке с помощью threading.Thread
start = time.time()
threads = []
for i in range(3):
    thr=threading.Thread(target=odd_primes,args=(new_range[i]))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()

print("Multithreading execution {} ".format(time.time() - start))

#3)Запуск в отдельном потоке с помощью multiprocessing.Process
start = time.time()
process = []
for i in range(3):
     p = multiprocessing.Process(target=odd_primes, args=(new_range[i]))
     p.start()
     process.append(p)

for p in process:
    p.join()

print('Multiprocessing execution: {}'.format(float(time.time() - start)))


"""
main thread - 3сек.
multithreading - 3сек.
multiprocessing - 1.5сек.
"""
