*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api.mysql_connect
Force Tags      管理端登录

*** Keywords ***
登录测试
        [Arguments]     ${phone}     ${password}     ${expected}
        ${result}  login     ${phone}        ${password}
        should be equal      ${result}[1]    ${expected}
        log to console       ${result}[0]
        log to console       ${result}[1]

*** Test Cases ***
登录
    [Tags]  tag1
    [Template]  登录测试
    15666644343     111111        登陆成功
    ${empty}        111111        手机号码格式错误
    15666644343     ${empty}      密码错误
    ${empty}        ${empty}      手机号码格式错误