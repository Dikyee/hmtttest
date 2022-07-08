# 导包
from selenium import webdriver
from time import sleep
import threading

# 封装百度请求

def get_baidu(driver):
    # driver = webdriver.Chrome()
    driver.get("http://www.baidu.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.find_element_by_id('kw').send_keys('python')
    driver.find_element_by_id('su').click()
    sleep(5)
    driver.quit()

# 封装driver
def get_driver(browser):
    cap = None
    if browser is "chrome":
        cap = webdriver.DesiredCapabilities.CHROME.copy()
    elif browser is "firefox":
        cap = webdriver.DesiredCapabilities.FIREFOX.copy()
    cap['platform'] = "WINDOWS"
    return webdriver.Remote("http://127.0.0.1:4444/wd/hub",cap)

# 遍历多线程
browserName = ['chrome','firefox']

for browser in browserName:
    driver = get_driver(browser)
    threading.Thread(target=get_baidu,args=(driver,)).start()
