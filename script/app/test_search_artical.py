# 1.定义测试类
import time

from page.app.home_page import HomeProxy
from utils import DriverUtils


class TestSearchArtical:
    # 2.定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_app_driver()
        self.home_proxy = HomeProxy()


    # 3.定义测试方法
    def test_search_artical(self):
        # 定义测试数据
        channel_name = "前端"
        # 调用测试方法
        self.home_proxy.test_search_artical_by_channel_name(channel_name)
        # 断言



    # 4.定义销毁方法
    def teardown_class(self):
        time.sleep(3)
        DriverUtils.quit_app_driver()