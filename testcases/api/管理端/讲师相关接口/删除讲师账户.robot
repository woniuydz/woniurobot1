#*** Settings ***
#Library     pylib.api.api_libb
#Variables     pylib.api.env
##Library     pylib.api111.mysql_connect
#Force Tags      讲师111111------删不掉
#
#*** Keywords ***
#获取token
#        [Arguments]     ${phone}     ${password}
#        ${result}   login     ${phone}     ${password}
#        return from keyword      ${result}[0]
#
#*** Test Cases ***
#删除讲师账户
#    ${token}    获取token    15666644343     111111
#    del_speaker_account     20        ${token}
#    del_speaker_account     ${empty}    ${token}
#    del_speaker_account     11        ${empty}
#    del_speaker_account     ${empty}    ${token}

*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
Suite Setup     获取token
Force Tags      讲师


*** Keywords ***
获取msg信息
        [Arguments]     ${id}     ${expected}
        ${result}   del_speaker_account     ${id}        ${token}
        should be equal     ${result}       ${expected}
获取token
        ${info}    login       15666644343     111111
        set suite variable     ${token}        ${info}[0]

*** Test Cases ***
删除讲师账户
        [Template]  获取msg信息
        32                删除成功
#        ${empty}          前端传入id异常
#        1123              前端传入id异常      #   输入一个不存在的id