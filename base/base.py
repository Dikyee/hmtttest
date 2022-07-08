"""
    公共方法封装
"""
from time import sleep

import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_log()

class Base:
    # 初始化
    def __init__(self,driver):
        log.info(f"正在初始化driver：{driver}")
        self.driver = driver

    # 查找方法封装
    def base_find(self,loc,max_time=15,min_time=0.5):
        log.info(f"正在查找元素{loc}")
        return WebDriverWait(self.driver,timeout=max_time,poll_frequency=min_time).until(lambda x:x.find_element(*loc))

    # # 坐标点击
    # def app_target_click(self, x1, y1,loc):
    #     TouchAction(self.driver).tap(loc,x1,y1).perform()  # 模拟单手点击操作

    # 输入方法封装
    def base_input(self,loc,value):
        el = self.base_find(loc)
        log.info("正在清理信息")
        el.send_keys(Keys.CONTROL,"a")
        sleep(3)
        el.send_keys(Keys.DELETE)
        sleep(3)
        log.info("正在输入信息")
        el.send_keys(value)

    # 点击方法封装
    def base_click(self,loc):
        log.info(f"正在进行点击操作")
        self.base_find(loc).click()

    # 获取元素方法封装
    def base_get_text(self,loc):
        log.info(f"正在获取{loc}的信息")
        return  self.base_find(loc).text

    # 根据显示文本点击指定元素
    def base_click_element(self,element1,element2):
        loc = By.CSS_SELECTOR,f'{element1}'
        self.base_click(loc)
        sleep(3)
        loc2 = By.XPATH,f"//*[text()='{element2}']"
        self.base_click(loc2)

    # 跳转ifram
    def base_switch_ifram(self,fid):
        self.driver.switch_to_frame(fid)

    # 退出ifram页面
    def base_switch_default(self):
        self.driver.switch_to_default_content()


    # 获取图片
    def base_get_errimg(self):
        log.error("断言错误，正在截图")
        self.driver.get_screenshot_as_file("../imgs/eer.png")
        log.error("正在将截图写入报告")
        self._base_write_img()

    # 获取图片
    def base_get_infoimg(self):
        log.error("正在截图")
        self.driver.get_screenshot_as_file("../imgs/info.png")


    # 写入照片
    def _base_write_img(self):
        with open("../imgs/eer.png","rb") as f:
            allure.attach(f.read(),"错误原因",allure.attachment_type.PNG)

