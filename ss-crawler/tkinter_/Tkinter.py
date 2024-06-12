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

class Tkinter:

    def __init__(self, shopList):

        ### Reset
        self.shopList = shopList
        
        ### tkinter setting
        self.window = tk.Tk("SS-Crawler")
        self.window.title("SS-Crawler for MKShop")
        icon = tk.PhotoImage(file=GLOBAL_VAL.resource_path("./ss-crawler/resources/mk.png"))
        self.window.iconphoto(True, icon)

        ### Component setting
        # Combo Box
        self.shopComboBox = shopComboBox = ttk.Combobox(self.window)
        shopComboBox.config(values=shopList, state="readonly")
        shopComboBox.set(shopList[0])
        shopComboBox.grid(row=0, column=0, columnspan=5, padx=20, pady=20)

        # Button
        saveBtn = tk.Button(self.window, text="추출")
        saveBtn.config(command=self.saveBtnEvent)
        saveBtn.grid(row=0, column=5, columnspan=2, padx=20, pady=20, ipadx=20)
        
        # Run
        self.window.mainloop()

    ### event method when saveButton is clicked
    def saveBtnEvent(self):
        
        # Select save path
        savePath = filedialog.asksaveasfilename(filetypes=(("Excel files", "*.xlsx"),), title="파일 저장 경로 선택",
                                           initialfile=datetime.today().strftime("%Y_%m_%d") + "_" + self.shopComboBox.get() + ".xlsx" )
        if savePath == "":
            return

        try:
            # Select Crawler
            if self.shopComboBox.get() == GLOBAL_VAL.HYUNSTORYMALL:
                crawler = NaverSmartStoreCralwer.NaverSmartStoreCralwer()

            # Crawling page data
            crawledData = crawler.getProductsUntilLastReview(crawler.driver)
            values = []
            for i in range(len(crawledData['names'])):
                row = [crawledData['names'][i], crawledData['prices'][i]]
                values.append(row)

            # Save as excel file
            excel = Excel.Excel(savePath)
            excel.createAndInsertData(row=2, column=2, rowGap=3, values=values)

            # notice and kill program
            msgbox.showinfo("Success", "파일이 성공적으로 저장되었습니다.")
            sys.exit()
        
        ### errer case
        except Exception as e:
            msgbox.showerror("Error", "도중에 문제가 발생했습니다.\n다시 시도해주세요")
            print(e)

        
    