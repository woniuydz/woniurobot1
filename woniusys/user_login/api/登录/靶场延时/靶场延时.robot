*** Settings ***
Library     woniusys.Pylib.api.api_lib
Force Tags   靶场延时
Suite Setup     获取token

*** Keywords ***
获取token
    ${result}    login      18339145881     111
    set suite variable      ${token}     ${result}[0]

*** Test Cases ***
靶场延时

    ${result}       shootGround time    ${token}     38
    should be equal     ${result}[msg]      延时失败, 倒计时小于30分钟才能延时,每次延时30分钟
    should be equal     ${result}[code]      ${201}
    ${len}      get length      ${result}[data]
    should be true      ${len}>=1