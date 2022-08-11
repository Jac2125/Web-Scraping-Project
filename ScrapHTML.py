from bs4 import BeautifulSoup

with open('pc.html', 'r', encoding="utf8") as html_file:
    content = html_file.read()
    #print(content)
    
    soup = BeautifulSoup(content, 'lxml')
    
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