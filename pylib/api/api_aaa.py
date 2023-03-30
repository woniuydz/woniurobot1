#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2023/3/16 9:55
import json
import requests
from pylib.api111.env import url, uu

session =requests.session()

#   管理端--登录
def login(phone,password):
    param = {'phone':phone,
             'password':password
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.post(url = f'{url}/labManager/login',data=js_data,headers=header)
    re_result = json.dumps(re.text)
    data = re.json()
    msg = data.get('msg')
    token = data.get('data')
    return token,msg
    # return token

    # a =  re_result.get('mst'), re_result.get('data')
    # return re_result.get('mst'), re_result.get('data')

#   添加实验
def add_lab():
    param = {"dockerNetName": "db",
             "experimentAim": "php反序列化场景",
             "experimentFlag": "abc123",
             "experimentName": "php反序列化",
             "experimentResult": "本实验主要考察PHP反序列化的利用、POP链的构造及常见的绕过方式",
             "experimentScene": "学会php反序列化",
             "experimentSteps": "第一关\n1、看到源码，本题需要绕过一个__wakeup()函数和一个正则匹配，才能显示出 f15g_1s_here.php 文件。\n2、绕过__wakeup()：在反序列化执行之前，会先执行__wakeup这个魔术方法，所以需要绕过。",
             "experimentTips": "无",
             "experimentTool": "浏览器",
             "inPath": "/tmp/app/",
             "inPort": 88,
             "preKnowledge": "php，反序列化",
             "shootGroundId": 1,
             "upFilePath": "D:\\java",
             "userId": 1
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.post(url = f'{url}/labExperiment/addExperiment',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   查询实验
def select_lab():
    param = {"experimentName": "1"}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labExperiment/getExperiment',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   删除实验.robot
def del_lab():
    param = {"id": "19"
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.delete(url = f'{url}/labExperiment/delExperiment',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   查询会员购买记录.robot
def select_huiyuan_buy_jilu(token):
    param = {"pageNum": 1,
             "pageSize": 10
             }
    js_data = json.dumps(param)
    # header = {"Content-Type": "application/json"}
    header = {'com.woniuxy.woniulab.manage.token':token,"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labVip/getVipBuy',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   增加讲师账户
def add_speaker_account(managerName,phone):
    param = {"managerName": managerName,
             "phone": phone
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.post(url = f'{url}/labManager/addManager',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   禁用讲师账户
def jinyong_speaker_account(id):
    param = {"id": id}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labManager/disEnableManager',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   启用讲师账户
def qiyong_speaker_account(id):
    param = {"id": id}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labManager/enableManager',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   查询讲师账户
def select_speaker_account(pageNum=None,pageSize=None,searchName=None):
    param = {"pageNum": pageNum,
             "pageSize":pageSize,
             "searchName":searchName
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labManager/getManager',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

# #   修改密码
# def update_password(oldPassword,password,token):
#     param = {"oldPassword": oldPassword,
#              "password":password}
#     js_data = json.dumps(param)
#     header = {'com.woniuxy.woniulab.manage.token':token,"Content-Type": "application/json"}
#     re = session.put(url = f'{url}/labManager/updatePwd',data=js_data,headers=header)
#     print(re.text)
#     print(js_data)
#     print(re.url)

#   重置讲师账户密码
def chongzhi_speaker_password(id):
    param = {"id": id}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labManager/removeManager',params=param,headers=header)
    print(re.text)
    print(param)
    print(re.url)

#   修改密码
def update_password(oldPassword,password):
    param = {"oldPassword": oldPassword,
             "password":password}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.put(url = f'{url}/labManager/updatePwd',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   删除讲师账户
def del_speaker_account(id):
    param = {"id": id}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.delete(url = f'{url}/labManager/delManager',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   添加菜单列表信息
def add_menu_info(menuName,state):
    param = {"menuName": menuName,
             "state": state
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.post(url = f'{url}/labMenuManage/add',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   查询菜单列表信息
def select_menu_info(menuName=None):
    param = {"menuName": menuName}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labMenuManage/get',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   修改菜单列表信息
def update_menu_info(id,menuName,state):
    param = {"id": id,
             "menuName": menuName,
             "state": state}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.put(url = f'{url}/labMenuManage/update',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   删除系统菜单
def del_menu_info():
    param = {"menuId": "16"}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.delete(url = f'{url}/labMenuManage/delete',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   查询当前靶场所有评论
def select_bachang_pinglun(pageNum,pageSize,shootGroundId):
    param = {"pageNum": pageNum,
             "pageSize": pageSize,
             "shootGroundId": shootGroundId}
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{url}/labComments/getAllLabBill',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   用户端--登录
def login_user(password,phone):
    param = {'password':password,
             'phone':phone
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.post(url = f'{uu}/labUser/passLogin',data=js_data,headers=header)
    # print(re.text)
    # # print(js_data)
    # # print(re.url)
    # # print(re.text)
    # # return re.data
    data = re.json()
    token = data.get('data')
    # print(token)
    return token

#   查询我的通关实验记录
def select_info(pageNum=None,pageSize=None):
    param = {'pageNum':pageNum,
             'pageSize':pageSize
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{uu}/labUserPass/getLabUserPass',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   发表评论
def add_info(content,shootGroundId):
    param = {'content':content,
             'shootGroundId':shootGroundId
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.post(url = f'{uu}/labComments/addLabComments',data=js_data,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

#   查询当前靶场所有评论
def user_select_bachang_info(pageNum,pageSize,shootGroundId):
    param = {'pageNum':pageNum,
             'pageSize':pageSize,
             'shootGroundId':shootGroundId
             }
    js_data = json.dumps(param)
    header = {"Content-Type": "application/json"}
    re = session.get(url = f'{uu}/labComments/getAllLabComments',params=param,headers=header)
    print(re.text)
    print(js_data)
    print(re.url)

if __name__ == '__main__':
    pass
    # print(login(13888998899,"123123"))
    # token = login(13888998899,"123123")

    # del_lab()
    # del_speaker_account()
    # del_menu_info()

    # add_lab()       #   靶场不存在
    # select_lab()
    # select_huiyuan_buy_jilu(token)
    # add_speaker_account("abc",13212345670)      # id = 1122
    # jinyong_speaker_account(20,token)
    # qiyong_speaker_account(20,token)
    # select_speaker_account(token)
    # chongzhi_speaker_password(20,token)
    # update_password("123123","123123",token)
    # add_menu_info("aaa",0,token)
    # select_menu_info(token)
    # update_menu_info(21,"qqq",0,token)
    # select_bachang_pinglun(10,10,10,token)


    # login_user("111",13212345678)
    # a = login_user("111",13212345678)
    # select_info(a,10,10)
    # # select_info()
    # add_info(a,"你好",1)
    # user_select_bachang_info(a,10,1,10)
