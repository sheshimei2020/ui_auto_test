import time

from config import PUB_ARTICAL_TITLE
from page.mis.audit_page import AuditProxy
from page.mis.home_page import HomeProxy
from utils import DriverUtils, is_exists_element

import pytest

@pytest.mark.run(order=102)
# 1.定义测试类
class TestAudit:

    # 2.定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()

        # 定义创建业务方法所在类的对象
        self.home_proxy = HomeProxy()
        self.audit_proxy = AuditProxy()

    # 3.定义测试方法
    def test_audit_artical(self):
        # 定义测试数据
        art_title = PUB_ARTICAL_TITLE
        # 执行测试步骤
        self.home_proxy.to_audit_page()
        self.audit_proxy.test_audit_art(art_title)

        # 断言
        assert is_exists_element(self.driver,art_title)

    # 4.定义销毁的方法
    def teardown_class(self):
        time.sleep(3)
        DriverUtils.quit_mis_driver()
