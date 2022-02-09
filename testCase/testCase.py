import time,unittest
from time import sleep
from appium import webdriver
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
        sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_chrome(self):
        """打开h5页面"""
        self.driver.get("http://pss-app-test.cddev.cddpi.com/#/")
        sleep(5)
        self.driver.find_element_by_xpath("//span[contains(.,'故障处置')]").click()

if __name__=='__main__':
    unittest.main()
    # myTests().test_chrome()