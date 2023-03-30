*** Settings ***
Library     pylib.api.api_libb
Variables     pylib.api.env
#Library     pylib.api111.mysql_connect
Force Tags      用户

*** Keywords ***
获取token
        [Arguments]     ${phone}     ${password}
        ${result}   login_user     ${phone}     ${password}
        return from keyword        ${result}[0]

*** Test Cases ***
查询当前靶场所有评论
    ${token}    获取token    13923605762     aaa
    user_select_bachang_info     ${empty}       ${empty}      ${empty}    ${token}
    user_select_bachang_info     ${empty}       ${empty}      ${empty}    ${empty}
    user_select_bachang_info     ${empty}       ${empty}      13          ${token}
    user_select_bachang_info     ${empty}       50            ${empty}    ${token}
    user_select_bachang_info     1              ${empty}      ${empty}    ${token}
    user_select_bachang_info     ${empty}       ${empty}      ${empty}    ${token}