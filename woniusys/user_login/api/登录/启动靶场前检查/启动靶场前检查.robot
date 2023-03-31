*** Settings ***
Library     woniusys.Pylib.api.api_lib
Force Tags   启动靶场前检查
Suite Setup     获取token

*** Keywords ***
获取token
    ${result}    login      18339145881     111
    set suite variable      ${token}     ${result}[0]

*** Test Cases ***

启动靶场前检查接口

    log     ${token}
    start shootGround check    ${token}         1