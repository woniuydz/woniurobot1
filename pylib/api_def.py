#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2023/3/27 15:45
import json

import requests

import random
sj = random.randint(1,9999)
from pylib.url_info import *
s = requests.session()
def php():
    re = s.get(url="192.168.120.2:8090/labPhpVersion/getAllPhp")
    print(re.text)
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
    return re.text

login_miss()
def TOMCat():
    r= s.get(url=url+"/labTomcatVersion/getAllTomcat")
    print(r.text)


def add_user():
    data = {
        "phone":f"1599999{sj}"
    }
    r = s.get(url=url+"/labUser/addUser",params=data)
    print(r.text)

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


if __name__ == '__main__':
    print(login_miss())