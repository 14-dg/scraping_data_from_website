from bs4 import BeautifulSoup
import requests

url = 'https://www.stackfield.com/de/pricing'

data = requests.get(url)
doc = BeautifulSoup(data.text, 'html.parser')
#print(doc.prettify)

prices = doc.find_all(text='€')
print(prices)
for i, price in enumerate(prices):
    parent = price.parent.parent
    #print(parent)
    span = parent.find_all("span")
    print(parent.string)