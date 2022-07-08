from base.base import Base
from page.page_pm_login import PageElement

class PageClass(object):
    def __init__(self,driver):
        self.driver = driver

    def page_login_tast(self,username,code):
        PageElement(self.driver).page_login_task(username,code)

