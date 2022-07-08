"""
    文章发表
"""
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_log()
class PageArtical(object):
    def __init__(self,driver):
        self.base = Base(driver)
        self.driver = driver
        self.content = By.CSS_SELECTOR,'[class="el-submenu__title"]'
        self.postartical = (By.XPATH,"//li[contains(text(), '发布文章')]")
        self.title = By.CSS_SELECTOR,'[placeholder="文章名称"]'
        self.art_content = By.CSS_SELECTOR,'[id="tinymce"]'
        self.type = By.XPATH,"//span[contains(text(), '自动')]"
        self.channel1 = '[placeholder="请选择"]'
        self.channel2 = "数据库"
        self.publish = By.CSS_SELECTOR,'[class="el-button filter-item el-button--primary"]'
        self.tost = By.XPATH,"//p[contains(text(), '新增文章成功')]"


    # 点击发布内容管理
    def page_click_content(self):
        log.info("正在点击内容发布")
        self.base.base_click(self.content)

    #点击发布文章
    def page_click_postartical(self):
        log.info("点击发布文章")
        el = self.base.base_find(self.postartical)
        ActionChains(self.driver).move_to_element(el).click().perform()
        sleep(5)

    # 输入标题
    def page_input_title(self,titles):
        log.info("正在输入标题")
        self.base.base_input(self.title,titles)

    # 输入内容
    def page_input_content(self,content):
        log.info("正在输入内容")
        self.base.base_switch_ifram('publishTinymce_ifr')
        self.base.base_input(self.art_content,content)
        self.base.base_switch_default()

    # 点击类型
    def page_click_type(self):
        log.info("正在选择自动类型")
        self.base.base_click(self.type)

    # 选择频道
    def page_click_channel(self):
        log.info("正在选择频道")
        self.base.base_click_element(self.channel1,self.channel2)

    # 发表
    def page_publish_artical(self):
        log.info("点击发表")
        self.base.base_click(self.publish)

    # 获取发表信息
    def page_get_tost(self):
        log.info("正在获取提示")
        return self.base.base_get_text(self.tost)

    # 发表流程
    def page_publish_artical_task(self,title,content):
        self.page_click_content()
        self.page_click_postartical()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_type()
        self.page_click_channel()
        self.page_publish_artical()


