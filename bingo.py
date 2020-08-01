import requests
import re
from bs4 import BeautifulSoup as bs4

TEST=False
URL='https://bing.com'
Id="preloadBg"
regex='(?<=\=).*?(?=&)'

def download(link):
    global URL
    print('downloading ... ')
    name=re.search(regex,link).group(0)
    resp=requests.get(URL+link)
    open(name,'wb').write(resp.content)


print('please wait ... ')

if TEST:
    html=open('index.html').read()
else:
    resp=requests.get(URL)
    html=resp.content

soup=bs4(html,features='html5lib')

link=soup.find(id=Id)['href']

download(link)
