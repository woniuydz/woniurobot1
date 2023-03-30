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
    print(sj_jg)
    return sj_jg.get("msg"),phone
# add_user_1("19191945655")
# add_user_1("19595959599")
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

def r_table(sql):
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
    print(select_relust[0].get("states"))
    return select_relust[0].get("states")

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

def r_tb(sql):
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
    print(select_relust[0].get("id"))
    return select_relust[0].get("id")
def status_user(id):
    data = {
        "id":id
    }
    r =s.get(url=url+"/labUser/changeUserStates",params=data)
    print(r.text)

    sj = json.loads(r.text)
    return sj.get("msg"),id
# status_user("26")
def conutbylogin():#
    r = s.post(url=url+"/labUser/countByLogin")
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")
# conutbylogin()
def conutbyzc():
    r = s.post(url=url+"/labUser/countInRegisterByWeek")
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")



def delete_user(id):
    data = {
        "id":id
    }
    r = s.delete(url=url+"/labUser/delUser",params=data)
    print(r.text)
def get_day_money():
    r = s.get(url=url+"/labUser/getDayMoney")
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")

def get_month_money():
    r = s.get(url=url+"/labUser/getMonthMoney")
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")
def get_name(name):
    data = {
        "name":name,
        "pageNum":1,
        "pageSize":10
    }
    r = s.get(url=url+"/labUser/getUserByName",params=data)
    print(r.text)
    # sj = json.loads(r.text)
    # return sj.get("msg")
# get_name("")
def getuserbystates(states):
    data = {
        "states": states,
        "pageNum": 1,
        "pageSize": 10
    }
    r = s.get(url=url + "/labUser/getUserByStates", params=data)
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")
def getgetUserByVip(vip):
    data = {
        "vip": vip,
        "pageNum": 1,
        "pageSize": 10
    }
    r = s.get(url=url + "/labUser/getUserByVip", params=data)
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")

def getuser_now():
    r = s.get(url=url+"/labUser/getUserNow")
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")
def getuser_num():
    r = s.get(url=url+"/labUser/getUserNum")
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("data")
# getuser_num()
def r_tb_1(sql):
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
    # print(select_relust[0].get("id"))
    print(len(select_relust))
    return len(select_relust)
# r_tb_1("select * from lab_user")
def getweekmoeny():
    r = s.get(url=url+"/labUser/getWeekMoney")
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")
# getweekmoeny()
def cz_password(id):
    data = {
        "id":id
    }
    r = s.get(url=url+"/labUser/resetPassword",params=data)
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")
cz_password("1323312")
def cz_status(id):
    data = {
        "id":id
    }
    r = s.get(url=url+"/labUser/updateUserStates",params=data)
    print(r.text)
    sj = json.loads(r.text)
    return sj.get("msg")
#
# if __name__ == '__main__':
#     # print(login_miss())