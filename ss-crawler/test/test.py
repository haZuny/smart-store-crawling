import sys
sys.path.append("C:/Users/gkwns/Hajun/smart-store-crawling/ss-crawler")

from cralwer import NaverSmartStoreCralwer

c = NaverSmartStoreCralwer.NaverSmartStoreCralwer('https://smartstore.naver.com/dalmongstore/category/ALL?st=TOTALSALE&dt=LIST&page=1&size=40')

res = c.getProductsUntilLastReview(c.driver, 1)
print(res)