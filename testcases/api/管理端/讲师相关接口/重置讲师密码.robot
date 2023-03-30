*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
Suite Setup     获取token
Force Tags      讲师


*** Keywords ***
获取msg信息
        [Arguments]     ${id}     ${expected}
        ${result}   chongzhi_speaker_password     ${id}        ${token}
        should be equal     ${result}       ${expected}
获取token
        ${info}    login       15666644343     111111
        set suite variable     ${token}        ${info}[0]

*** Test Cases ***
重置讲师账户密码
        [Template]  获取msg信息
        33                重置成功
#        ${empty}          服务器繁忙
#        1123              前端传入id异常      #   输入一个不存在的id