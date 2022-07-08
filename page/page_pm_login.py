from time import sleep

from base.base import Base
from selenium.webdriver.common.by import By

from tools.get_log import GetLog

log = GetLog.get_log()
class PageElement(object):
    # 获取元素
    def __init__(self,driver):
        #公用方法
        self.base = Base(driver)
        # 用户名元素
        self.username = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        # 验证码元素
        self.code = (By.CSS_SELECTOR, '[placeholder="验证码"]')
        # 登入按钮
        self.login_btn = (By.CSS_SELECTOR, '[class="el-button el-button--primary"]')
        # 用户名
        self.usertext = (By.CSS_SELECTOR,'[class="user-name"]')

    def page_input_username(self,username):
        log.info(f"输入用户名：{username}")
        self.base.base_input(self.username,username)

    def page_input_code(self,code):
        log.info(f"输入验证码：{code}")
        self.base.base_input(self.code,code)

    def page_click_login_btn(self):
        sleep(3)
        log.info("点击登入按钮")
        self.base.base_click(self.login_btn)

    def get_usertext(self):
        log.info(f"获取登入用户名为：{self.base.base_get_text(self.usertext)}")
        return self.base.base_get_text(self.usertext)

    def page_login_task(self,username,code):
        log.info(f"正在执行登入操作，用户名：{username},验证码{code}")
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 发布文章依赖（正向）
    def page_login_article(self,):
        log.info(f"正在执行登入操作，用户名：13911111111,验证码：246810")
        self.page_input_username(13911111111)
        self.page_input_code(246810)
        self.page_click_login_btn()


