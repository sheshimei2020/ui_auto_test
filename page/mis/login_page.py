"""
黑马头条后台管理系统登录页面
"""
from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle
from utils import DriverUtils

# 对象库层
class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        # 账号
        self.username = (By.NAME,"username")
        # 密码
        self.password = (By.NAME,"password")
        # 登录
        self.submit_btn = (By.ID,"inp1")

    def find_username(self):
        return self.find_ele(self.username)

    def find_password(self):
        return self.find_ele(self.password)

    def find_submit_btn(self):
        return self.find_ele(self.submit_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self,username):
        self.input_text(self.login_page.find_username(),username)

    # 输入密码
    def input_password(self,password):
        self.input_text(self.login_page.find_password(),password)

    # 点击登录
    def click_submit_btn(self):
        js_str = 'document.getElementById("inp1").removeAttribute("disabled")'
        DriverUtils.get_mis_driver().execute_script(js_str)
        self.login_page.find_submit_btn().click()


# 业务层
class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务
    def test_mis_login(self,username,password):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.click_submit_btn()

