# encoding:utf-8

import requests, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


base_aima_url = 'http://api.f02.cn/http.do?action='
uid = 'jiuyueguang'
pwd = '765081406'
yuyue_pid = '101'  # 就预约这个项目而言的pid=101
login_url = base_aima_url + ('loginIn&uid=%s&pwd=%s' % (uid, pwd))
resp = requests.get(login_url)
token = resp.text[len(uid) + 1:]

by_types = {'id': By.ID, 'class': By.CLASS_NAME, 'tag': By.TAG_NAME}


def get_mobile_num(mobile=''):
    mobile_url = base_aima_url + (
        'getMobilenum&pid=%s&uid=%s&token=%s&size=1&mobile=' % (yuyue_pid, uid, token)) + mobile
    resp = requests.get(mobile_url)
    mobile_num = resp.text[:11]
    return mobile_num
    pass


def get_code_and_release_mobile_num(mobile_num):
    code_url = base_aima_url + ('getVcodeAndReleaseMobile&uid=%s&token=%s&mobile=%s' % (uid, token, mobile_num))
    text = requests.get(code_url).test
    start = text.find('为') + len('为')
    end = start + 6
    return text[start:end]
    pass


def get_element(driver, by_type, value):
    try:
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((by_types[by_type], value)))
    except:
        return None
    return driver.find_element(by_types[by_type], value)
    pass


def yuyue():
    url = 'http://bj.58.com/jiancai/21489702398110x.shtml?PGTID=14285722666260.07828750674570628&ClickID=1'
    driver = webdriver.Firefox()
    driver.get(url)

    ele_yuyue = get_element(driver, 'class', 'abtn')
    if ele_yuyue:
        ele_yuyue.click()
        time.sleep(5)
    ele_month = get_element(driver, 'id', 'getMonth_hy')
    if ele_month:
        ele_month.send_keys('2015-09-10')
        time.sleep(10)

    pass


if __name__ == '__main__':
    print token
    # get_mobile_num()
    # yuyue()
    a = '验证码为123456，s'
    start = a.find('为') + len('为')
    end = start + 6
    print a[start:end]
    pass
