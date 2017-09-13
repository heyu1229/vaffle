import os
import unittest

import xlrd
#---------------------------编写excel数据写入函数，可以把测试结果写入excel表格中---------------------------------------------------

from public.get_url import Url
from xlutils.copy import copy #http://pypi.python.org/pypi/xlutils


class Write_ExcelData():


    '''获取当前文件夹的父目录绝对路径E:\python35\HG\heaven_interface_vaffle3.0'''
    def write_excel_data(self,sheet_value,row_value,col_value,datetext):

        #获取EXcel路径
        path = Url().test_path()

        '''获取当前文件夹的父目录绝对路径E:\python35\HG\heaven_interface_vaffle3.0'''
        '''
        # 打开excel
        filename = xlrd.open_workbook(path)
        #利用原工作簿创建新的工作薄
        newdate = shutil.copyfile ( path,'E:/python35/HG/heaven_interface_vaffle3.0/test_date/interface2.xls')
        # 打开excel
        filename2 = xlrd.open_workbook(newdate)
        #通过sheet_by_index()获取的sheet没有write()方法
        #sheet = filename2.sheet_by_index (sheet_value)

        sheet = newdate.get_sheet (0)
        print(sheet)
        #写入行列中数据
        sheet.write(3,5,"aaa")
        #保存文档
        newdate.save(path)
        '''
        # 打开想要更改的excel文件
        old_excel = xlrd.open_workbook ( path)
        # 将操作文件对象拷贝，变成可写的workbook对象
        new_excel = copy ( old_excel )
        # 获得第一个sheet的对象
        sheet = new_excel.get_sheet (sheet_value)
        sheet.write ( row_value, col_value,datetext )
        #os.remove ( path )
        new_excel.save(path)



if __name__ == '__main__':
    unittest.main()
