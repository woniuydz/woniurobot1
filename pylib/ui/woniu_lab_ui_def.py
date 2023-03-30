#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 2023/3/17 14:55
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def longin(phone,password):     #   login界面
    global browser
    browser = webdriver.Chrome()
    browser.get("http://192.168.120.10:90/#/login")
    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[1]/div/div[2]/input').send_keys(phone)
    time.sleep(0.5)
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[2]/div/div[2]/div/input').send_keys(password)
    time.sleep(0.5)
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[1]/div/div[2]/input').clear()
    time.sleep(0.5)
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[2]/div/div[2]/div/input').clear()
    time.sleep(0.5)
    browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[3]/div/button').click()   #点击登录
    time.sleep(0.5)

def refresh():           #   刷新页面
    browser.refresh()
    time.sleep(0.5)
def back():
    browser.back()
def quit():             #   关闭浏览器
    browser.quit()
    time.sleep(0.5)
def assert_login():
    if len(browser.find_elements(By.XPATH, '//*[@id="app"]/section/header/div[2]/span')) == 1:
        return browser.find_element(By.XPATH, '//*[@id="app"]/section/header/div[2]/span').text
    elif browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[1]/div/div[3]').text:
        return browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[1]/div/div[3]').text
    elif browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[2]/div/div[3]').text:
        return browser.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/form/div[2]/div/div[3]').text

def update_password(oldpassword,newpassword,checkpassword):
    pass




if __name__ == '__main__':

    longin('15666644343', 111111)

