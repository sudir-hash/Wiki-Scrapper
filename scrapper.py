import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



xpath="/html/body/div[3]/div[3]/div[5]/div[1]/table[1]"

# info_table_class="infobox vcard"
page_url='https://en.wikipedia.org/wiki/Canada'



def beauty_scarpe(page_url):
    page = requests.get(page_url).text
    soup = BeautifulSoup(page, 'html.parser')

#    info_table_class="info vbox"
    # table = soup.find('table', class_=info_table_class)
    table=soup.select("table[class*=info]") # with *= means: contains
    df = pd.read_html(str(table))
    df = pd.concat(df)
    return df

#beauty_scarpe()
def selenium_scrape( link, xpath):
	browser= webdriver.Chrome(ChromeDriverManager().install())
	browser.get(link)
	html = browser.find_element(By.XPATH, xpath)
	return pd.read_html(html.get_attribute('outerHTML'))


df=selenium_scrape(page_url,xpath)
print(df)


#using beautfiul soup
# df=beauty_scarpe(page_url,xpath)
# df.drop(index=0)
# print(df)



