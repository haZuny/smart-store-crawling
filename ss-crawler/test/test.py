import sys
sys.path.append("C:/Users/gkwns/Hajun/smart-store-crawling/ss-crawler")
from cralwer import NaverSmartStoreCralwer
from excel import Excel

from PIL import Image as pi


e = Excel.Excel('aa.xmlx')

print(e.insertImageFromURL(0,0,'https://shop-phinf.pstatic.net/20231021_38/1697898352804uF7yo_JPEG/44863607582911739_975259582.jpeg?type=f140', 20))