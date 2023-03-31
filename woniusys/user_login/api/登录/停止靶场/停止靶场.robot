*** Settings ***
Library     woniusys.Pylib.api.api_lib
Force Tags   停止靶场

*** Keywords ***
获取token
    [Arguments]     ${phone}    ${password}
    ${result}   login    ${phone}    ${password}
    return from keyword     ${result}[0]
*** Test Cases ***

停止靶场接口
      ${token}      获取token   18339145881     111
      log    ${token}
      ${result_1}   stop shootGround      38        ${token}
      log   ${result_1}