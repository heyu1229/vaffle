import os
import unittest

import time
import xlrd
#---------------------------编写读取excel数据函数，用于读取测试数据，测试用例调用excel数据做准备---------------------------------------------------
import json

from public.get_url import Url


class Read_ExcelData():



    #---------------------读取str类型-------------------------------------------
    def read_excel_data(self,sheet_value,row_value,col_value):
        #获取EXcel路径
        path = Url().test_path()

        '''获取当前文件夹的父目录绝对路径E:\python35\HG\heaven_interface_vaffle3.0'''
        # 打开excel
        filename = xlrd.open_workbook(path)
        #选择工作页
        sheet = filename.sheet_by_index(sheet_value)
        #读取行列数据
        daterow = sheet.row(row_value)[col_value].value

        #daterow = str(daterow)
        #返回读取结果
        return daterow

    #--------------------读取dict字典类型-（str改成dict类型）------------------------------------------
    def read_excel_data_dict(self,sheet_value,row_value,col_value):
        #获取EXcel路径
        path = Url().test_path()

        # 打开excel
        filename = xlrd.open_workbook(path)


        #选择工作页
        sheet = filename.sheet_by_index(sheet_value)
        #读取行列数据
        daterow = sheet.row(row_value)[col_value].value
        #str改成dict类型
        daterow = json.loads(daterow)
        #返回读取结果
        return daterow


