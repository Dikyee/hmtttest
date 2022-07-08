from time import sleep

from selenium.webdriver.common.by import By

from base.app_base import AppBase


class AppLogin(object):

    def __init__(self,driver):
        self.user = By.XPATH,"//*[@text='网易邮箱/手机号']"
        self.pwd = By.XPATH,"//*[@text='密码']"
        self.lgbt = By.XPATH,"//*[@index='3' and @text='登 录']"
        self.appbase = AppBase(driver)
        self.lg_success = By.XPATH,"//*[@text='今天还没有阅读文章' and @index='0']"
        self.my = By.XPATH,"//*[@bounds='[938,2162][1005,2190]']"
        self.login = By.XPATH,"//*[@resource-id='com.netease.newsreader.activity:id/a71']"
        self.clickuser = By.XPATH,"//*[@resource-id='com.netease.newsreader.activity:id/p8']"

    #点击我的
    def applogin_click_my(self):
        self.appbase.base.base_click(self.my)

    #点击登入
    def applogin_click_gologin(self):
        self.appbase.base.base_click(self.login)


    # 输入账号
    def applogin_input_user(self,value):
        self.appbase.base.base_input(self.user,value)

    # 确认账号
    def applogin_click_user(self):
        self.appbase.base.base_click(self.clickuser)

    # 输入密码
    def applogin_input_pwd(self,pwd):
        self.appbase.base.base_input(self.pwd,pwd)

    # 点击登入
    def applogin_click_loginbt(self):
        sleep(3)
        self.appbase.base.base_click(self.lgbt)

    # 判断是否登入成功
    def applogin_get_success(self):
        return self.appbase.app_base_is_exist(self.lg_success)

    # 登入业务
    def applogin_task(self,user,pwd):
        sleep(5)
        # self.appbase.app_target_click(self.my,969,2178)
        self.applogin_click_my()
        self.applogin_click_gologin()
        self.applogin_input_user(user)
        self.applogin_click_user()
        self.applogin_input_pwd(pwd)
        self.applogin_click_loginbt()