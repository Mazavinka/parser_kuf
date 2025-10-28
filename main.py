import time
from bs4 import BeautifulSoup
import requests
import db
import tg
from headers import my_headers
import os
from dotenv import load_dotenv
import hashlib

load_dotenv()


def get_all_pages_link(start_page_link):
    all_pages_link = [start_page_link]
    page_now = start_page_link

    while page_now != '':
        response = requests.get(page_now, headers=my_headers, timeout=15)
        bs = BeautifulSoup(response.text, 'lxml')
        try:
            next_page = os.getenv('BASE_URL') + bs.select_one('a[data-testid="realty-pagination-next-link"]')['href']
            all_pages_link.append(next_page)
            page_now = next_page
        except (TypeError, KeyError):
            page_now = ''
        time.sleep(3)
    return all_pages_link


def get_all_posts_from_page(page_link):
    response = requests.get(page_link, headers=my_headers, timeout=15)
    bs = BeautifulSoup(response.text, 'lxml')
    all_posts = bs.select('section')

    data = []

    for post in all_posts:

        price_byn = set_clean_byn_price(safe_text_from_post(post, 'span[class*="styles_price__byr"]'))
        price_usd = set_clean_usd_price(safe_text_from_post(post, '[class*="styles_price__usd"]'))
        parameters = safe_text_from_post(post, '[class*="styles_parameters"]')
        address = safe_text_from_post(post, 'span[class*="styles_address"]')
        short_description = safe_text_from_post(post, '[class*="styles_body"]')
        post_url = safe_url_from_post(post, 'a[data-testid*="kufar-realty-card"]')
        post_id = get_id_from_url(safe_url_from_post(post, 'a[data-testid*="kufar-realty-card"]'))
        hash_id = set_hash_id(address, post_id)

        item = {
            'price_byn': price_byn,
            'price_usd': price_usd,
            'parameters': parameters,
            'address': address,
            'short_description': short_description,
            'post_url': post_url,
            'post_id': post_id,
            'hash_id': hash_id,
        }

        is_added = db.add_new_item(post_id, price_byn, price_usd, parameters, address, short_description, post_url, hash_id)
        if is_added:
            data.append(item)
            tg.send_message(price_byn, price_usd, parameters, address, short_description, post_url)
            print('...New item in db...')

    return data


"""def set_my_personal_id(address, parameters):
    if address and parameters:
        return address + parameters
    else:
        print(address, parameters)
        return 'Empty'"""


def set_hash_id(address, post_id):
    if address and post_id:
        return hashlib.sha256(str(post_id + address).encode()).hexdigest()
    else:
        print(post_id, address)
        return 'Empty'


def set_clean_byn_price(price):
    if price:
        price = price.replace(' ', '')
        clean_price = price.split('р')[0]
        return clean_price
    else:
        return None


def set_clean_usd_price(price):
    if price:
        price = price.replace(' ', '')
        clean_price = price.split('$')[0]
        return clean_price
    else:
        return None


def safe_text_from_post(tag, selector):
    item = tag.select_one(selector)
    if item:
        return item.getText(strip=True)
    else:
        return None


def safe_url_from_post(tag, selector):
    url = tag.select_one(selector)
    if url:
        return url['href']
    else:
        return None


def get_id_from_url(url):
    if url:
        url_id = (url.split('?')[0]).split('/')[-1]
        return url_id
    else:
        return None


def run(url=os.getenv('STARTING_URL')):
    all_links = get_all_pages_link(url)
    data = [url]
    for link in all_links:
        data.append(get_all_posts_from_page(link))
        time.sleep(5)


if __name__ == '__main__':
    print('-----PARSER_WAS_STARTED-----')
    while True:
        try:
            run()
            time.sleep(20 * 60)
        except KeyboardInterrupt:
            print('-----PARSER_WAS_CLOSED-----')
