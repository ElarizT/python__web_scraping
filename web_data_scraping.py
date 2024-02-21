# This code is for to print multiple lines of(3 lines here) paragraph after a key word(header)
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

# Input the heading
question = 'Anatomy'

# Print the data only 3 lines after the heading
found_word = False
lines_after_header = 3
lines_printed = 0

for word in bs.find_all('span', {"class": 'mw-headline'}):
    if question.lower() in word.text.lower():
        found_word = True
        next_element = word.find_next()
        while next_element and lines_printed < lines_after_header:
            if next_element.name == 'p':
                print(next_element.text)
                lines_printed += 1
            next_element = next_element.find_next()
if not found_word:
    print(f"Header '{question}' not found on the webpage.")

elif lines_printed < lines_after_header:
    print(f"Insufficient element for the '{question}' key word")
