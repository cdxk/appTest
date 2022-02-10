import time,unittest
from time import sleep
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
#故障处置提交
class myTests(unittest.TestCase):
    #测试开始前执行的方法
    @classmethod
    def setUpClass(cls):
        desired_caps={'platformName': 'Android',
                'deviceName': '127.0.0.1:21503',
                'platformVersion': '7.1.2',
                'noReset': True,
                'browserName':'Chrome'
                }
        cls.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) #连接appium
        sleep(1)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_chrome(self):
        """打开h5页面"""
        self.driver.get("http://pss-app-test.cddev.cddpi.com/#/")
        sleep(5)
        self.driver.find_element_by_xpath("//span[contains(.,'故障处置')]").click()
        sleep(2)
        input=self.driver.find_element_by_xpath("//input[contains(@placeholder,'请输入标题')]")
        input.clear() #清空文本框内容
        input.send_keys("标题")   #设置文本框内容
        # print(input.get_attribute('value'))#获取文本框内容
        self.driver.find_element_by_xpath("//input[contains(@placeholder,'请选择故障类型')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//span[contains(.,'线上故障')]").click()
        self.driver.find_element_by_xpath("//span[contains(.,'网络故障')]/..").click()
        self.driver.find_element_by_xpath("//input[contains(@placeholder,'请输入故障发生地点')]").send_keys('故障发生地点')
        self.driver.find_element_by_xpath("//input[contains(@placeholder,'请选择故障发生时间')]").click()
        self.driver.find_element_by_xpath("//button[contains(.,'确认')]").click()
        while  1:
            try:
                sleep(5)
                elem = self.driver.find_element_by_xpath("//button[contains(.,'确认')]")
                print('exception')
                print(elem)
                elem.click()
            except Exception as  e:
                print("关闭时间控件")
                break

        # js = "var q = document.documentElement.scrollTop = 10000"
        # self.driver.execute_script(js)
        # print(self.driver.find_element_by_xpath("//input[contains(@placeholder,'请选择厂调审核人')]").get_attribute(
        #     'placeholder'))
        # sleep(5)
        self.driver.find_element_by_xpath("//input[contains(@placeholder,'请选择厂调审核人')]").click()
        sleep(2)
        print(self.driver.find_elements_by_xpath(
            "//div[contains(@style,'transform: translate3d(0%, 0px, 0px); transition-duration: 0.3s;')]/div/div/ul/li")[
                  1].text)
        self.driver.find_elements_by_xpath(
            "//div[contains(@style,'transform: translate3d(0%, 0px, 0px); transition-duration: 0.3s;')]/div/div/ul/li")[
            1].click()
        sleep(2)
        self.driver.find_element_by_xpath("//span[contains(.,'提交')]/../..").submit()





if __name__=='__main__':
    unittest.main()
    # myTests().test_chrome()