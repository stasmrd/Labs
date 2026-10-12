# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde

print("---------9----------")
import requests

response = requests.get(BASE_URL)

print(response.status_code)  #atribut
print(response.ok)  #atribut
print(response.url)  #atribut
print(response.encoding)  #atribut
print("---------10----------")

try:
    response2 = requests.get(BASE_URL + "/this-page-does-not-exist")
    response2.raise_for_status()
    print(response2.status_code)
except requests.HTTPError as e:
    print("Din pacate ceva nu a mers.")
    print(e)

print("---------11----------")

response3 = response.headers.items()
print(response3)
print("---------12----------")

response4 = response.headers.get("Server", "lipseste")
print(response4)
response5 = response.headers.get("Content-Type", "lipseste")
print(response5)
print()
response6 = response.headers.get("server", "lipseste")
print(response6)
response7 = response.headers.get("content-type", "lipseste")
print(response7)
print("---------13----------")
# am observat ca la folosirea functiei response.headers.get ,
# folosirea literelor mari sau mici nu au absolut niciun efect,
# ambele vor returna aceeasi chestie, nu are vreo importanta

response8 = response.text.lower().count("cyber")
print(response8)
print("---------14----------")

# .lower() transformă textul în litere mici și ne dă înapoi tot un text,
# pentru că rezultatul este în continuare un text, putem lipi imediat după el .count() pentru a număra cuvântul.

html = response.text
start = response.text.find("<title>") + len("<title>")
end = response.text.find("</title>")
title = html[start:end].strip()
print(title)
print("---------15----------")

lines = html.splitlines()
max_line = len(max(lines, key = len))
counter = len(lines)
print(counter)
print(lines)
print(max_line)
print("---------16----------")

verify_security = BASE_URL.startswith("https://")
if verify_security:
    print("Conexiune securizata.")
else:
    print("Conexiune nesecurizata.")
print("---------17----------")

BASE_URL_unsecure = "http://cybercor.org"
response = requests.get(BASE_URL_unsecure)
response17 = response.history
for resp in response17:
    print(f"Cod de stare: {resp.status_code}\nURL: {resp.url}")
print(f"\nURL final: {response.url}")
print("---------18----------")

response18 = requests.head(BASE_URL)
print(response18.status_code)
print()
response19 = requests.get(BASE_URL)
print(f"Status code: {response18.status_code}")
print(f"Cerere HEAD len: {len(response18.content)}")
print()
print(f"Status code: {response19.status_code}")
print(f"Cerere GET len: {len(response19.content)}")
print("---------19----------")

# Cererea head() aduce doar header-ele HTTP (fara corp), de asta len(response_head.content) e 0.
# Cererea get() descarca si corpul paginii, deci are o lungime mai mare de 0 bytes.

resp_cookie = response19.cookies
if len(resp_cookie) == 0:
    print("Niciun cookie setat.")
else:
    for cook in resp_cookie:
        print(f" COOKIE NAME: {cook.name}")
        print(f" COOKIE SECURE: {cook.secure}")
print("---------20----------")

session = requests.Session()
session.headers.update({"User-Agent": "WebLab-Stas"})
cerere = session.get(ECHO_URL + "/headers")
print(f"Cerere text: {cerere.text}")
print(f"Cerere json: {cerere.json()}")
user_agent_trimis = cerere.json().get("headers", {}).get("User-Agent")
print(f"User-Agent confirmat: {user_agent_trimis}")
print("---------------------")