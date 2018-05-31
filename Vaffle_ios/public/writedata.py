import unittest,xlrd
from xlutils.copy import copy

class Writedata(unittest.TestCase):
    def __init__(self):
        self.excel = xlrd.open_workbook('..//testdata/testdata.xls')
        self.newexcel=copy(self.excel)

    def Write_data(self,index,row,col,text):
        sheet=self.newexcel.get_sheet(index)
        sheet.write(row,col,text)
        self.newexcel.save('..//testdata/testdata.xls')




if __name__ == '__main__':
    unittest.main()
