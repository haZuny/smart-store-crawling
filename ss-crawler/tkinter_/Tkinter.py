### about tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox as msgbox

### about project files
from cralwer import NaverSmartStoreCralwer
from excel import Excel
import GLOBAL_VAL

### ect.
from datetime import datetime
import os
import sys
import traceback    # pring errer line

class Tkinter:

    ### URL Parameter Variable
    param_size = '80'
    param_st = 'TOTALSALE'
    paramStMap = {'인기도순':'POPULAR', '최신등록순':'RECENT', '낮은가격순':'LOW_DISP_PRICE', '높은가격순':'HIGH_DISP_PRICE',
                 '할인율순':'DISCOUNT_RATE', '누적판매순':'TOTALSALE', '리뷰많은순':'REVIEW', '평점높은순':'SATISFACTION'}
    urlParamsDefault = '?page=1&dt=LIST'
    urlParams = "?page=1&dt=LIST&size=80&st=TOTALSALE"

    def __init__(self, ):
        
        ### tkinter setting
        self.window = tk.Tk("SS-Crawler")
        self.window.title("SS-Crawler for MKShop")
        self.window.geometry("450x100")
        icon = tk.PhotoImage(file=GLOBAL_VAL.resource_path("./ss-crawler/resources/mk.png"))
        self.window.iconphoto(True, icon)

        ### URL Entry setting
        # Label
        self.urlLable = tk.Label(self.window, text='URL')
        self.urlLable.grid(row=0, column=0, columnspan=4, sticky='W')
        # Blank
        self.urlBlank = tk.Label(self.window, text='')
        self.urlBlank.grid(row=0, column=4, sticky='W')
        # Entry
        self.urlEntry = tk.Entry(self.window, width='50')
        self.urlEntry.grid(row=0, column=5, columnspan=7, sticky='W')

        ### Page cnt Entry setting
        # Label
        self.pageCntLable = tk.Label(self.window, text='최대 페이지')
        self.pageCntLable.grid(row=1, column=0, columnspan=4, sticky='W')
        # Blank
        self.pageCntBlank = tk.Label(self.window, text='')
        self.pageCntBlank.grid(row=1, column=4, sticky='W')
        # Entry
        self.pageCntEntry = tk.Entry(self.window)
        self.pageCntEntry.insert(0, '1')
        self.pageCntEntry.grid(row=1, column=5, columnspan=4, sticky='W')

        ### Max products cnt Setting
        # Label
        self.productCntLable = tk.Label(self.window, text='몇개씩 보기')
        self.productCntLable.grid(row=2, column=0, columnspan=4, sticky='W')
        # Blank
        self.productCntBlank = tk.Label(self.window, text='')
        self.productCntBlank.grid(row=2, column=4, sticky='W')
        # ComboBox
        self.productCntList = [20, 40, 60, 80]
        self.productCntCombobox = ttk.Combobox(self.window)
        self.productCntCombobox.config(values=self.productCntList, state='readonly')
        self.productCntCombobox.set('80')
        self.productCntCombobox.grid(row=2, column=5, columnspan=4, sticky='W')

        ### Align Setting
        # Label
        self.alignLable = tk.Label(self.window, text='정렬 기준')
        self.alignLable.grid(row=3, column=0, columnspan=4, sticky='W')
        # Blank
        self.alignBlank = tk.Label(self.window, text='')
        self.alignBlank.grid(row=3, column=4, sticky='W')
        # ComboBox
        self.alignList = ['인기도순', '최신등록순', '낮은가격순', '높은가격순',
                          '할인율순', '누적판매순', '리뷰많은순', '평점높은순']
        self.alignCombobox = ttk.Combobox(self.window)
        self.alignCombobox.config(values=self.alignList, state='readonly')
        self.alignCombobox.set('누적판매순')
        self.alignCombobox.grid(row=3, column=5, columnspan=4, sticky='W')

        # ### Button Setting
        # Button
        saveBtn = tk.Button(self.window, text="추출", overrelief='solid',
                            padx='30', pady='10', bg='light cyan')
        saveBtn.config(command=self.saveBtnEvent)
        saveBtn.grid(row=2, column=10, columnspan=4, rowspan=2)
        
        # Run
        self.window.mainloop()

    ### event method when saveButton is clicked
    def saveBtnEvent(self):
        
        # Select save path
        savePath = filedialog.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"),), title="파일 저장 경로 선택",
                                           initialfile=datetime.today().strftime("%Y_%m_%d_%H_%m_%s") + ".xlsx" )
        if savePath == "":
            return

        try:
            # Create Crawler
            url = self.getFullURL(self.getDefaultUrl(), self.urlParams)
            crawler = NaverSmartStoreCralwer.NaverSmartStoreCralwer(url)

            # Crawling page data
            crawledData = crawler.getProductsUntilLastReview(crawler.driver, int(self.pageCntEntry.get()))
            values = []
            for i in range(len(crawledData['names'])):
                row = [crawledData['names'][i], crawledData['prices'][i]]
                values.append(row)

            # Save as excel file
            excel = Excel.Excel(savePath)
            excel.createAndInsertData(row=2, column=2, rowGap=3, values=values)

            # notice and kill program
            msgbox.showinfo("Success", "파일이 성공적으로 저장되었습니다.")
        
        ### errer case
        except Exception as e:
            msgbox.showerror("Error", "도중에 문제가 발생했습니다.\n다시 시도해주세요")
            print(traceback.format_exc())


    ### About URL
    def getDefaultUrl(self):
        url = self.urlEntry.get()
        defaultUrl = url.split("?")[0]
        return defaultUrl
    
    def getFullURL(self, defaultUrl, parameter):
        return defaultUrl + parameter
    
    # change url parameter
    def setUrlParams(self, parameter, value):
        if parameter == 'size':
            self.param_size = value
        elif parameter == 'st':
            self.param_st = self.paramStMap[value]

        self.urlParams = self.urlParamsDefault + "&size=" + self.param_size + "&st="+self.param_st
