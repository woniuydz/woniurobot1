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

def start_shootGround(shootGroundId,token):
    """
    启动靶场
    :param shootGroundId: 靶场id
    :param token: 已登录的token
    :return:
    """
    param = {
        "shootGroundId": shootGroundId,
    }
    header = {"Content-Type":"application/json","com.woniuLab.user.token":token}
    result = session.post(url=f"{conf}/labShootGround/begin", data=json.dumps(param), headers=header).text
    print(result)
    return result

def stop_shootGround(shootGroundId,token):
    """
    停止靶场
    :param shootGroundId: 靶场id
    :param token: 已登录的token
    :return:
    """
    param = {
        "shootGroundId": shootGroundId,
    }
    header = {"com.woniuLab.user.token":token}
    result = session.get(url=f"{conf}/labShootGround/stop", params=param, headers=header).text
    print(result)
    return result

def start_shootGround_check(token,shootGroundId):
    """
    启动靶场前检查
    :param token:已登录的token
    :param shootGroundId:靶场id
    :return:
    """
    param = {
        "shootGroundId": shootGroundId,
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/stop", params=param, headers=header).text
    print(result)
    return result

def shootGround_time(token,shootGroundId):
    """
    靶场延时
    :param token: 已登录的token
    :param shootGroundId: 靶场id
    :return:
    """
    param = {
        "shootGroundId": shootGroundId,
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/delayed", params=param, headers=header).text
    print(result)
    result = json.loads(result)
    return result

def download_excl(token,shootGroundId):
    """
    下载文件接口
    :param token:已登录的token
    :param shootGroundId:靶场id
    :return:
    """
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/download/{shootGroundId}", headers=header).text
    print(type(result))
    result = json.loads(result)
    print(result)
    return result

def find_shootGround(token,pageNum,pageSize):
    """
    查询所有靶场
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:一页多少行数据
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize": pageSize,
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/searchAllShootGroud", params=param, headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_shootGroundctf(token,pageNum,pageSize):
    """
    查询所有靶场CTF
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:一页多少行数据
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize": pageSize,
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/searchAllShootGroudCtf", params=param, headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_labShootGround(token,freeType,pageNum,pageSize):
    """
    根据靶场价格查询靶场
    :param token:已经登录的token
    :param freeType:靶场空闲状态
    :param pageNum:页码
    :param pageSize:一页多少行数据
    :return:
    """
    param = {
        "freeType": freeType,
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    header ={"Content-Type":"application/json","com.woniuLab.user.token":token}
    result = session.post(url=f"{conf}/labShootGround/searchForFreeType", data=json.dumps(param), headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_labShootGroundCTF(token,freeType,pageNum,pageSize):
    """
    根据靶场价格查询靶场CTF
    :param token:已经登录的token
    :param freeType:靶场空闲状态
    :param pageNum:页码
    :param pageSize:一页多少行数据
    :return:
    """
    param = {
        "freeType": freeType,
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    header ={"Content-Type":"application/json","com.woniuLab.user.token":token}
    result = session.post(url=f"{conf}/labShootGround/searchForFreeTypeCTF", data=json.dumps(param), headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_shootGround_id(token,shootGroundId):
    """
    根据靶场Id查询靶场
    :param token:已经登录的token
    :param shootGroundId:靶场id
    :return:
    """
    param = {
        "shootGroundId": shootGroundId,
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/searchForId", params=param, headers=header).text
    result = json.loads(result)
    print(type(result))
    return result

def find_shootGround_level(token,level,pageNum,pageSize):
    """
    根据靶场难度查询靶场
    :param token:已经登录的token
    :param level:靶场难度
    :param pageNum:页码
    :param pageSize:一页多少行数据
    :return:
    """
    param = {
        "level": level,
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    header = {"Content-Type": "application/json", "com.woniuLab.user.token": token}
    result = session.post(url=f"{conf}/labShootGround/searchForLevel", data=json.dumps(param),
                          headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_shootGround_level_CTF(token,level,pageNum,pageSize):
    """
    根据靶场难度查询靶场CTF
    :param token:已经登录的token
    :param level:靶场难度
    :param pageNum:页码
    :param pageSize:一页多少行数据
    :return:
    """
    param = {
        "level": level,
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    header = {"Content-Type": "application/json", "com.woniuLab.user.token": token}
    result = session.post(url=f"{conf}/labShootGround/searchForLevelCTF", data=json.dumps(param),
                          headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_shootGround_searchForStudyCount(token,pageNum,pageSize ):
    """
    默认根据靶场热度查询靶场
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:每页有多少条数据
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize":pageSize
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/searchForStudyCount", params=param, headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_shootGround_searchForStudyCount_CTF(token,pageNum,pageSize ):
    """
    默认根据靶场热度查询靶场CTF
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:每页有多少条数据
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize":pageSize
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/searchForStudyCountCTF", params=param, headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_shootGround_type(token,pageNum,pageSize,type):
    """
    根据靶场类别查询靶场
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:每页有多少条数据
    :param type:查询类型
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize": pageSize,
        "type":type
    }
    header = {"Content-Type": "application/json", "com.woniuLab.user.token": token}
    result = session.post(url=f"{conf}/labShootGround/searchForType", data=json.dumps(param),
                          headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_shootGround_typeCTF(token,pageNum,pageSize,type):
    """
    根据靶场类别查询靶场
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:每页有多少条数据
    :param type:查询类型
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize": pageSize,
        "type":type
    }
    header = {"Content-Type": "application/json", "com.woniuLab.user.token": token}
    result = session.post(url=f"{conf}/labShootGround/searchForTypeCTF", data=json.dumps(param),
                          headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_VIP_shootGround(token,pageNum,pageSize):
    """
    查询VIP尊享靶场
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:每页有多少条数据
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/searchVipShootGroud", params=param, headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_VIP_shootGroundCTF(token,pageNum,pageSize):
    """
    查询VIP尊享靶场CTF
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:每页有多少条数据
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labShootGround/searchVipShootGroudCTF", params=param, headers=header).text
    result = json.loads(result)
    print(result)
    return result

def find_Pass_Controller(token,pageNum,pageSize):
    """
    查询我的通关实验记录
    :param token:已经登录的token
    :param pageNum:页码
    :param pageSize:每页有多少条数据
    :return:
    """
    param = {
        "pageNum": pageNum,
        "pageSize": pageSize
    }
    header = {"com.woniuLab.user.token": token}
    result = session.get(url=f"{conf}/labUserPass/getLabUserPass", params=param, headers=header).text
    result = json.loads(result)
    print(result)
    return result

if __name__ == '__main__':
    a = login("18339145881","111")
    # start_shootGround("13",a[0])
    # stop_shootGround("13",a[0])
    # shootGround_time(a[0],"38")
    # download_excl(a[0],"38")
    # find_shootGround(a[0],"1","10")
    # find_shootGroundctf(a[0],"1","10")
    # find_labShootGround(a[0],"2","1","10")
    # find_labShootGroundCTF(a[0],"2","1","10")
    # find_shootGround_id(a[0],"10")
    # find_shootGround_level(a[0],"ESAY","1","10")
    # find_shootGround_level(a[0],"ESAY","1","10")
    # find_shootGround_searchForStudyCount(a[0],"1","10")
    # find_shootGround_searchForStudyCount_CTF(a[0],"1","10")
    # find_shootGround_type(a[0],"1","10","SCAN")
    # find_shootGround_typeCTF(a[0],"1","10","SCAN")
    # find_VIP_shootGround(a[0],"1","10")
    # find_VIP_shootGround(a[0],"1","10")
    find_Pass_Controller(a[0],"1","10")