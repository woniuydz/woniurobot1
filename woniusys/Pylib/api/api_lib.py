#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2023/3/28 16:38
from config import conf
import requests
import json

session = requests.session()

def login(phone,password):
    """
    登录接口
    :param phone: 电话号码登录
    :param password: 登录密码
    :return: 接口的返回体
    """
    param = {
        "phone":phone,
        "password":password
    }
    header = {"Content-Type":"application/json"}
    result = session.post(url=f"{conf}/labUser/passLogin",data=json.dumps(param),headers=header).text
    print(result)
    dict_a = json.loads(result)
    token = dict_a.get("data")
    msg = dict_a.get("msg")
    print(token)
    print(msg)
    return token,msg

def start_bachang(shootGroundId,token):
    """
    启动靶场
    :param shootGroundId: 靶场id
    :return:
    """
    param = {
        "shootGroundId": shootGroundId,
    }
    header = {"Content-Type":"application/json","com.woniuLab.user.token":token}
    result = session.post(url=f"{conf}/labShootGround/begin", data=json.dumps(param), headers=header).text
    print(result)
    return result

def stop_bachang(shootGroundId,token):
    """
    停止靶场
    :param shootGroundId: 靶场id
    :return:
    """
    param = {
        "shootGroundId": shootGroundId,
    }
    header = {"com.woniuLab.user.token":token}
    result = session.get(url=f"{conf}/labShootGround/stop", params=param, headers=header).text
    print(result)
    return result

if __name__ == '__main__':
    login("18339145881","111")
    start_bachang("17","1640973025392873472")
    stop_bachang("17","1640973025392873472")