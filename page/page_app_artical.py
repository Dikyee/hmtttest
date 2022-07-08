from selenium.webdriver.common.by import By

from base.app_base import AppBase


class AppArtical(object):

    def __init__(self,driver):
        self.driver = driver
        self.appbase = AppBase(self.driver)
        self.pindao = By.XPATH,"//*[@resource-id='com.netease.newsreader.activity:id/bmz']"
        self.title = By.XPATH,"//*[@resource-id='com.netease.newsreader.activity:id/oq']"

    # 滑动p频道
    def app_swip_pindao(self,channel):
        self.appbase.app_base_figit_wipe_left(self.pindao,channel)

    # 查找文章
    def app_find_artical(self,title):
        self.appbase.app_base_figit_wipe_up(self.title,title)

    # 查找文章业务
    def app_artical_task(self,channel):
        self.app_swip_pindao(channel)
