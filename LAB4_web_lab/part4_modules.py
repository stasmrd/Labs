# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261


BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

import re
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

