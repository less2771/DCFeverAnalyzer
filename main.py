import requests
from bs4 import BeautifulSoup

def get_data():
    response = requests.get('https://www.dcfever.com/trading/listing.php?id=84&page=1')
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def main():
    data = get_data()
    result = data.find_all("ul", class_="item_list")
    item_list = []
    for item in result:
        print(item.text)
        item_list.append(item.text)
        
    print(item_list)
    
    
    
    
if __name__ == '__main__':
    main()