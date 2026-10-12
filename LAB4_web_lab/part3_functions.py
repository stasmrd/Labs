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
print("Type Error")
# Adnotarile de tip nu blocheaza codul. Eroarea apare de la requests.get(),
# pentru ca a primit un numar in loc de un URL de tip text
print("---------27----------")

def page_exists(url):
    print("url = ", url)
    try:
        requests.get(url, timeout=TIMEOUT)
    except requests.RequestException:
        return False
    return True

print(page_exists("https://this-domain-does-not-exist.invalid"))
print("---------28----------")

paths = ["/", "/robots.txt", "/sitemap.xml"]
def check_paths(base, paths):
    dict_paths = {}
    for path in paths:
        full_paths = base + path
        resp = requests.get(full_paths)
        status_code = response.status_code
        dict_paths[path] = status_code
    print(dict_paths)
    return response.status_code

check_paths(BASE_URL,paths)
print("---------29----------")

def get_header(url, name , default = "Lipseste"):
    resp = requests.get(url, timeout=TIMEOUT)
    hdr = resp.headers.get(name, default)
    print(hdr)
    return None

get_header(BASE_URL, name = "Server")
print("---------30----------")

def security_headers(url):
    antete = ["Strict-Transport-Security", "X-Frame-Options",
            "Content-Security-Policy", "X-Content-Type-Options","Referrer-Policy"]
    resp = requests.get(url, timeout=TIMEOUT)
    ant_dict = {}
    for antet in antete:
        get_ant = resp.headers.get(antet, False)
        if get_ant:
            ant_dict[antet] = True
        else:
            ant_dict[antet] = get_ant
    print(ant_dict)
    return ant_dict

security_headers(BASE_URL)
print("---------31----------")

def score_headers(results):
    count_true = 0
    count_dict = len(results.keys())
    for key, val in results.items():
        if val: count_true += 1

    sir = f"{count_true}/{count_dict}"
    return sir

result_sh = score_headers(security_headers(BASE_URL))
print(result_sh)
print("---------32----------")

def fetch_robots(base):
    fisier = "/robots.txt"
    resp = requests.get(base + fisier, timeout=TIMEOUT)
    text = resp.text
    print(resp.status_code)
    if resp.status_code == 200:
        return text
    else:
        return None

def disallowed_paths(robots_text):
    if robots_text is None:
        return []

    paths = []
    for line in robots_text.splitlines():
        line = line.strip()
        if line.lower().startswith("disallow:"):
            path = line.split(":", 1)[1].strip()
            if path:
                paths.append(path)

    return paths

text_robots = fetch_robots(ECHO_URL)
lista_cai = disallowed_paths(text_robots)
print(text_robots)
print(lista_cai)
# Am folosit ECHO_URL in functia fetch_robots deoarece la BASE_URL nu exista Disallow.
print("----------33----------")

def response_times(*urls):
    dict_urls = {}
    for url in urls:
        resp = requests.get(url, timeout=TIMEOUT)
        sec = resp.elapsed.total_seconds()
        dict_urls[url] = sec
    return dict_urls

print(response_times(BASE_URL, ECHO_URL))
print("---------34----------")

def log(message, **details):
    parts = [message]
    for key, value in details.items():
        parts.append(f"{key}={value}")
    result = "  |  ".join(parts)
    return result

print(log("verificat", url=BASE_URL, status=200))

# print() doar afiseaza informatia pe ecran pentru
# a o putea vedea tu, dar nu o pastreaza in cod,dar
# return trimite valoarea inapoi in program, ceea ce
# iti permite sa o salvezi intr-o variabila si sa o folosesti
# mai departe in alte calcule sau functii.
print("---------------------")


