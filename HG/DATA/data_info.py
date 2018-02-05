import unittest,os
from re import A

import xlrd
from DATA.FileBaseControl import XlsEngine


class heaven_info(unittest.TestCase):
    def userinfo_01(self):
        data = xlrd.open_workbook('E:/python35/HG/heaven_formal/DATA/data_info.xlsx')      # 打开excel
        # data = xlrd.open_workbook ( os.getcwd()[:-9]+'/DATA/data_info.xlsx' )
        sheet = data.sheets()[0]                                                             # 读取第几张sheet,从0开始
        row = sheet.row_values(1)                                                            # 读取第二行数据,行从0开始
        An = str(row[0])                                                                     # 列从0开始( 转成int型)
        Bn = str(row[1])
        Cn = str(row[2])
        Dn = int(row[3])
        En = str(row[4])
        Fn = str(row[5])
        Gn = str(row[6])
        Hn = int(row[7])
        return An,Bn,Cn,Dn,En,Fn,Gn,Hn

    # def userinfo_01(self):
    #     # 打开excel
    #     xls_path =os.getcwd()[:-9]+"/DATA/data_info.xlsx"
    #     workbook = XlsEngine().open_file(xls_path)
    #     # 读取第几张sheet,从0开始
    #     table, table.nrows, table.ncols = XlsEngine().get_sheet_data(xls_path,workbook,0)
    #     # 读取第二行数据,行从0开始
    #     rows = XlsEngine().get_row_value(table,2)
    #     arr = []
    #     for row in rows:
    #         arr.append(row)
    #     An = str ( arr[0] )  # 列从0开始( 转成int型)
    #     Bn = str ( arr[1] )
    #     Cn = str ( arr[2] )
    #     Dn = int ( arr[3] )
    #     En = str ( arr[4] )
    #     Fn = str ( arr[5] )
    #     Gn = str ( arr[6] )
    #     Hn = int ( arr[7] )
    #     return An, Bn, Cn, Dn, En, Fn, Gn, Hn
    '''普通标模板'''


    if __name__ == '__main__':
        unittest.main ()
