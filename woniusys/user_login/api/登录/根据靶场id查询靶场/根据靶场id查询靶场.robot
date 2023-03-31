*** Settings ***
Library     woniusys.Pylib.api.api_lib
Force Tags   根据靶场id查询靶场
Suite Setup     获取token

*** Keywords ***
获取token
    ${result}    login      18339145881     111
    set suite variable      ${token}     ${result}[0]

*** Test Cases ***
根据靶场id查询靶场

    ${result}       find shootGround id    ${token}        38
    should be equal     ${result}[msg]      访问成功
    should be equal     ${result}[code]      ${200}
    ${len}      get length      ${result}[data]
    should be true      ${len}>=1