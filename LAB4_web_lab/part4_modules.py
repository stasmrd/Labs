# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261
import hashlib

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import re
import time
import requests
from urllib.parse import urlparse , urljoin

print("---------35----------")

def urllib_parse_urlparse():
    url = "https://cybercor.org/path?x=1#top"
    parsed = urlparse(url)
    print("Descompunere URL: ", url)
    print("Scheme: ", parsed.scheme)
    print("Netloc: ", parsed.netloc)
    print("Path: ", parsed.path)
    print("Query: ", parsed.query)
    print("Fragment: ", parsed.fragment)
    return parsed

urllib_parse_urlparse()
print("---------36---------")

def urllib_parse_urljoin():
    relatives = ["/about", "contact.html", "../index.html"]
    print("Compunere URL:\n",urljoin(BASE_URL, relatives[0]))
    print(urljoin(BASE_URL, relatives[1]))
    print(urljoin(BASE_URL, relatives[2]))
    return list(set(relatives))

urllib_parse_urljoin()
print("---------37---------")

def extract_links(html):
    legaturi = re.findall(r'href="([^"]+)"', html)
    return legaturi

html_exemplu = """<a href="https://cybercor.org/#servicii">Servicii</a>
                    <a href="https://pwn.college/dojos">Dojos</a> """

print("Extragerea legaturilor:",extract_links(html_exemplu))
print("---------38---------")

def split_links(links, domain):
    lst_in = []
    lst_ex = []
    for link in links:
        if domain in link:
            lst_in.append(link)
        else:
            lst_ex.append(link)
    return lst_in, lst_ex

lnk = ["https://cybercor.org", "https://cybercor.org/home", "https://pwn.college/dojos", "https://google.com"]
dmn = "https://google.com"

print(split_links(lnk, dmn))
print("---------39---------")

from html.parser import HTMLParser


class ImageFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "img":
            src = dict(attrs).get("src")
            if src:
                self.images.append(src)


test_html = """
<html><body>
  <img src="/logo.png" alt="Logo">
  <IMG SRC="poza.jpg">
  <img alt="imagine fără src">
  <img src="https://cdn.example.com/banner.webp" />
  <a href="/despre">Aceasta nu este o imagine</a>
</body></html>
"""

finder = ImageFinder()
finder.feed(test_html)
print(finder.images)

assert finder.images == [
    "/logo.png",  # imagine obișnuită
    "poza.jpg",  # tag scris cu majuscule
    "https://cdn.example.com/banner.webp",  # tag care se închide singur
], "Parserul nu a găsit exact imaginile așteptate"
print("Testul a trecut!")

response = requests.get(BASE_URL, timeout=TIMEOUT)
finder = ImageFinder()
finder.feed(response.text)
print(len(finder.images), "imagini găsite")
for src in finder.images:
    print(src)

print("---------40---------")

def page_fingerprint(url):
    resp = requests.get(url, timeout=TIMEOUT)
    return hashlib.sha256(resp.content).hexdigest()

print(page_fingerprint("https://www.bbc.com/news"))
time.sleep(30)
print(page_fingerprint("https://www.bbc.com/news"))
# Rezultate vor fi diferite in cazul cand site-ul respectiv se actualizeaza
# intr-un timp foarte scurt si cand folosim functia la o anumita distanta de timp,
# de dorit mai mare ca 1, in dependenta de site.

print("---------41---------")

