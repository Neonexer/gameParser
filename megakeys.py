import requests
from bs4 import BeautifulSoup
from threading import Thread
import time


class MegaKeys:
    """
    parsing megakeys.info for games
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
            th = Thread(target=self.start, args=(f"https://megakeys.info/pc-games/search.php?searchstr={search}&sort=price",))
            th.start()

        th = Thread(target=self.kek)
        th.start()
        print("started")

    def start(self, url):
        response = requests.get(url)

        soup = BeautifulSoup(response.text, features="html.parser")

        elements = soup.find_all('div', class_="items_listnew")
        for i in elements:
            a = i.find_next("a", class_="item_listnew")
            href = "https://megakeys.info/" + a.get("href")
            name = a.find_next("span").text
            price = float(i.find_next("div", class_="pricenew").text)

            if ((
                        "key" in name.lower() or "ключ" in name.lower()) and self.key in name.lower()) and self.notKey not in name.lower():  # Убираем аккаунты из списка
                self.lst.append([[price], [name], [href]])

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
            text = str(i[0]) + " : " + str(i[1]) + " : " + str(i[2]) + "\n"
            print(text)

        print(len(lst))
        input()