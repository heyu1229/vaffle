# -*- coding:UTF-8 -*-
from datetime import date

import xlrd
from log.UI_log import UI_log

class XlsEngine():

    def __init__(self):
        # self.xls_path = __filepath
        self.xlrd_object = None
        self.isOpenfailed = True
        self.LOG = UI_log.init_log(0)
    #-------------打开EXCEL------------------------
    def open_file(self,xls_path):
        try:
            self.xlrd_object = xlrd.open_workbook(xls_path)#, formatting_info=True)
            self.isOpenfailed = False
            self.LOG.debug('open "%s" file Succeed' % xls_path)
            return self.xlrd_object
        except Exception as e:
            self.xlrd_object = None
            self.LOG.error('open "%s" file Failed: %s \n' % (xls_path, e))
            raise (Exception('open "%s" file Failed \n' % xls_path, e))
        # finally:
        #     self.LOG.debug('File is Close!!!')
        #     return self.isOpenfailed#, self.xlrd_object

    # -------------获取sheet表 几行几列------------------------
    def get_sheet_data(self, xls_path,workbook,sheetName):
        if self.xlrd_object == None:
             self.open_file(xls_path)
        if self.isOpenfailed == False:
           try:
               table =workbook.sheets()[sheetName]
               # table = self.xlrd_object.sheet_by_name(sheetName)
               self.LOG.debug('get Sheet %s: Rownums=%d, Colnums=%d' % (sheetName, table.nrows, table.ncols))
               return table, table.nrows, table.ncols
           except Exception as e:
               self.LOG.error('get %s sheet content fail: %s' % (sheetName, e))
               raise (Exception('get %s sheet content fail' % sheetName, e))
        else:
            self.LOG.debug('File %s not open, not Executable!' % xls_path)

    # -------------获取某sheet的行------------------------
    def get_row_value(self, table, row_id):
        try:
            row_num = int(row_id) - 1
            rows_value = table.row_values(row_num)
            self.LOG.debug('table in %s row content: %s' % (row_id, str(rows_value).replace("u\'","\'")))
            return rows_value
        except Exception as e:
            self.LOG.error('get table in %s row content fail: %s' % (table, e))
            raise (Exception('get table in %s row content fail' % table, e))

    # -------------获取某sheet的列------------------------
    def get_col_value(self, table, col_id):
        try:
            col_num = int(col_id) - 1
            cols_value = table.col_values(col_num)
            self.LOG.debug('table in %s col content:%s' % (col_id, cols_value))
            return cols_value
        except Exception as e:
            self.LOG.error('get table in %s col content fail: %s' % (table, e))
            raise (Exception('get table in %s col content fail' % table, e))

    # -------------获取某sheet的某个单元格的值------------------------
    def get_cell_value(self, table, cell_row, cell_col):
        try:
            row_num = int(cell_row) - 1
            col_num = int(cell_col) - 1
            value_type = self.get_cell_value_type(table, row_num, col_num)
            if value_type == 'date':
                date_value = xlrd.xldate_as_tuple(table.cell_value(row_num, col_num), self.xlrd_object.datemode)
                value = date(*date_value[:3]).strftime('%Y/%m/%d')
            else:
                value = table.cell(row_num, col_num).value
                #if type(value) != float: value = value.encode('gbk')
                self.LOG.debug('table(%s, %s)value:%s' % (cell_row, cell_col, value))
            return value
        except Exception as e:
            self.LOG.error('get cell content fail: %s' % e)
            raise (Exception('get cell content fail', e))

    # -------------获取某sheet的某个单元格的类型------------------------
    def get_cell_value_type(self, table, cell_row, cell_col):
        try:
            row_num = int(cell_row) - 1
            col_num = int(cell_col) - 1
            cell_data_type = table.cell(row_num, col_num).ctype
            type_dict = {0: 'empty', 1: 'string', 2: 'number', 3: 'date', 4: 'boolean', 5: 'error'}
            self.LOG.debug('cell value type: %s' % type_dict[cell_data_type])
            return type_dict[cell_data_type]
        except Exception as e:
            self.LOG.error('get cell value type fail: %s' % e)
            raise (Exception('get cell value type fail', e))