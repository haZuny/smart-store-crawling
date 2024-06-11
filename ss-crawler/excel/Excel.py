from openpyxl import Workbook

class Excel:

    def __init__(self, fileName):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.fileName = fileName
    

    ### insert data with row
    def insertRow(self, row, column, values):
        for i in range(len(values)):
            self.ws.cell(row+i, column, values[i])

    
    ### insert full data
    def insertData(self, row, column, values):
        for i in range(len(values)):
            for j in range(len(values[i])):
                self.ws.cell(row+i, column+j, values[i][j])
    
    
    ### save
    def save(self):
        self.wb.save(self.fileName)