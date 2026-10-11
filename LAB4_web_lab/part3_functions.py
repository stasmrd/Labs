# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261

import requests
import time


BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def get_status(url:str) -> int:
    """Returnează codul de stare HTTP pentru adresa url."""
    print("url = ", url)
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

print("---------21----------")
def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
print(fetch(BASE_URL))
print("---------22----------")

print(get_status(BASE_URL + "/"))
time.sleep(1)

apel1 = "/robots.txt"
print(get_status(BASE_URL + apel1))
time.sleep(1)
apel2 = "/sitemap.xml"
print(get_status(BASE_URL + apel2))
print("---------23----------")


def fetch_mod(url,tmt = 10):
    response = requests.get(url, timeout = tmt)
    return response.status_code

print(fetch_mod(BASE_URL))
print(fetch_mod(BASE_URL, 3))
print("---------24----------")


def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    title = html[start:end].strip()
    return title

response = requests.get(BASE_URL, timeout=TIMEOUT)
print(get_title(response.text))
print("---------25----------")

def get_title():
    """Acesta este un docstring facut de Stas :D"""
    return None

help(get_title)
print("---------26----------")
# get_status(123)
print("---------27----------")
