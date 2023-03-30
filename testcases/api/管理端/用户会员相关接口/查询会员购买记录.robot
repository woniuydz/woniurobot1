*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api111.mysql_connect
Force Tags      查询会员购买记录

*** Keywords ***
获取token
        [Arguments]     ${phone}     ${password}
        ${result}   login     ${phone}     ${password}
        return from keyword      ${result}[0]

*** Test Cases ***
查询会员购买记录
    ${token}    获取token    15666644343     111111
    select_huiyuan_buy_jilu     ${token}
    select_huiyuan_buy_jilu     ${empty}
