from bs4 import BeautifulSoup
import requests

url = "https://www.instagram.com/"
page = requests.get(url)   
soup = BeautifulSoup(page.content,"html.parser")
usuarios = soup.find_all('div', class_='e1e1d')
print(usuarios)


