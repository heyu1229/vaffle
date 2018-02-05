import unittest,os
from re import A

import xlrd
from DATA.FileBaseControl import XlsEngine


class heaven_info(unittest.TestCase):
    '''普通标模板'''
    def userinfo_01(self):

        data = xlrd.open_workbook(os.getcwd()+'/DATA/data_info.xlsx')      # 打开excel
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
        In = str(row[8])
        Jn = int(row[9])
        return An,Bn,Cn,Dn,En,Fn,Gn,Hn,In,Jn

    # def userinfo_02(self):
    #     # 打开excel
    #     xls_path ="E:/python35/HG/heaven_formal/DATA/data_info.xlsx"
    #     workbook = XlsEngine().open_file(xls_path)
    #     # 读取第几张sheet,从0开始
    #     table, table.nrows, table.ncols = XlsEngine().get_sheet_data(xls_path,workbook,0)
    #     # 读取第二行数据,行从0开始
    #     rows = XlsEngine().get_row_value(table,2)
    #     for row in rows:
    #         An =row
    #         print(An)

            # cell_value = XlsEngine ().get_cell_value ( table, 2, len(rows) )
            # print(cell_value)


        # An = str ( row[0] )  # 列从0开始( 转成int型)
        # Bn = str ( row[1] )
        # Cn = str ( row[2] )
        # Dn = int ( row[3] )
        # En = str ( row[4] )
        # Fn = str ( row[5] )
        # Gn = str ( row[6] )
        # Hn = int ( row[7] )
        # return An, Bn, Cn, Dn, En, Fn, Gn, Hn
        # print(An,Bn,Cn,Dn,En,Fn,Gn,Hn)

        # return An, Bn, Cn, Dn, En, Fn, Gn, Hn

    if __name__ == '__main__':
        unittest.main ()
