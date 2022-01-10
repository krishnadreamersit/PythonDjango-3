# Web Scraping
    # requests -> reading contents from website
    # pip install requests

import requests
url = "http://broadwayinfosys.com"
response = requests.get(url)
print(response.text)