*** Settings ***
Library     pylib.api.api_libb
#Library     pylib.api.mysql_connect
#Library     pylib.api.function
Variables     pylib.api.env
Suite Setup    login    13888998899     123123
Force Tags      add

*** Keywords ***
获取msg信息
        [Arguments]     ${managerName}     ${phone}          ${expected}
        ${result}   add_speaker_account     ${managerName}     ${phone}
        should be equal     ${result}       ${expected}


*** Test Cases ***
增加讲师账户
      [Tags]  tag1
      [Template]  获取msg信息
      user1           12345178141         新增成功
      user1           15666644343         该号码已被注册
      user1           ${empty}              访问失败