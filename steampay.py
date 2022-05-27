import requests
from bs4 import BeautifulSoup
from threading import Thread


class SteamPay:
    """
        parsing steampay.com for games
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

        self.start(f"https://steampay.com/search?q={search}")
        th = Thread(target=self.kek)
        th.start()

    def start(self, url):
        response = requests.get(url)

        soup = BeautifulSoup(response.text, features="html.parser")


        elements = soup.find_all("a", class_="catalog-item")
        for i in elements:
            name = i.find_next("div", class_="catalog-item__name").text.split("\n")[1]
            href = "https://steampay.com" + i.get("href")
            price = i.find_next("div", class_="catalog-item__price")
            price = price.find_next("span", class_="catalog-item__price-span").text.split("\n")[1]
            try:
                price = float(price[:-1])
            except:
                price = 0.0
            if (self.key in name.lower()) and self.notKey not in name.lower() and price != 0:  # Убираем аккаунты из списка
                self.lst.append([[price], [name], [href]])

    def kek(self):
        print()
        self.lst.sort()

        def f(l):
            n = []
            for i in l:
                if i not in n:
                    n.append(i)
            return n

        lst = f(self.lst)

        for i in lst:
            text = str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]) + "\n"
            print(text)

        print(len(lst))
        input()

