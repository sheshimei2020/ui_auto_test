import logging
import time

import pytest

from config import PUB_ARTICAL_TITLE, BASE_PATH
from page.mp.home_page import HomeProxy
from page.mp.publish_artical_page import PubArtProxy
from utils import DriverUtils, is_exists_element, build_data


# 1.定义测试类
@pytest.mark.run(order=2)
class TestMpPubArt:

    # 2.定义初始化方法
    def setup_class(self):
        # 启动浏览器
        self.driver = DriverUtils.get_mp_driver()
        # 创建好对应要调用的业务层对象
        self.home_proxy = HomeProxy()
        self.pub_art_proxy = PubArtProxy()

    # 3.定义业务测试方法
    @pytest.mark.parametrize("art_content,channel_name",build_data(BASE_PATH +"/data/test_pub_artical_data.json"))
    def test_mp_pub_art(self,art_content,channel_name):

        # a.定义测试数据
        art_title = PUB_ARTICAL_TITLE
        art_content = art_content
        option_name = channel_name

        logging.info("发布文章信息为:文章标题={},文章内容={},文章频道={}".format(art_title,art_content,channel_name))
        
        # b.调用业务层已经封装好的业务方法
        self.home_proxy.to_pub_artical_page()
        self.pub_art_proxy.test_pub_artical(art_title,art_content,option_name)
        # c 对测试结果进行断言
        assert is_exists_element(self.driver,"新增文章成功")

    # 4.定义销毁方法
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mp_driver()
