from bs4 import BeautifulSoup
import requests

url = "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
texto = soup.find_all('p')
print soup
print(texto[0].get_text())


outer= soup.find_all('p', class_='outer-text')

print (outer[0].get_text())
print (outer[1].get_text())