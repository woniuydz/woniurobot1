*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api111.mysql_connect
Force Tags      靶场



*** Keywords ***
获取token
        [Arguments]     ${phone}     ${password}
        ${result}   login     ${phone}     ${password}
        return from keyword      ${result}[0]

*** Test Cases ***
查询当前靶场所有评论
    ${token}    获取token    15666644343     111111
    select_bachang_pinglun     1            100            1           ${token}
    select_bachang_pinglun     ${empty}     100            1           ${token}
    select_bachang_pinglun     1            ${empty}       1           ${token}
    select_bachang_pinglun     1            100            ${empty}    ${token}
    select_bachang_pinglun     1            100            1           ${token}
    select_bachang_pinglun     ${empty}     ${empty}       ${empty}    ${empty}