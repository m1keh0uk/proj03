import argparse
import requests
from bs4 import BeautifulSoup
import json
import csv
import pprint

#get command line arguments
parser = argparse.ArgumentParser(description='bru')
parser.add_argument('search_term')
parser.add_argument('--pg_num', default=10)
parser.add_argument('--csv', action='store_true', help='make ouput csv instead of json')
args = parser.parse_args()
# print(args.search_term)

# page_number = 8

#list of all items on the ebay pages
items = []

for page_number in range(1,int(args.pg_num)+1):

    #make url
    url = 'https://www.ebay.com/sch/i.html?_nkw==' 
    url += args.search_term 
    url += '&_sacat=0&_from=R40&_pgn='
    url += str(page_number)
    # print('url=', url)

    #dl html
    r = requests.get(url)
    status = r.status_code
    # print('status=', status)
    html = r.text

    soup = BeautifulSoup(html, 'html.parser')
    tag_items = soup.select('.s-item')
    for tag_item in tag_items[2:]:
        name = None
        tags_name = tag_item.select('.s-item__title span')
        for tag in tags_name:
            # print('title=', tag.text)
            name = tag.text

        free_return = False
        tags_free_return = tag_item.select('.s-item__freeReturnsNoFee')
        for tag in tags_free_return:
            free_return = True

        items_sold = False
        tags_sold = tag_item.select('.s-item__quantitySold')
        for tag in tags_sold:
            items_sold = ''
            for char in tag.text:
                if char.isdigit():
                    items_sold += char
        
        price = False
        tags_price= tag_item.select('.s-item__price')
        for tag in tags_price:
            price_str = ''
            for char in tag.text:
                if char.isdigit():
                    price_str += char
        if price_str:
            price = int(price_str)

        status = False
        tags_status = tag_item.select('.SECONDARY_INFO')
        for tag in tags_status:
            status = tag.text

        shipping = False
        tags_shipping = tag_item.select('.s-item__logisticsCost')
        for tag in tags_shipping:
            shipping = ''
            for char in tag.text:
                if char.isdigit():
                    shipping += char
            if len(shipping) == 0:
                shipping = 0

        item = {
            'name': name,
            'price': price,
            'status': status,
            'shipping': int(shipping),
            'free_returns': free_return,
            'items_sold': items_sold

        }
        items.append(item)

pprint.pprint(items)

if args.csv:
    filename = f"{args.search_term}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=items[0].keys())
        writer.writeheader()
        for item in items:
            writer.writerow(item)
else:
    with open(f'{args.search_term}.json', 'w', encoding='ascii') as f:
        f.write(json.dumps(items))

