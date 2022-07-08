from time import sleep

import pytest
from base.base import Base
from page.page_app_login import AppLogin
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_log()
class TestLogin(object):


    def setup_class(self):
        self.driver = GetDriver.get_app_driver()
        self.applogin = AppLogin(self.driver)
        self.base = Base(self.driver)


    def teardown_class(self):
        GetDriver.quit_app_driver()

    @pytest.mark.parametrize("user,pwd,expert",read_yaml("data_applogin.yaml"))
    def test_app_login(self,user,pwd,expert):
        self.driver.wait_activity("com.netease.nr.phone.main.MainActivity",10)
        self.applogin.applogin_task(user,pwd)
        sleep(3)
        print("您是否登入成功",self.applogin.applogin_get_success())
        try:
            assert expert == self.applogin.applogin_get_success()
        except Exception as e :
            log.info(f"输出错误信息：",e)
            self.base.base_get_errimg()
            raise

if __name__ == '__main__':
    pytest.main()