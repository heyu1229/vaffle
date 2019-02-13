# -*- coding:UTF-8 -*-
import unittest,threading

import xlrd
#---------------------------编写excel数据写入函数，可以把测试结果写入excel表格中---------------------------------------------------

from get_url import Url
from xlutils.copy import copy #http://pypi.python.org/pypi/xlutils


class Write_ExcelData():
    #------------------单例模式，第一次执行init，后面不再执行--------------------------
    __instance = None

    def __init__ (self):
        self.get_instance()
        pass

    def get_instance ( self):
        if Write_ExcelData.__instance is None:
            # 获取EXcel路径
            self.path = Url ().test_path ()
            open =  xlrd.open_workbook(self.path)
            Write_ExcelData.__instance = copy ( open )
        return Write_ExcelData.__instance
    def write_excel_data(self,sheet_value,row_value,col_value,datetext,path):
        #old_excel = xlrd.open_workbook ( path )
        # 获得第一个sheet的对象
        sheet = self.__instance.get_sheet (sheet_value)
        sheet.write ( row_value, col_value,datetext )
        self.__instance.save ( path )


if __name__ == '__main__':
    unittest.main()

    '''
    #---------------------------------
    不使用单例，可用如下方法，调用写法如下：这样init也只调用第一次
        obj =Write_ExcelData()
        obj.write_excel_data( 0, 93, 6, result['code'],self.path,self.filename)
        obj.write_excel_data ( 0, 93, 7, result['msg'], self.path, self.filename )
        obj.write_excel_data ( 0, 93, 8, str ( result ), self.path, self.filename )
        obj.write_excel_data ( 0, 93, 9, end - start, self.path, self.filename )


    def __init__(self):
        #获取EXcel路径
        self.path = Url().test_path()
        # 打开excel
        self.filename =  xlrd.open_workbook(self.path)
        # 将操作文件对象拷贝，变成可写的workbook对象
        self.new_excel = copy ( self.filename )
        print(self.new_excel)
    '''

    '''获取当前文件夹的父目录绝对路径E:\python35\HG\heaven_interface_vaffle3.0'''


