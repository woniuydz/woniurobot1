*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api111.mysql_connect
Force Tags      用户

*** Keywords ***
获取token
        [Arguments]     ${phone}     ${password}
        ${result}   login_user     ${phone}     ${password}
        return from keyword      ${result}[0]

*** Test Cases ***
查询我的通关实验记录
    ${token}    获取token    13923605762     aaa
    select_info     ${empty}        ${empty}        ${token}
    select_info     ${empty}        ${empty}        ${empty}
    select_info     1        ${empty}        ${token}
    select_info     ${empty}        20        ${token}