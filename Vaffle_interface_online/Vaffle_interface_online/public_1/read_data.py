import os
import unittest

import time
import xlrd
#---------------------------编写读取excel数据函数，用于读取测试数据，测试用例调用excel数据做准备---------------------------------------------------
import json
from get_url import Url

class Read_ExcelData():
    # ------------------单例模式，第一次执行init，后面不再执行--------------------------
    __instance = None

    def __init__(self):
        self.get_instance ()
        pass

    def get_instance(self):
        if Read_ExcelData.__instance is None:
            # 获取EXcel路径
            self.path = Url ().test_path ()
            Read_ExcelData.__instance = xlrd.open_workbook ( self.path )
        return Read_ExcelData.__instance

    #---------------------读取str类型-------------------------------------------
    def read_excel_data(self,sheet_value,row_value,col_value):
        #选择工作页
        sheet = self.__instance.sheet_by_index(sheet_value)
        #读取行列数据
        daterow = sheet.row(row_value)[col_value].value
        #daterow = str(daterow)
        #返回读取结果
        return daterow



    #--------------------读取dict字典类型-（str改成dict类型）------------------------------------------
    def read_excel_data_dict(self,sheet_value,row_value,col_value):
        #选择工作页
        sheet = self.__instance.sheet_by_index(sheet_value)
        #读取行列数据
        daterow = sheet.row(row_value)[col_value].value
        #str改成dict类型
        daterow = json.loads(daterow)
        print(daterow)
        #返回读取结果
        return daterow


