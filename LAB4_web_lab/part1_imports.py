# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 # secunde

# Exercitiul 1

import time
import urllib.request
import requests

print("Versiunea requests: ", requests.__version__)
print()

# Exercitiul 2

response1 = requests.get(BASE_URL, timeout=TIMEOUT)
print("Codul de stare (Stil 1): ", response1.status_code)
print()

time.sleep(1)

from requests import get 
response2 = get(BASE_URL, timeout=TIMEOUT)
print("Codul de stare (Stil 2): ", response2.status_code)
print()

# Exercitiul 3

import requests as rq
response3 = rq.get(BASE_URL, timeout=TIMEOUT)
print("Codul de stare (ex.3): ", response3.status_code)
print()

time.sleep(1)

# Exercitiul 4
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
print()

# Exercitiul 5

print(dir(requests))

stasik = dir(requests)
print()
print(f"stasik = {stasik}")
print()

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
print("Cod de stare (Stil 6): ", response6.status_code)
print()


# Exercitiul 7
time1 = time.perf_counter()
print("Time 1 = ", time1)
response7 = requests.get(BASE_URL, timeout=TIMEOUT)
time2 = time.perf_counter()
print("Time 2 = ", time2)
print(response7.elapsed)
print()

# Exercitiul 8
try :
    import bs4
except:
    print("Instalați modulul cu: pip install beautifulsoup4")

#print(bs4.__file__)

