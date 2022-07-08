import pytest
from base.base import Base
from page.page_app_artical import AppArtical
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog().get_log()

class TestArtical(object):

    def setup_class(self):
        self.driver = GetDriver.get_app_driver()
        self.artical = AppArtical(self.driver)
        self.base = Base(self.driver)

    def teardown_class(self):
        GetDriver.quit_app_driver()
    @pytest.mark.parametrize("channel,title",read_yaml("data_app_artical.yaml"))
    def test_app_artical(self,channel,title):
        self.driver.wait_activity("com.netease.nr.phone.main.MainActivity",10)
        self.artical.app_artical_task(channel)
        try:
            self.artical.app_find_artical(title)
        except Exception as e :
            log.info(f"输出错误信息：",e)
            self.base.base_get_errimg()
            raise







if __name__ == '__main__':
    pytest.main()
