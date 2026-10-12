# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

import time
import urllib.request
import requests

print("--------------------")

print("Versiunea requests: ", requests.__version__)
print("---------1----------")

response1 = requests.get(BASE_URL, timeout=TIMEOUT)
print("Codul de stare: ", response1.status_code)
print("---------2----------")

time.sleep(1)

from requests import get 
response2 = get(BASE_URL, timeout=TIMEOUT)
print("Codul de stare: ", response2.status_code)
print("---------3----------")

import requests as rq
response3 = rq.get(BASE_URL, timeout=TIMEOUT)
print("Codul de stare: ", response3.status_code)
print("---------4----------")

time.sleep(1)

import urllib.request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
req = urllib.request.Request(BASE_URL, headers=headers)
with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
    status_code = response.status
    print("Cod de stare (urllib): ", status_code)
    
    content_bytes = response.read()
    content_text = content_bytes.decode("utf-8")

print("Primele 200 de caractere: ", content_text[:200])
time.sleep(1)
print("---------5----------")

print(dir(requests))

dir_req = dir(requests)
print()
print(f"Dir Request: = {dir_req}")
print("---------6----------")

# Am ales 3 nume din rezultatul funcției dir(requests):
#
# 1. get - Este o FUNCTIE.
#    Se foloseste pentru a efectua cereri HTTP de tip GET.
#
# 2. Response - Este o CLASA.
#    Reprezintă obiectul pe care îl returnează apelul requests.get() și conține 
#    starea cererii, antetele și corpul răspunsului.
#
# 3. exceptions - Este un MODUL (submodul).
#    Conține definițiile pentru diverse tipuri de erori.

# Exercitiul 6
response6 = requests.get(BASE_URL, timeout=5)
print("Cod de stare: ", response6.status_code)
print("---------7----------")

time1 = time.perf_counter()
print("Time 1 = ", time1)
response7 = requests.get(BASE_URL, timeout=TIMEOUT)
time2 = time.perf_counter()
print("Time 2 = ", time2)
print(response7.elapsed)
print("---------8----------")

try :
    import bs4
except:
    print("Instalați modulul cu: pip install beautifulsoup4")

print(bs4.__file__)
print("--------------------")


