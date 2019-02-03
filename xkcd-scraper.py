import requests, os, time
from bs4 import BeautifulSoup
from urllib.request import urlopen

xkcdUrl = 'http://xkcd.com/'
xkcdPage = urlopen(xkcdUrl)
soup = BeautifulSoup(xkcdPage, 'html.parser')
previousComic = ((soup.find("a", {"rel":"prev"})).attrs['href']).strip('/')
currentCommic = int(previousComic) + 1

count = currentCommic
while (count > 0):
    xkcdUrl = 'http://xkcd.com/'+str(count)
    xkcdPage = urlopen(xkcdUrl)
    count -= 1
    soup = BeautifulSoup(xkcdPage, 'html.parser')
    comicElement = soup.find("div", {"id": "comic" })
    comicImage = 'http:' + comicElement.find('img').attrs['src']
    print(comicImage)
    if (count % 5 == 0):
        time.sleep(10)
print()
