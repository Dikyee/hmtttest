import os

import allure

from page.page_pm_artical import PageArtical
from tools.get_log import GetLog
from base import base
from page.page_pm_login import PageElement
from tools.get_driver import GetDriver
import pytest

from tools.read_yaml import read_yaml

log = GetLog.get_log()

class TestLogin(object):
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver()
        self.base = base.Base(self.driver)
        self.pl = PageElement(self.driver)
        self.pa = PageArtical(self.driver)

    def teardown_class(self):
        # 退出driver
        GetDriver.quit_driver()

    @allure.story("发表文章")
    @pytest.mark.parametrize("title,content,tost",read_yaml("data_artical.yaml"))
    def test_artical(self,title,content,tost):

        self.pl.page_login_article()
        self.pa.page_publish_artical_task(title,content)
        self.tost = self.pa.page_get_tost()
        try:
            assert tost == self.tost
        except Exception as e:
            log.info(f"输出错误信息：{e}")
            self.base.base_get_errimg()
            raise

if __name__ == '__main__':
    pytest.main()
