
from splinter import Browser
from bs4 import BeautifulSoup as bs
import re
import time
import pandas as pd


browser = Browser('chrome', executable_path = 'chromedriver', headless=False)


# # Visit the NASA mars news site

url = 'https://mars.nasa.gov/news'
browser.visit(url)
browser.is_element_present_by_css('ul.item_list li.slide')


html = browser.html
news_soup = bs(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide' , wait_time = 1)

slide_elem.find('div', class_='content_title')

news_title = slide_elem.find('div',class_='content_title').get_text()
news_title


news_p = slide_elem.find('div',class_='article_teaser_body').get_text()
news_p


# # JPL Space Images Featured Image

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()

html = browser.html
img_soup = bs(html,'html.parser')

img_url_rel = img_soup.select_one('figure.lede a img').get('src')
img_url_rel

img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# # Mars Facts

df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


df.to_html()

browser.quit()



