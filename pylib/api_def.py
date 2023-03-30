#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2023/3/27 15:45
import json,pymysql,datetime
import requests
import random
from pylib.database_info import *
from pylib.url_info import *
s = requests.session()
def php():
    re = s.get(url=url+"/labPhpVersion/getAllPhp")
    print(re.text)
    sj_jg = json.loads(re.text)
    print(sj_jg)
    return sj_jg.get("code")

def login_miss():
    param = {
  "password": "123123",
  "phone": "13888998899"
}
    j_data = json.dumps(param)

    header = {"Content-Type": "application/json"}
    re = s.post(url=url+"/labManager/login",data=j_data,headers=header)
    # print(re.text)
    # print(re.url)
    # print(re.headers)
    # print(type(j_data))
    print(re.text)
    sj_result = json.loads(re.text)
    print(type(sj_result.get("msg")))
    return sj_result.get("msg")


def TOMCat():
    r= s.get(url=url+"/labTomcatVersion/getAllTomcat")
    print(r.text)
    sj_jg = json.loads(r.text)
    print(sj_jg)
    return sj_jg.get("code")

def add_user():
    sj = random.randint(1, 9999999)
    global miss
    miss = f"1599{sj}"
    print(miss)
    data = {
        "phone":miss
    }
    r = s.get(url=url+"/labUser/addUser",params=data)
    # print(r.text)
    sj_jg = json.loads(r.text)
    # print(sj_jg.get("msg"))
    # print(sj)

    return sj_jg.get("msg"),miss

def add_user_1(phone):
    data = {
        "phone":phone
    }
    r = s.get(url=url+"/labUser/addUser",params=data)
    # print(r.text)
    sj_jg = json.loads(r.text)
    # print(sj_jg.get("msg"))
    # print(sj)
    print(sj_jg.get("msg"))
    return sj_jg.get("msg")

add_user_1("150945684723")
def retrieve_table(sql):
    '''
    查询方法
    :param sql: SQL语句
    :return: 查询结果
    '''
    conn = pymysql.connect(**database_info)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute(sql)
    select_relust = curs.fetchall()  # 列表嵌套字典
    for i in select_relust:  # i就是每一个字典
        for j in i.keys():  # j每一个字典的key
            if type(i[j]) == datetime.date:
                i[j] = i[j].strftime("%Y-%m-%d")
    curs.close()
    conn.close()
    return select_relust[0].get("phone")


def cud_table(sql):
    '''
    crud增删改查
    :return:
    '''
    conn = pymysql.connect(**database_info)
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute(sql)
    curs.close()
    conn.close()


# def retrieve_table(sql):
#     '''
#     查询方法
#     :param sql: SQL语句
#     :return: 查询结果
#     '''
#     conn = pymysql.connect(**database_info)
#     curs = conn.cursor(pymysql.cursors.DictCursor)
#     curs.execute(sql)
#     select_relust = curs.fetchall()    # 列表嵌套字典
#     for i in select_relust: # i就是每一个字典
#         for j in i.keys():  # j每一个字典的key
#             if type(i[j]) == datetime.date:
#                 i[j] = i[j].strftime("%Y-%m-%d")
#     curs.close()
#     conn.close()
#     return select_relust



def status_user():
    data = {
        "id":"77"
    }
    r =s.get(url=url+"/labUser/changeUserStates",params=data)
    print(r.text)

def conutbylogin():
    r = s.post(url=url+"/labUser/countByLogin")
    print(r.text)

def conutbyzc():
    r = s.post(url=url+"/labUser/countInRegisterByWeek")
    print(r.text)


def delete_user():
    data = {
        "id":"77"
    }
    r = s.delete(url=url+"/labUser/delUser",params=data)
    print(r.text)
def get_day_money():
    r = s.get(url=url+"/labUser/getDayMoney")
    print(r.text)

def get_month_money():
    r = s.get(url=url+"/labUser/getMonthMoney")
    print(r.text)
def get_name():
    data = {
        "name":"admin",
        "pageNum":1,
        "pageSize":10
    }
    r = s.get(url=url+"/labUser/getUserByName",params=data)
    print(r.text)

def getUserByName():
    data = {
        "states": 1,
        "pageNum": 1,
        "pageSize": 10
    }
    r = s.get(url=url + "/labUser/getUserByStates", params=data)
    print(r.text)

def getgetUserByVip():
    data = {
        "vip": 1,
        "pageNum": 1,
        "pageSize": 10
    }
    r = s.get(url=url + "/labUser/getUserByVip", params=data)
    print(r.text)

def getuser_now():
    r = s.get(url=url+"/labUser/getUserNow")
    print(r.text)
def getuser_num():
    r = s.get(url=url+"/labUser/getUserNum")
    print(r.text)
def getweekmoeny():
    r = s.get(url=url+"/labUser/getWeekMoney")
    print(r.text)
def cz_password():
    data = {
        "id":30
    }
    r = s.get(url=url+"/labUser/resetPassword",params=data)
    print(r.text)
def cz_status():
    data = {
        "id":30
    }
    r = s.get(url=url+"/labUser/updateUserStates",params=data)
    print(r.text)

#
# if __name__ == '__main__':
#     # print(login_miss())