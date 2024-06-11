from cralwer import HyunstorymallCralwer
from excel import Excel

if __name__ == '__main__':
    a = HyunstorymallCralwer.HyunstorymallCralwer()
    data = a.getProductsUntilLastReview(a.driver)
    dataSize = len(data['names'])

    values = []
    for i in range(dataSize):
        row = [data['names'][i], data['prices'][i]]
        values.append(row)


    e = Excel.Excel("C:/Users/gkwns/Hajun/smart-store-crawling/test.xlsx")
    e.createAndInsertData(2, 2, 3, values)
    print('end')

