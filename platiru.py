import requests
from bs4 import BeautifulSoup
from threading import Thread
import time

class PlatiRu:
    """
    parsing plati.ru for games
    """

    def __init__(self, search, key="", notKey=""):

        self.lst = []

        search = search.replace(" ", "%20")
        if not len(key):
            self.key = " "
        else:
            self.key = key

        if not len(notKey):
            self.notKey = "JJKBHJBHJBHJGJNJKLNHJHJGGHVHBGH+++++1qrwerw"
        else:
            self.notKey = notKey

        for i in range(1, 31):
            th = Thread(target=self.start, args=(f"https://plati.market/search/{search}?id=" + str(i) + "&ai=601828",))
            th.start()

        th = Thread(target=self.kek)
        th.start()
        print("started")

    def start(self, url):
        response = requests.get(url)

        soup = BeautifulSoup(response.text, features="html.parser")

        elements = soup.find_all('li', class_="shadow")
        for i in elements:
            h1 = i.find_next("h1", style="font-size:12px;")

            name = h1.find_next('a').text

            price = h1.find_next('span').text
            priceTemp = price.split("/")
            price = priceTemp[1][1:-5]
            price = price.replace(",", ".")
            price = float(price)

            href = "https://plati.market/" + h1.find_next('a').get('href')

            try:
                sells = i.find_all_next("strong")
                sells = sells[1].text
            except:
                sells = "Error"

            if (("key" in name.lower() or "ключ" in name.lower()) and self.key in name.lower()) and self.notKey not in name.lower(): # Убираем аккаунты из списка
                self.lst.append([[price], ["Продаж - ", sells], [name], [href]])

    def kek(self):
        print("\n", "-" * 100, "\n")
        time.sleep(10)
        self.lst.sort()

        def f(l):
            n = []
            for i in l:
                if i not in n:
                    n.append(i)
            return n

        lst = f(self.lst)

        for i in lst:
            text = str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]) + " : " + str(i[3]) + "\n"
            print(text)

        print(len(lst))
        input()