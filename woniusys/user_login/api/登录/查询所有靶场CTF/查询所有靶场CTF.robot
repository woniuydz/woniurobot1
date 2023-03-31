*** Settings ***
Library     woniusys.Pylib.api.api_lib
Force Tags   查询所有靶场CTF
Suite Setup     获取token

*** Keywords ***
获取token
    ${result}    login      18339145881     111
    set suite variable      ${token}     ${result}[0]

*** Test Cases ***
查询所有靶场CTF

    ${result}       find shootGroundctf    ${token}    1       10
    should be equal     ${result}[msg]      查询所有靶场CTF
    should be equal     ${result}[code]      ${200}
    ${len}      get length      ${result}[data]
    should be true      ${len}>=1