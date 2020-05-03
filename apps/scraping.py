
from splinter import Browser
from bs4 import BeautifulSoup as bs
import re
import datetime as dt
import pandas as pd

# Set the executable path and initialize the chrome browser in splinter.
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path)

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }
    browser.quit()

    return data


def mars_news(browser):
    
    # Vist the mars nasa news site.
    url = ('https://mars.nasa.gov/news/')
    browser.visit(url)
    # Optional delay for loading page.
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time = 1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = bs(html, "html.parser")

    # Add try/except for error handling.
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')

        # Use the parent element to find the first `a` tag and save it as `news_title`.
        news_title = slide_elem.find("div", class_='content_title').get_text()

        # Use the parent element to find the summary paragraph.
        news_p = slide_elem.find('div', class_ = 'article_teaser_body').get_text()

    except AttributeError:
        return (None, None)

    return (news_title, news_p)

def featured_image(browser):
    
    # JPL Space Images Featured Image
    url = ('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')
    browser.visit(url)

    # Find and click the full imagine button.
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click it.
    browser.is_element_present_by_text('more info', wait_time = 1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup.
    html = browser.html
    img_soup = bs(html, 'html.parser')

    # Add try/except to handel errors.
    try:
        # Find the relative image url.
        img_url_rel = img_soup.select_one('figure.lede a img').get('src')

        # Use the base url to create an absolute url.
        img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    except AttributeError:
        return(None)

    return (img_url)

# # Challenge

# ## High-resolution images for each of Mars's hemispheres

# Visit URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Parse the resulting html with soup
html = browser.html
soup = bs(html, 'html.parser')

base_url= 'https://astrogeology.usgs.gov'

#Parse out the soup and find all of the links
description_elem = soup.find_all('div', class_='description')


#Add base url to links. 
links = [base_url + item.a['href'] for item in description_elem]

links


# Create dictionary. 
title_url_list = []

# Parse out each link. 
for link in links:
    browser.visit(link)
    
    # Parse the resulting html with soup
    html = browser.html
    soup = bs(html, 'html.parser')
    
    # Get title with get_text function. 
    title = soup.select_one('h2.title').get_text()
    
    # Get img_url 
    img_elem = soup.select('div.downloads li')
    
    img_url, = [item.a['href'] for item in img_elem if item.a.get_text() == 'Sample']
    
    
    # Create a dictionary containing title and image. 
    title_url_dict = {'title': title, 'img_url': img_url}
    
    # Append to list
    title_url_list.append(title_url_dict)
    
print(title_url_list)


# # Mars Facts

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

