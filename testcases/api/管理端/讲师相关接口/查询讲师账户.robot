*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api111.mysql_connect
Force Tags      讲师
Suite Setup     获取token

*** Keywords ***
获取msg信息
        [Arguments]     ${pageNum}     ${pageSize}    ${searchName}      ${expected}
        ${result}   select_speaker_account      ${token}       ${pageNum}     ${pageSize}    ${searchName}
        should be equal     ${result}       ${expected}

获取token
        ${info}    login         13456789012     admin
        set suite variable     ${token}   ${info}[0]

*** Test Cases ***


查询讲师账户
    [Template]  获取msg信息
#    ${token}    获取token    13888998899     123123
    1            30           测试用---            查询成功
    1            30           ${empty}           查询成功
    1            ${empty}           测试用---            查询成功
    ${empty}            30           测试用---            查询成功
    ${empty}     ${empty}     ${empty}            查询成功
    5           1               add      查询成功
