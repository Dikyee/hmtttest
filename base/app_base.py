from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from base.base import Base


class AppBase(object):

    def __init__(self,driver):
        self.driver = driver
        self.base = Base(self.driver)

    #查看页面是否存在指定元素
    def app_base_is_exist(self,loc):
        try:
            self.base.base_find(loc)
            print(f"找到：{loc}元素了")
            return True
        except:
            print(f"未找到{loc}元素")
            return False

    # 向左滑动规定的区域
    def app_base_figit_wipe_left(self,loc_are,click_text):
        # 查找元素
        el = self.base.base_find(loc_are)
        # 获取y值
        y = el.location.get("y")
        # 获取元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算起点和终点的坐标
        start_y = y + height * 0.5
        start_x = width * 0.8
        end_x = width * 0.2
        end_y = start_y
        # 组合元素配置信息
        loc = By.XPATH,f"//android.widget.LinearLayout/*[contains(@text,'{click_text}')]"
        # 循环操作
        while True:
            page_source = self.driver.page_source
            try:
                el = self.base.base_find(loc)
                print(f"已经找到元素：{loc}")
                el.click()
                break
            except:
                print(f"未找到元素：{loc}")
                self.driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=2000)
            if page_source == self.driver.page_source:
                print("已经滑到最后一页未找到元素")
                raise NoSuchElementException

    # 向上滑动规定的区域
    def app_base_figit_wipe_up(self,loc_are,click_text):
        # 查找元素
        el = self.base.base_find(loc_are)
        # 获取y值
        y = el.location.get("y")
        # 获取元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 计算起点和终点的坐标
        start_y = y + height * 0.8
        start_x = width * 0.5
        end_x = start_x
        end_y = y + height * 0.2
        # 组合元素配置信息
        loc = By.XPATH,f"//*[contains(@text,'{click_text}')]"
        # 循环操作
        while True:
            page_source = self.driver.page_source
            try:
                el = self.base.base_find(loc)
                print(f"已经找到元素：{loc}")
                el.click()
                break
            except:
                print(f"未找到元素：{loc}")
                print("正在滑动,继续查找元素")
                self.driver.swipe(start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y, duration=2000)
            if page_source == self.driver.page_source:
                print("已经滑到最后一页未找到元素")
                raise NoSuchElementException
