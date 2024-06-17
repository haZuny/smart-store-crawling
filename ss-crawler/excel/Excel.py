from openpyxl import Workbook
import openpyxl
import openpyxl.styles
import openpyxl.utils

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
    def insertData(self, row, column, rowGap, values):
        for i in range(len(values)):
            for j in range(len(values[i])):
                self.ws.cell(row+ rowGap*i, column+j, values[i][j])
    
    
    ### save
    def save(self):
        self.wb.save(self.fileName)


    ### change excel sheet gap
    def autoFitColumn(self, multySize):
        for column_cells in self.ws.columns:
            # get:: Max data size * 1.1
            length = max(len(str(cell.value))*multySize for cell in column_cells)
            self.ws.column_dimensions[column_cells[0].column_letter].width = length

    ### set column align
    def alignColumn(self, align):
        for column_cells in self.ws.columns:
            ## align center
            for cell in self.ws[column_cells[0].column_letter]:
                cell.alignment = openpyxl.styles.Alignment(horizontal=align)

    
    ### create excel file and insert data
    def createAndInsertData(self, row, column, rowGap, values):
        self.insertData(row, column, rowGap, values)
        self.autoFitColumn(1.5)
        self.alignColumn('center')
        self.save()