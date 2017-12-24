from bs4 import BeautifulSoup
from collections import Counter
import requests
from string import punctuation

r = requests.get("http://en.wikipedia.org/wiki/Wolfgang_Amadeus_Mozart")

soup = BeautifulSoup(r.content, "html5lib")

text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
print (c.most_common(5)) # prints most common words staring at most common.