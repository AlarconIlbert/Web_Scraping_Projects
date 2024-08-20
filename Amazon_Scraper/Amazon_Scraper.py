from datetime import datetime
import requests
import csv
import bs4
import concurrent.futures
from tqdm import tqdm


USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
REQUEST_HEADER = {
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US, en;q=0.5',
}

NO_THREADS = 10

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


def extract_product_info(url, output):
    product_info = {}
    #print(f'Scraping URL: {url}')
    html = get_page_html(url=url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    product_info['price'] = get_product_price(soup)
    product_info['title'] = get_product_title(soup)
    product_info['rating'] = get_product_rating(soup)
    product_info.update(get_product_technical_details(soup))
    output.append(product_info)

if __name__ == "__main__":
    products_data = []
    urls = []
    with open('amazon_products_url.csv', newline='') as csvfile:
        urls = list(csv.reader(csvfile, delimiter=','))
    with concurrent.futures.ThreadPoolExecutor(max_workers=NO_THREADS) as executor:
        for wkn in tqdm(range(0, len(urls))):
            executor.submit(extract_product_info, urls[wkn][0], products_data)
    output_file_name = 'output_{}.csv'.format(
        datetime.today().strftime('%Y-%m-%d'))
    with open(output_file_name,'w') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(products_data[0].keys())
        for product in products_data:
            writer.writerow(product.values())
