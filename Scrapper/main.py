from bs4 import BeautifulSoup
import requests

url = "https://www.lanacion.com.ar/"
page = requests.get(url)
soup = BeautifulSoup(page.content,"html.parser")
print(soup)
