#*** Settings ***
#Library     pylib.api111.api_aaa
#Variables     pylib.api111.env
#Library     pylib.api111.mysql_connect
#Force Tags      登录
#Suite Setup     登录测试    13888998899     123123
#
#*** Keywords ***
#登录测试
#        [Arguments]     ${phone}     ${password}
#        ${result}  login     ${phone}     ${password}
##        should be equal     ${result}[1]    ${expected}
#        log to console      ${result}[0]
