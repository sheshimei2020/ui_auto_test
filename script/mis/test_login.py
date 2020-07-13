import time

from page.mis.login_page import LoginProxy
from utils import DriverUtils, is_exists_element
import pytest

@pytest.mark.run(order=101)
class TestLogin:

    # 1.创建浏览器驱动对象以及打开浏览器
    # 2.创建测试方法所要调用的业务方法所在类的对象
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        self.login_proxy = LoginProxy()

    def test_mis_login(self):
        # 定义测试数据
        username = "testid"
        password = "testpwd123"
        # 执行测试用例步骤
        self.login_proxy.test_mis_login(username,password)
        # 断言
        assert is_exists_element(self.driver,"管理员")

    # 关闭浏览器
    def teardown_class(self):
        time.sleep(2)
        DriverUtils.quit_mis_driver()