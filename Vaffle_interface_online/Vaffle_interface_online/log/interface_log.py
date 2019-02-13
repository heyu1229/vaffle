# -*- coding=utf-8 -*-
import global_list
import logging
#---------------获取日志----------------------
import logging.handlers

class interface_log():
    #日志级别log_level 0:notset(所有)，10:debug ，20:info ,30:warning ,40:error ,50:critical
    def init_log(log_level):
        #创建一个logging的实例logger
        logger = logging.getLogger()
        #设定全局日志级别
        logger.setLevel(log_level)
        # logger.setLevel(logging.DEBUG)
        #创建一个handler，用于写入日志文件
        fh = logging.FileHandler(global_list.path+"/test_date/vaffle2.0_interface.log")
        #再创建一个屏幕的handler，用于输出到控制台
        ch = logging.StreamHandler()
        # 定义handler的输出格式formatter
        formatter = logging.Formatter ( '%(asctime)s - %(name)s - %(levelname)s - %(message)s' )
        fh.setFormatter ( formatter )
        ch.setFormatter ( formatter )

        # 给logger添加handler
        # logger.addFilter(filter)
        logger.addHandler ( fh )
        logger.addHandler ( ch )
        return logger




