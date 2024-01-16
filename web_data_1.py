import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl

# Ignore the ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Open the link and parse
url = urllib.request.urlopen('https://en.wikipedia.org/wiki/Jellyfish')
bs = BeautifulSoup(url, 'html.parser')

# Convert data to text format
paragraphs = bs.find_all('p')
url_text = '\n'.join(bs.text for paragraph in paragraphs)

# Input the question
question = input('Enter your key word: ')

# Print the data only after the word I write down
if question:
    found_word = False
    for paragraph in paragraphs:
        if question in paragraph.text:
            found_word = True
            data = paragraph.find_all_next(text = True)
            print(' '.join(data))
            break
    if not found_word:
        print(f"Data for '{question}' not found in webpage")
else:
    print('Use different key word')