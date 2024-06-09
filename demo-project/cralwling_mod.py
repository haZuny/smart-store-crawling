import time

### import bs4
import requests
from bs4 import BeautifulSoup

### import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

### seleniup page get
driver = webdriver.Chrome()
url = 'https://smartstore.naver.com/hyunstorymall/category/ALL?st=TOTALSALE&dt=LIST&page=1&size=20'
driver.get(url)

### next page
btn = driver.find_element(By.XPATH, '//*[@id="CategoryProducts"]/div[3]/a[3]')
ActionChains(driver).click(btn).perform()

time.sleep(1)

### bs4 parsing
soup = BeautifulSoup(driver.page_source, 'html.parser')


print()
print()
selected = soup.select("div#CategoryProducts>ul>li>div._1vVKEk_wsi>strong")
print(selected)

# print(driver)