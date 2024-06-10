### import about python
from abc import abstractmethod
import time

### import bs4
import requests
from bs4 import BeautifulSoup

### import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

### Interface class
class Cralwer():
    # pageUrl
    pageUrl = ''
    # current page cnt
    currentPageCnt = 1
    # Xpath form about next Buttons
    nextBtnsXpath_form = ''
    # beautifulSoup find style about a name of product
    productNameStyle = ''
    # beautifulSoup find style about a price of product
    productPriceStyle = ''
    # beautifulSoup find style about the product list of current page.
    productListStyle = ''
    # html element form about review can be used to define the product has review
    reviewElement = ''

    # get BeautifulSoup source about page.
    def updatePageSource(self, driver):
        self.pageSource = BeautifulSoup(driver.page_source, 'html.parser')

    # click next page button, False: lastPage
    def clickNextPage(self, driver, nextBtnsXpath_form):
        btns = driver.find_elements(By.XPATH, nextBtnsXpath_form)
        click_flag = False
        for btn in btns:
            if click_flag:
                try:
                    btn.click()
                except:
                    pass
                self.currentPageCnt+=1
                return True
            if str(self.currentPageCnt) == btn.text:
                click_flag = True
        return False
    
    # click next page button and update page data source. False: lastPage
    def updateNextPageSource(self, driver, nextBtnsXpath_form):
        isLast = self.clickNextPage(driver, nextBtnsXpath_form)
        time.sleep(1)
        self.updatePageSource(driver)
        return isLast

    # get a list of puduct names
    def getPruductNames(self, pageSource, productNameStyle):
        nameTags = pageSource.select(productNameStyle)
        list = []
        for nameTag in nameTags:
            list.append(nameTag.string)
        return list

    # get a list of puduct prices
    def getPruductPrices(self, pageSource, productPriceStyle):
        priceTags = pageSource.select(productPriceStyle)
        list = []
        for priceTag in priceTags:
            list.append(priceTag.string)
        return list

    # get a list if a puduct has review
    def getReviewBoolean(self, pageSource, productListStyle, reviewElement):
        list = []
        products = pageSource.select(productListStyle)
        for product in products:
            if reviewElement in str(product):
                list.append(True)
            else:
                list.append(False)
        return list


    def getProductsUntilLastReview(self, driver):
        nameList = []
        priceList = []
        reviewList = []

        # 전체 이름, 가격, 리뷰 여부 얻어오기
        nameList += self.getPruductNames(self.pageSource, self.productNameStyle)
        priceList += self.getPruductPrices(self.pageSource, self.productPriceStyle)
        reviewList += self.getReviewBoolean(self.pageSource, self.productListStyle, self.reviewElement)

        # 최대 1페이지만 탐색하므로 주석 처리
        # while(self.updateNextPageSource(driver, self.nextBtnsXpath_form)):
        #     nameList += self.getPruductNames(self.pageSource, self.productNameStyle)
        #     priceList += self.getPruductPrices(self.pageSource, self.productPriceStyle)
        #     reviewList += self.getReviewBoolean(self.pageSource, self.productListStyle, self.reviewElement)
        # nameList += self.getPruductNames(self.pageSource, self.productNameStyle)
        # priceList += self.getPruductPrices(self.pageSource, self.productPriceStyle)
        # reviewList += self.getReviewBoolean(self.pageSource, self.productListStyle, self.reviewElement)
        
        # 마지막 인덱스 탐색
        lastIdx = len(reviewList)-1
        while (lastIdx >= 0):
            if (reviewList[lastIdx]):
                break
            lastIdx -= 1
        
        # 각 요소 반환
        dict = {}
        dict['names'] = nameList[:lastIdx+1]
        dict['prices'] = priceList[:lastIdx+1]

        print(len(dict['names']))
        print(dict)
        return dict







class HyunstorymallCralwer(Cralwer):
    

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

    # def test(self):
    #     self.updateNextPageSource(self.driver, self.nextBtnsXpath_form)
    #     # self.updateNextPageSource(self.driver, self.nextBtnsXpath_form)
    #     # self.updateNextPageSource(self.driver, self.nextBtnsXpath_form)
    #     print(self.getPruductNames(self.pageSource, self.productNameStyle))

a = HyunstorymallCralwer()
a.getProductsUntilLastReview(a.driver)