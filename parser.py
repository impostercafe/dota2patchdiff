from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.dota2.com/patches/7.27c")
soup = BeautifulSoup(r.content)
print(soup.prettify())