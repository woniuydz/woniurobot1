#*** Settings ***
#Library     pylib.api.api_libb
#Variables     pylib.api.env
##Library     pylib.api111.mysql_connect
#Force Tags      实验
#
#*** Keywords ***
#获取token
#        [Arguments]     ${phone}     ${password}
#        ${result}   login     ${phone}     ${password}
#        return from keyword      ${result}[0]
#
#*** Test Cases ***
#添加实验
#    ${token}    获取token    15666644343     111111
#    add_lab     ${token}
#    add_lab     ${empty}
