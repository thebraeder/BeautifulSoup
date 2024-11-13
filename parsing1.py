
import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# ua = UserAgent()


# print(ua.random)
# url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"



url = "https://books.toscrape.com/"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'}
params = {"ref_":"books.toscrape.com"}

session = requests.session()

response = session.get(url+"/intl",params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")


rows = soup.find_all('tr')

films = []


for row in rows[2:]:
    film = {}
    area_info = row.find('a', {'class': 'price_color'})
    film['area'] =[area_info.getText(), url + area_info.get('href')]

    print()