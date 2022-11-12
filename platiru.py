import requests
from bs4 import BeautifulSoup
from threading import Thread
from flask import Flask, render_template, request, redirect, url_for
import time, webbrowser

app = Flask(__name__)

@app.route('/')
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      name = request.form['name']
      key = request.form['key']
      global content
      content = []
      a = PlatiRu(name, key)
      time.sleep(13)
      return render_template("login.html", content=a.__str__())
      # return """<style>
      #   body{
      #       background-color: grey;
      #   }
      #   </style><form action = "http://localhost:5000/login" method = "post" style="text-align: center;
      #  background-color: silver; padding-right: 650px; padding-left: 650px">
      #    <p><b>Game:</b></p>
      #    <p><input type = "text" name = "name" /></p>
      #    <p><input type = "key" name = "key" /></p>
      #    <p><input type = "submit" value = "submit" /></p>
      # </form>""" + f"""<div style="text-align: center;
      #  background-color: silver;">{a.__str__()}</div>"""
   else:
      user = request.args.get('name')
      return render_template('login.html')


content = []

class PlatiRu:
    """
    parsing plati.ru for games
    """

    def __str__(self):
        global content
        # result = ""
        # for i in content:
        #     price = i[0][0]
        #     cells = i[0][1]
        #     name = i[0][2]
        #     href = i[0][3]
        #     img = i[0][4]
        #     #result += f"<div>{price} : {cells} : <b><i>{name}</i></b> : <a href={href}>Ссылка</a></div>"
        #     result += f"{price} : {cells} : {name} : {href}"
        #     print(i[0])
        try:
            return content
        except:
            return "Error"

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
        img = soup.find("img")["src"]
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
                self.lst.append([[price], ["Продаж - ", sells], [name], [href], [img]])

    def kek(self):
        global content
        print("\n", "-" * 100, "\n")
        time.sleep(10)
        self.lst.sort()
        #self.lst = self.lst[::-1]

        def f(l):
            n = []
            for i in l:
                if i not in n:
                    n.append(i)
            return n

        lst = f(self.lst)

        for i in lst:
            text = str(i[0][0]) + " : " + str(i[1][0]) + str(i[1][1]) + " : " + str(i[2][0]) + " : " + str(i[3][0]) + "\n"
            a = []
            a.append([str(i[0][0]), str(i[1][0]) + str(i[1][1]), str(i[2][0]), str(i[3][0]), str(i[4][0])])
            content.append(a)
            #print(text)

        print(len(lst))


if __name__ == "__main__":
    #PlatiRu(input("Search:"), input("Key:"), input("bad key:"))
    #PlatiRu("lego")
    #time.sleep(2)
    webbrowser.open("http://127.0.0.1:5000/")
    app.debug = False
    app.run()
    #app.run(host='0.0.0.0', port=5000)

