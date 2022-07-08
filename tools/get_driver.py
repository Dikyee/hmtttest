"""
  获取driver
"""
from time import sleep

from selenium import webdriver as webdriver
from appium import webdriver as appdriver


class GetDriver(object):
    web_driver = None
    app_driver = None

    @classmethod
    def get_driver(cls):
        if cls.web_driver is None:
            cls.web_driver = webdriver.Chrome()
            cls.web_driver.maximize_window()
            cls.web_driver.get('http://pc-toutiao-python.itheima.net/#/login')

        return cls.web_driver

    @classmethod
    def quit_driver(cls):
        if cls.web_driver :
            cls.web_driver.quit()
            cls.web_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.app_driver is None:
            disired_cap = {}
            disired_cap['platformName'] = 'Android'
            disired_cap['platformVersion'] = '10'
            disired_cap['deviceName'] = 'VBJDU18522004463'
            disired_cap['noReset'] = True
            disired_cap['appPackage'] = 'com.netease.newsreader.activity'
            disired_cap['appActivity'] = 'com.netease.nr.biz.ad.AdActivity'
            # disired_cap['automationName'] = 'UiAutomator1'
            # disired_cap['TrueunicodeKeyboard'] = True
            cls.app_driver = appdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_capabilities=disired_cap)
        return cls.app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.app_driver:
            cls.app_driver.quit()
            cls.app_driver = None

if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(5)
    GetDriver.quit_app_driver()



