import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent

url = 'https://kups.club/'

user = fake_useragent.UserAgent().random
headers = {"user-agent": ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, "lxml")
products = soup.find_all('div', class_='row mt-4')
for product in products:
    title_products = product.find('h3', class_='card-title')
    print(title_products.text)

