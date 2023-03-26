import time

import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
titles = list()
prices = list()
urls = list()


driver.get(url="https://www.ozon.ru/category/smartfony-15502/")
driver.implicitly_wait(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
elements = soup.find_all("div",{"x7k kx8"})
print(len(elements))
for element in elements:
    title = element.find_next("span",{"class":"he0 eh1 he1 he3 tsBodyL uk3"}).get_text()
    print(title)
    titles.append(title)
    price = element.find_next("span",{"class":"_32-a2"}).get_text()
    print(price)
    prices.append(price)
    url = "https://www.ozon.ru" + element.find_next("a",{"class":"tile-hover-target uk3"})["href"]
    urls.append(url)
    print(url)


links = list()
next_page = soup.find_all("a",{"class":"a4ar"})
for page in next_page:
    try:
        print("https://www.ozon.ru" + page["href"])
        links.append("https://www.ozon.ru" + page["href"])

    except:
        pass


driver.quit()

df = pd.DataFrame({"title":titles,"price":prices,"url":urls})

df.to_excel("result_smartfony.xlsx")