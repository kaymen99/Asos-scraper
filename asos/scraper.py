from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os, re
from selenium.webdriver.chrome.options import Options 
import pandas as pd
from parsel import Selector





def scrape(search, gender, pages):
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36")
    opts.add_argument('--headless')
    opts.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=opts)
    driver.get(f'https://www.asos.com/search/?q={search}&refine=floor:{gender}')
    time.sleep(5)

    response = Selector(driver.page_source)
    max_pages = int(response.xpath('//*[@id="plp"]/div/div[3]/div/div[2]/progress/@max').getall()[0])//72
    print(f'The max number of pages is : {max_pages}')

    p = re.compile(r'£\d+.\d+')


    elements = []
    for i in range(1, pages+1):
        driver.get(f'https://www.asos.com/search/?page={i}&q={search}&refine=floor:{gender}')
        time.sleep(5)
        sel = Selector(driver.page_source)
        products_links = response.xpath('//article[@data-auto-id="productTile"]/a/@href').getall()
        products = response.xpath('//article[@data-auto-id="productTile"]/a/@aria-label').getall()
        for product, link in zip(products, products_links):
            name = product.split(';')[0]
            price = product.split(';')[1]
            try:
                current = p.findall(price)[1]
                original = p.findall(price)[0]
            except IndexError as e:
                current = original = p.findall(price)[0]

            elements.append([name, original, current, link])
        print(f'Scraped page {i}')


    data = pd.DataFrame(elements, columns=['name', 'original', 'current', 'link'])
    save_path = os.path.join(os.getcwd(), 'data.csv')
    data.to_csv(save_path)

    print('finished')
    driver.quit()


