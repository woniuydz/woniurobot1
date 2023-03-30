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
发表评论
    ${token}    获取token    13888998899     123123
    add_info     ${empty}        ${empty}        ${token}
    add_info     ${empty}        ${empty}        ${empty}
    add_info     1        ${empty}        ${token}
    add_info     ${empty}        13        ${token}
    add_info     ${empty}        10        ${token}