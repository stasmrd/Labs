import webtools
from webtools import get_title , security_headers

BASE_URL = "https://cybercor.org"

webtools.get_title(webtools.fetch(BASE_URL).text)

# Daca voi folosi o functie proprie get_title atunci acea din import va fi ignorata
# iar in locul ei, va rula functia mea.