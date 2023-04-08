import requests
from bs4 import BeautifulSoup
import csv

key = 'hotels'
location = 'london'
url = 'https://www.yell.com/ucs/UcsSearchAction.do?keywords={}&location={}&scrambleSeed=1113185796&pageNum=2'.format(key,location)

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

req = requests.get(url, headers=headers)
print(req)