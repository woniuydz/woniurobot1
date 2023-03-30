*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
Suite Setup     获取token
Force Tags      讲师


*** Keywords ***
获取msg信息
        [Arguments]     ${oldPassword}     ${password}     ${expected}
        ${result}   update_password     ${oldPassword}     ${password}      ${token}
        should be equal     ${result}       ${expected}
获取token
        ${info}    login       14555555555     111111
        set suite variable     ${token}        ${info}[0]


*** Test Cases ***
修改密码
        [Template]   获取msg信息
         111111               111111      修改成功
         ${empty}        111111      密码错误           #bug
#         111111          111111      密码错误
         ${empty}        ${empty}    密码错误          #bug