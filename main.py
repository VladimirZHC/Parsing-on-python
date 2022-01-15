import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

url = 'https://itproger.com/'
session = requests.Session()
try:
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        soup = bs4(req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'article'})
        for div in divs:
            title = div.find('a').text
            href = div.find('a')['href']
            print(f'{title} -https://itproger.com/{href}')
    else:
        print('Ошибка')
except Exception:
    print('Ошибка в самом Url-адресе')