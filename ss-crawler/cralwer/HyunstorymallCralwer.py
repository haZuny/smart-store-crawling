### Interface
from . import Cralwer

### Selenium webdriver
from selenium import webdriver

class HyunstorymallCralwer(Cralwer.Cralwer):
    def __init__(self):
        # pageUrl
        self.pageUrl = 'https://smartstore.naver.com/hyunstorymall/category/ALL?st=TOTALSALE&dt=LIST&page=1&size=80'
        # Xpath form about next Buttons
        self.nextBtnsXpath_form = '//*[@id="CategoryProducts"]/div[3]/*'
        # beautifulSoup find style about a name of product
        self.productNameStyle = 'div#CategoryProducts>ul>li._3S7Ho5J2Ql>div._1vVKEk_wsi>strong._1Zvjahn0GA'
        # beautifulSoup find style about a price of product
        self.productPriceStyle = 'div#CategoryProducts>ul>li._3S7Ho5J2Ql>div._1vVKEk_wsi>div>strong._22XUYkkUGJ>span._3_9J443eIx'
        # beautifulSoup find style about the product list of current page.
        self.productListStyle = 'div#CategoryProducts>ul>li._3S7Ho5J2Ql'
        # html element form about review can be used to define the product has review
        self.reviewElement = '<span class="_2AHonHjEgF">리뷰</span>'

        # seleniup driver
        self.driver = webdriver.Chrome()
        self.driver.get(self.pageUrl)

        # beautifulSoup page source
        self.updatePageSource(self.driver)