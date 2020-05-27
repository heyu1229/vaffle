import unittest
import xlrd,json


class Readdata(unittest.TestCase):

    def Read_data(self,index,row_value,col_value):
        excel=xlrd.open_workbook("..//testdata/testdata.xls")
        sheet=excel.sheet_by_index(index)
        data=sheet.row(row_value)[col_value].value
        # data=json.loads(data)
        return data
    # def Read_data(self):
    #     excel=xlrd.open_workbook("..//testdata/testdata.xls")
    #     sheet=excel.sheet_by_index(0)
    #     data=sheet.row(1)[0].value
    #     print(data)

if __name__ == '__main__':
    # Readdata.Read_data()
    unittest.main()
