from bs4 import BeautifulSoup
import requests

url = "https://www.lanacion.com.ar/"
page = requests.get(url)   
soup = BeautifulSoup(page.content,"html.parser")
content_titles = soup.find_all('h2','com-title')
print(":::::::::::::::TITULARES::::::::::::")
for tit in content_titles:
    sub = tit.find_all('a')
    print(sub[0].attrs.get('title'))    #con attrs.get me traigo el atributo que yo quiera de sub. en este caso me traigo el title.
    print("https://www.lanacion.com.ar"+sub[0].attrs.get('href'))
    print("")
