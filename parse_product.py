from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

df = pd.read_excel("result_smartfony.xlsx")
print(df)

column = df["url"]
print(column)
print(column[0])
prices = list()
titles = list()
for element in column:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(element)
    title = driver.find_element(by=By.CLASS_NAME, value="q6o")
    try:
        price = driver.find_element(by=By.CLASS_NAME, value="n8z zn8")
        prices.append(price.text)
    except:
        price = driver.find_element(by=By.CLASS_NAME, value="nz9")
        prices.append(price.text)
    titles.append(title.text)



df = pd.DataFrame({"title":titles,
                   "price":prices})

df.to_excel("result_full")

