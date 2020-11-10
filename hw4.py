import requests
from bs4 import BeautifulSoup
import json

keyword= 'ring'
#page_number= '5'
results=[]

headers= {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0'
}

for i in range(1,11):
    #r = requests.get(' https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw='+keyword)
    r=requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+keyword+'_pgn='+str(i), headers=headers)
    print('r.statuscode=', r.status_code) 

    soup = BeautifulSoup(r.text, 'html.parser')

    '''

    items = soup.select('.s-item__title')
    for item in items:
        print('item=', item.text)  

    prices = soup.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .clearfix.s-item__details > div.s-item__detail--primary.s-item__detail > .s-item__price')
    for price in prices:
        print('price=', price.text )

    statuses = soup.select('.SECONDARY_INFO')
    for status in statuses:
        print('status=', status.text)
    '''

    boxes = soup.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper')
    for box in boxes:
        #print('--- ')
        result= {}
        titles = box.select('.s-item__title')
        for title in titles:
            #print('title=', title.text)
            result['title'] =title.text  
        prices = box.select('.clearfix.srp-list.srp-results > li.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .clearfix.s-item__details > div.s-item__detail--primary.s-item__detail > .s-item__price')
        for price in prices:
            #print('price=', price.text )
            result['price']= price.text
        statuses = box.select('.SECONDARY_INFO')
        for status in statuses:
            #print('status=', status.text)
            result['status']= status.text
        #print('results=', result)
        results.append(result)

    print('len(results)=', len(results))

j= json.dumps(results)
with open('items.json', 'w') as f:
    f.write(j)
#print('j=', j)
