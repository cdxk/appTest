#coding:utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time,os,yaml
from util import get_path
from common import logConf

log=logConf.logging
log.info("test")
url='http://pss-app-test.cddev.cddpi.com/#/'
getpath=open(get_path.getPath())
path =os.path.join(getpath+'capability.yaml')
file =open(path,encoding='utf-8')
#使用yaml加载yaml文件数据
data=yaml.load(file,yaml.FullLoader)
desired_caps = {'platformName': data['platformName'],
                'deviceName':data['deviceName'],
                'platformVersion': data['platformVersion'],
                'noReset': data['noReset'],
                'browserName':data['browserName']
                }
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
print('浏览器启动成功')
driver.get(url)
print(driver.contexts)
daiban="//span[contains(.,'待办的工单')]"  #根据标签内容进行定位
el1 =  driver.find_element_by_xpath(daiban)
print(el1.get_attribute('class'))
el1.click()





# driver.switch_to.context('NATIVE_APP')
# print('切换到原始APP成功')
# try:
#     WebDriverWait(driver,10,1).until(lambda x:x.find_element_by_xpath('//*[@text="否"]')).click()
#     print('翻译提示已出现')
# except:
#     print('翻译提示未出现')
# driver.switch_to.context('CHROMIUM')
# print('切换到CHROMIUM成功')
# WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_xpath('//*[@id="m-tabs-0-0"]/span/div/span')).click()
# print('点击拨号盘成功')
# WebDriverWait(driver,20,1).until(lambda x:x.find_element_by_xpath('xxxxx')).click()print('拨打按钮点击成功')