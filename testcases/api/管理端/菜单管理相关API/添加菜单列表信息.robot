*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api111.mysql_connect
Force Tags      登录
Suite Setup     获取token

*** Keywords ***
获取msg信息
        [Arguments]     ${menuName}     ${state}          ${expected}
        ${result}   add_menu_info       ${menuName}       ${state}      ${token}
        should be equal     ${result}       ${expected}
获取token
        ${info}    login         13456789012     admin
        set suite variable     ${token}   ${info}[0]

*** Test Cases ***
添加菜单列表信息
           add         1           添加成功
           ${empty}    1           添加成功
           add         ${empty}    添加成功
           add         1           添加成功
           ${empty}    ${empty}    添加成功