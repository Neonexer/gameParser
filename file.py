from steampay import SteamPay
from platiru import PlatiRu
from megakeys import MegaKeys

print("""
Plati.ru -> 1
Megakeys.info -> 2
Steampay.com -> 3""")

while True:
    try:
        answer = int(input())
    except:
        continue
    match answer:
        case 1:
            search = input("Search:")
            key = input("Key:")
            notKey = input("NotKey:")
            PlatiRu(search, key, notKey)
            break
        case 2:
            search = input("Search:")
            key = input("Key:")
            notKey = input("NotKey:")
            MegaKeys(search, key, notKey)
            break
        case 3:
            search = input("Search:")
            SteamPay(search)
            break
        case _:
            continue