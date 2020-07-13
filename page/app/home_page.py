from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from base.app.base_page import BasePage, BaseHandle


# 对象库层
from utils import DriverUtils


class HomePage(BasePage):

    def __init__(self):
        super().__init__()

        # 频道区域
        self.channel_area = (By.CLASS_NAME,"android.widget.HorizontalScrollView")
        # 频道
        self.channel_option = (By.XPATH,"//*[contains(@text,'{}')]")
        # 第一条文章信息
        self.first_artical = (By.XPATH,"//*[contains(@text,'评论')]")

    def find_channel_area(self):
        return self.find_ele(self.channel_area)

    def find_channel_option(self,channel_name):
        return self.driver.find_element(self.channel_option[0],self.channel_option[1].format(channel_name))

    def find_first_artical(self):
        return self.find_ele(self.first_artical)


# 操作类
class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    # 1.选择频道
    def select_channel(self,channel_name):
        # 获取区域范围
        area = self.home_page.find_channel_area()
        x = area.location["x"]
        y = area.location["y"]

        w = area.size["weight"]
        h = area.size["height"]

        start_x = x + w*0.75
        start_y = y + h*0.5

        end_x = x + w*0.25
        end_y = start_y

        # 在当前区域根据频道名称来查找对应元素
        while True:

            # 获取当前页面信息
            page_old = DriverUtils.get_app_driver().page_source

            # 如果找到元素则点击
            try:
                self.home_page.find_channel_option(channel_name).click()
                break
            # 如果没找到则进行滑动
            except Exception as e:
                DriverUtils.get_app_driver().swipe(start_x,start_y,end_x,end_y,500)
                # 获取滑动之后的页面信息
                page_new = DriverUtils.get_app_driver().page_source
                # 判断滑动之前和滑动之后的页面信息是否相等
                if page_old == page_new:
                    raise NoSuchElementException("not find {} channel".format(channel_name))


        pass

    # 2.点击第一条文章
    def click_first_artical(self):
        self.home_page.find_first_artical().click()

# 业务层
class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    # 根据频道查询文章
    def test_search_artical_by_channel_name(self,channel_name):
        # 选择频道
        self.home_handle.select_channel(channel_name)
        # 点击第一条文章
        self.home_handle.click_first_artical()
