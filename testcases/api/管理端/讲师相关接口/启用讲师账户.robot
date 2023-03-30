*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
Suite Setup     获取token
Force Tags      讲师

*** Keywords ***
获取msg信息
        [Arguments]     ${id}     ${expected}
        ${result}   qiyong_speaker_account     ${id}        ${token}
        should be equal     ${result}       ${expected}
获取token
        ${info}    login         13456789012     admin
        set suite variable     ${token}   ${info}[0]

*** Test Cases ***
启用讲师账户
    [Template]  获取msg信息
     20            启用成功
     ${empty}      前端传入id异常
     1123              前端传入id异常      #   输入一个不存在的id