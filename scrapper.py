import pandas as pd
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

''''
work on fixing the class name
'''

xpath="/html/body/div[3]/div[3]/div[5]/div[1]/table[1]"

info_table_class="infobox vcard"
page_url='https://en.wikipedia.org/wiki/Canadian_Tire'

def beauty_scarpe():
    page = requests.get(page_url).text
    soup = BeautifulSoup(page, 'html.parser')

#    info_table_class="info vbox"
    table = soup.find('table', class_=info_table_class)

    df = pd.read_html(str(table))
    df = pd.concat(df)
    df = df.drop(index=0)
    print(df)

# beauty_scarpe()
def selenium_scrape():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(page_url)
    table = driver.find_elements_by_xpath (xpath)
    table_contents=[]
    # table = driver.find_elements(by=By.CLASS_NAME, value=info_table_class)
    for el in table:
        print(el.text)
        table_contents.append(el.text)


selenium_scrape()



