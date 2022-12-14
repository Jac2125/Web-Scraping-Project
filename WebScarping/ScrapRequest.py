from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
html_text = requests.get('https://www.bestbuy.ca/en-ca/category/gaming-desktop-computers/30441', headers= headers).text
soup = BeautifulSoup(html_text,'lxml')
computers = soup.find_all('div', class_ = 'col-xs-8_1v0z0 col-sm-12_G_a2r productItemTextContainer_HocvR')

for computer in computers:
    computer_price = computer.find('span', class_ = 'screenReaderOnly_2mubv large_3uSI_').text
    computer_description = computer.find('div', class_ = 'productItemName_3IZ3c').text
    available_via_ship = computer.find('span', class_ = 'container_1DAvI').text
    available_via_store = computer.find('p', class_ = 'availabilityMessageSearchPickup_1h9CR').text

    print(f'''
    Price : {computer_price}
    Spec : {computer_description}
    Shippinng available = {available_via_ship}
    Remaining stock = {available_via_store}
    ''')