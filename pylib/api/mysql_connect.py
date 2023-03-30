#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2022/6/13 9:55
import datetime
import math

import pymysql
from pylib.api.database_info import database_info



    # def __enter__(self):
    #     #print(database_info)
    #     self.conn = pymysql.connect(**database_info)
    #     self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    #     return self
# database_info = dict(host="localhost",
#                      user="root",
#                      password="123456",
#                      port=3306,
#                      database="woniuboss4.0",
#                      charset="utf8")
def cud_table(sql):
    '''
    crud增删改查
    :return:
    '''
    conn = pymysql.connect(**database_info)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    # 增加：create
    # 查询: retrieve
    # 更新：update
    # 删除：delete
    curs.execute(sql)
    conn.commit()
    curs.close()
    conn.close()

def retrieve_table(sql):
    '''
    查询方法
    :param sql: SQL语句
    :return: 查询结果
    '''
    conn = pymysql.connect(**database_info)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute(sql)
    select_relust = curs.fetchall()    # 列表嵌套字典
    for i in select_relust: # i就是每一个字典
        for j in i.keys():  # j每一个字典的key
            if type(i[j]) == datetime.date:
                i[j] = i[j].strftime("%Y-%m-%d")
    curs.close()
    conn.close()

    return select_relust

def delete(keyword,args):
    num = len(args)
    print(num)
    if keyword =="employee_name":
        for i in args:
           result = retrieve_table(f"select employee_id  from employee where employee_name='{i}'")[0].get("employee_id")
           print(result)
           print(i)
           cud_table(f"delete from employee WHERE employee_name='{i}'")
           cud_table(f"delete from system_user where employee_id={result}")
    elif keyword=="class_no":
        for i in args:
           sql = f"delete from class WHERE class_no='{i}'"
           cud_table(sql)





# if __name__ == '__main__':
    #  with ApiMysql() as D:
    #     sql = "SELECT * FROM employee ORDER BY employee_id DESC LIMIT 1;"
    # #     print(retrieve_table(sql))
    # delete('高级教师','高级教师')
    # delete("employee_name",["teacher02"])


    # print(result)
