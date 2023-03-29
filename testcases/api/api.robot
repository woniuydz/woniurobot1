*** Settings ***
Library     pylib.api_def
Variables     pylib.url_info
Force Tags  接口测试
Suite Setup         login_miss




*** Keywords ***
新增配置
        [Arguments]         ${phone}        ${yq}
        ${sj}       add user 1          ${phone}
        should be equal         ${sj}           ${yq}



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


添加用户测试传参版
        [Template]      新增配置
        15095889220         添加成功        #正常添加
        菜鸡菜鸡        服务器繁忙           #电话号码输入中文添加
        1111        服务器繁忙           #输入电话号码少于11位添加
        150945684720               添加成功                          #输入电话号码超出11位添加，按逻辑来说应该是提示用户输入号码不符合规则
        asdfasfa        服务器繁忙           #电话号码输入字母添加