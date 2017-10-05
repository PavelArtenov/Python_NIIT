'''
Создайте класс, один из методов которого способен принимать не одиночный url,
а массив url'ов и возвращать массив строк, полученных  из заголовков html страницек,
которые вы получите из этих заданных url'ов.
Используйте ThreadPoolExecutor из библиотеки concurrent.futures.
Его максимальное количество воркеров должно быть равно количеству ядер на компьтере.
Получение каждого отдельного урла должно запускаться с помощью метода submit у ThreadPoolExecutor.
Получение результата от отдельного урла должно происходить через объект Future,
который вернет метод submit. Подробности в документации.
Проверьте работу вашего класса с помощью любых 20 url'ов.
'''

import urllib.request
import re
from concurrent.futures import ThreadPoolExecutor , as_completed
import multiprocessing


class Title:
    def __init__(self,arr):
        self.arr = arr

    def cut_title(self,url):
        for site in url:
            doc = urllib.request.urlopen(url)
            html = doc.read().decode('utf-8')
            result = re.findall("<title>.*</title>", html)
            string = result[0]
            return (string[7:len(string) - 8])

    def multistream(self):
        title_arr = []
        with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as pool:
            results = [pool.submit(self.cut_title, i) for i in self.arr]

            for future in as_completed(results):
                title_arr.append(future.result())

        return title_arr



arr_site = [
            'https://nikiladonya.github.io/',
            'https://github.com/',
            'http://nnportal.org/',
            'https://habrahabr.ru/',
            'https://nn.hh.ru/',
            'https://pythonworld.ru/',
            'https://www.apple.com/',
            'https://Twitter.com/',
            'https://ru.wikipedia.org/',
            'http://www.shtanyuk.tk/',
            'https://docs.oracle.com/',
            'http://www.spacex.com/',
            'https://www.tesla.com/',
            'https://geekbrains.ru/',
            'https://www.ebay.com/',
            'https://ru.aliexpress.com/ru_home.htm',
            'https://mail.ru/',
            'https://yandex.ru/',
            'https://www.avito.ru/',
            'https://www.gismeteo.ru/',
           ]

ob = Title(arr_site)
for i in ob.multistream(): print(i)
