#json objesi

import requests



url = "http://api.fixer.io/latest?base="

birinci_doviz = input("Birinci Döviz:")

ikinci_doviz = input("İkinci Döviz:")

miktar =  float(input("Miktar"))


response = requests.get(url + birinci_doviz)


veri =  response.json()

try:
    print(float(veri["rates"][ikinci_doviz]) * miktar)
except KeyError:
    print("Lütfen para birimlerini kontrol edin")