*** Settings ***
Library     pylib.api_def
Variables     pylib.url_info



*** Test Cases ***
登录测试
       ${sj_jg}   login_miss
       log to console       ${sj_jg}
       ${yq_jg}         set variable        登陆成功
       should be equal     ${sj_jg}        ${yq_jg}



