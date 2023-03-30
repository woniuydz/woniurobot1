*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api111.mysql_connect
Force Tags      登录
Suite Setup     获取token

*** Keywords ***
获取msg信息
        [Arguments]     ${phone}     ${password}
        ${result}   login     ${phone}     ${password}
        return from keyword      ${result}[0]
获取token
        ${info}    login         13456789012     admin
        set suite variable     ${token}   ${info}[0]

*** Test Cases ***
删除系统菜单
    ${token}    获取token    15666644343     111111
    del_menu_info      21              ${token}
    del_menu_info      21              ${empty}
    del_menu_info      ${empty}        ${token}
    del_menu_info      ${empty}        ${empty}