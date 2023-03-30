*** Settings ***
Library     woniusys.Pylib.api.api_lib
Force Tags   登录

*** Keywords ***
登录
    [Arguments]     ${phone}    ${password}     ${expect}
    ${result}      login       ${phone}    ${password}
    log to console      ${result}
    should be equal      ${result}[1]       ${expect}

*** Test Cases ***
正确电话号码和密码登录
    登录  18339145881     111     登陆成功

电话号码输入错误
    登录  18339145882     111     当前用户账号不存在

密码输入错误
    登录  18339145881     1234     密码错误