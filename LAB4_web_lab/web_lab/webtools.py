import requests
TIMEOUT = 10

def fetch(url):
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code


def get_status(url:str) -> int:
    """Returnează codul de stare HTTP pentru adresa url."""
    print("url = ", url)
    response = requests.get(url, timeout=TIMEOUT)
    return response.status_code


def get_title(html):
    start = html.find("<title>") + len("<title>")
    end = html.find("</title>")
    title = html[start:end].strip()
    return title


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