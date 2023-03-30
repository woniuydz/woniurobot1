#*** Settings ***
#Library     pylib.api111.api_libb
#Variables     pylib.api111.env
##Library     pylib.api111.mysql_connect
#Force Tags      实验
#
#*** Keywords ***
#获取token
#        [Arguments]     ${phone}     ${password}
#        ${result}   login     ${phone}     ${password}
#        log to console      ${result}[0]
#
#*** Test Cases ***
#查询
#    ${token}    获取token    13888998899     123123
#    select_lab     ${token}
#    select_lab     ${empty}