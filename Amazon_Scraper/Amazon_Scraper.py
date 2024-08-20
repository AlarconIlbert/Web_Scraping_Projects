from datetime import datetime
import requests
import csv
import bs4

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',

}

def get_page_html(url):
    res = requests.get(url=url, headers=REQUEST_HEADER)
    return res.content

def get_product_price(soup):
    main_price_span = soup.find('span', attrs={'class': 'a-offscreen'})
    if main_price_span:
        price = main_price_span.text.strip().replace('US$', '').replace('$', '')
        return price
    return None

def get_product_title(soup):
    product_title = soup.find('span', id='productTitle')
    return product_title.text.strip()

def get_product_rating(soup):
    product_title = soup.find('span', id='acrPopover')
    return product_title.text.strip()

def get_product_technical_details(soup):
    details={}
    technical_details_section = soup.find('div', id='prodDetails')
    date_table = technical_details_section.findAll('table',class_='a-keyvalue prodDetTable')
    for table in date_table:
        table_rows = table.findAll('tr')
        for row in table_rows:
            row_key = row.find('th').text.strip()
            row_value = row.find('td').text.strip().replace('\u200e','')
            details[row_key] = row_value
    return details


def extract_product_info(url):
    product_info = {}
    print(f'Scraping URL: {url}')
    html = get_page_html(url=url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    product_info['rating'] = get_product_rating(soup)
    product_info.update(get_product_technical_details(soup))
    print(product_info)
    return product_info

if __name__ == "__main__":
    with open('amazon_products_url.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            url = row[0]
            extract_product_info(url)