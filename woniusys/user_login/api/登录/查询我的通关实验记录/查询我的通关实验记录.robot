*** Settings ***
Library     woniusys.Pylib.api.api_lib
Force Tags   查询我的通关实验记录
Suite Setup     获取token

*** Keywords ***
获取token
    ${result}    login      18339145881     111
    set suite variable      ${token}     ${result}[0]

*** Test Cases ***
查询我的通关实验记录

    ${result}       find Pass Controller    ${token}    1       10
    should be equal     ${result}[msg]      查询通关实验记录成功
    should be equal     ${result}[code]      ${200}
    ${len}      get length      ${result}[data]
    should be true      ${len}>=1