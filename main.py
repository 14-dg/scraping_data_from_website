from bs4 import BeautifulSoup
import requests

url = 'https://www.stackfield.com/de/pricing'

data = requests.get(url)
doc = BeautifulSoup(data.text, 'html.parser')
#print(doc.prettify)

euro = doc.find_all(text='€')
spans_complete = [euro[i].parent.parent.find_all('span') for i in range(len(euro))]
spans = list(map(lambda spans_list : [spans_list[1].string, spans_list[0].string], spans_complete))

print(spans)