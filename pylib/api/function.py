#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2023/3/16 19:16
def gaindata(list_a,keyword,list_c=None):#列表套字典  list_a 为数据库查询的结果，list_c需对比的数据为列表，keyword为提取数据库结果的关键字
    list_b=[]
    for i in list_a:
        list_b.append(str(i[keyword]))
    if list_c !=None:
        if set(list_b)==set(list_c):   #用集合判断两个列表是否相等
            return True
    else:
        return list_b







