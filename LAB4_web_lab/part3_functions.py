# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261

import requests
import time


BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


def get_status(url):
    """Returnează codul de stare HTTP pentru adresa url."""
    print("url = ", url)
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code

# Exercitiul  21
def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
print(fetch(BASE_URL))
print("-------")

# Exercitiul 22
print(get_status(BASE_URL + "/"))
time.sleep(1)

apel1 = "/robots.txt"
print(get_status(BASE_URL + apel1))
time.sleep(1)
apel2 = "/sitemap.xml"
print(get_status(BASE_URL + apel2))
print("------------------")

# Exercitiul 23

def fetch_mod(url,tmt = 10):
    response = requests.get(url, timeout = tmt)
    return response.status_code

print(fetch_mod(BASE_URL))
print(fetch_mod(BASE_URL, 3))
print("--------------")

# Exercitiul 24
def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    title = html[start:end].strip()
    return title

response = requests.get(BASE_URL, timeout=TIMEOUT)
print(get_title(response.text))
