from bs4 import BeautifulSoup
from collections import Counter
import requests
from string import whitespace, punctuation
r = requests.get("http://www.literaturepage.com/read/prideandprejudice-1.html")

soup = BeautifulSoup(r.content, "html5lib")

text = (word.lower().strip(whitespace + punctuation)
        for element in soup.findAll('p')
        for text in element.findAll(text=True)
        for word in text.split())

words_to_exclude = {'a', 'the', 'of', 'it', 'is', 'it', 'and', 'in', 'he', 'he', 'to'}

Important = Counter(word for word in text if word not in words_to_exclude)

print(Important.most_common(6))

# This prints most common words staring at most common.
# We want to exclude the helper verbs, articles, and 'a.'
# We are going to have a predefined set of words that we just dont want to analyze.
