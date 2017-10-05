'''
Парсинг (разбор) html страничек очень часто предлагают в качестве тестового задания для оценки способностей.
Напишите класс, который запрашивает содержимое веб-странички с помощью стандартной библиотеки urllib.request
и вытаскивает у нее заголовок (содержимое тэга title) любым придуманным вами способом (с помощью стандартной
или скаченной библиотеки, как угодно). Например, если вы скачаете страничке по адресу "http://python.org/",
то можете найти у нее указанный тег и текст внутри него - "<title>Welcome to Python.org</title>"
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
print(ob.multistream())
