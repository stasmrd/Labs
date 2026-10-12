# Laborator Python: funcții, metode și importuri pe web
# Student: Mardari Stanislav
# Grupa academica : SI-261


BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10  # secunde


from urllib.parse import urlparse

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

