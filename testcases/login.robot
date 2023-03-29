*** Settings ***
Library     pylib.api_def
Variables     pylib.url_info



*** Test Cases ***
登录测试
       ${login}   login_miss
       log to console       ${login}
#        should be equal        login miss       miss



