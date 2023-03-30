*** Settings ***
Library     pylib.api_def
Variables     pylib.url_info
Force Tags  接口测试
Suite Setup         login_miss     #前置：登录




*** Keywords ***
新增配置
        [Arguments]         ${phone}        ${yq}
        ${sj}       add user 1          ${phone}
        should be equal         ${sj}[0]           ${yq}
根据用户名查询配置
            [Arguments]     ${name}     ${yq}

            ${sj}       get_name    ${name}
            should be equal             ${yq}           ${sj}



*** Test Cases ***
php接口
    ${sj_jg}        php
    log to console      ${sj_jg}
    ${yq}   convert to integer    200
    should be equal     ${sj_jg}       ${yq}


TOMCat接口

        ${sj}       TOMCat
        log to console      ${sj}
        ${yq}      convert to integer    200
        should be equal     ${sj}       ${yq}


添加用户测试

        ${sj1}       add_user
        log to console      ${sj1}[0]
        ${yq1}      set variable         添加成功
        should be equal         ${sj1}[0]       ${yq1}
        ${sql}=     set variable    select phone from lab_user where phone=${sj1}[1]
        ${sj}       retrieve table      ${sql}
        should be equal     ${sj}       ${sj1}[1]   #这个sj1有两个返回值一个是实际结果第二个是预期结果
        [Teardown]      cud_table       DELETE FROM lab_user where phone=${sj1}[1]

添加用户测试传参版
        [Template]      新增配置
        15095889220         添加成功        #正常添加
        菜鸡菜鸡        服务器繁忙           #电话号码输入中文添加
        1111        服务器繁忙           #输入电话号码少于11位添加
        150945684720               添加成功                          #输入电话号码超出11位添加，按逻辑来说应该是提示用户输入号码不符合规则
        asdfasfa        服务器繁忙           #电话号码输入字母添加



启用用户
        ${id}=  convert to integer           28
        ${sj}       status user         ${id}
        ${yq}=      set variable        启用用户成功
        should be equal     ${sj}[0]       ${yq}
        ${sj1}        r_table       select states FROM lab_user where id=${id}
        should be equal         ${sj1}          ${1}


查询本周活跃人数
        ${sj}           conutbylogin
        ${yq}=  set variable    访问成功
        should be equal     ${sj}       ${yq}

统计本周活跃人数
        ${sj}       conutbyzc
        ${yq}=  set variable    访问成功
        should be equal     ${sj}       ${yq}

根据id删除用户
        ${bz}       add user_1      15656464646
        log to console  ${bz}[1]
        ${id}       r_tb        select id from lab_user where phone=${bz}[1]
        ${sj}       delete user     ${id}
        ${yq}=  set variable           ${None}
        should be equal     ${sj}       ${yq}



统计本日收入
        ${sj}       get_day_money
        ${yq}=  set variable       访问成功
        should be equal     ${sj}       ${yq}

统计本月收入
        ${sj}       get_month_money
        ${yq}=  set variable       访问成功
        should be equal     ${sj}       ${yq}


根据用户名查询
            [Template]      根据用户名查询配置
            测试用请务删      查询成功        #用存在的用户名查询
            ${EMPTY}           查询成功     #输入空查询
            胡涛          查询成功        #输入不存在的用户名查询，逻辑上来说应该提示用户不存在但是实际是查询成功

根据用户状态查询





