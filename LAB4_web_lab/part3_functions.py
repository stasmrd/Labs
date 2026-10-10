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
    response = requests.get(BASE_URL, timeout=TIMEOUT)
    return response.status_code

# Exercitiul  21
def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code
print(fetch(BASE_URL))
print("-------")

# Exercitiul 22
print(get_status(BASE_URL))
print()
time.sleep(1)
apel1 = "/robots.txt"
print(get_status(BASE_URL + apel1))
time.sleep(1)
apel2 = "/sitemap.xml"
print(get_status(BASE_URL + apel2))


