"""
自媒体端登录页面
"""
from selenium.webdriver.common.by import By

from base.mp.base_page import BasePage, BaseHandle


# 对象库层: 将所有测试用例所需要在该页面操作的元素全部定义对应是实例方法
class LoginPage(BasePage):

    # 在初始化方法中定义元素的实例属性,并且赋值,值为定义方式及定位方式的值
    def __init__(self):
        super().__init__()
        # 手机号码输入框
        self.phone_num = (By.CSS_SELECTOR,"[placeholder*='手机']")
        # 验证码
        self.code = (By.CSS_SELECTOR,"[placeholder*='验证码']")
        # 登录按钮
        self.login_btn = (By.CSS_SELECTOR,".el-button--primary")


    def find_phone_num(self):
        return self.find_ele(self.phone_num)

    def find_code(self):
        return self.find_ele(self.code)

    def find_login_btn(self):
        return self.find_ele(self.login_btn)


# 操作层: 通过调用对象库层的实例方法拿到元素对象,定义对应的操作方法
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()
    # 输入手机号码
    def input_phone(self,phone):
        self.input_text(self.login_page.find_phone_num(),phone)

    # 输入验证码
    def input_code(self,code):
        self.input_text(self.login_page.find_code(),code)

    # 点击登录按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()

# 业务层: 调用多个操作层的实例方法就可以组织成对应的大业务方法
class LoginProxy:

    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务
    def test_login(self,phone,code):
        # 1.输入电话号码
        self.login_handle.input_phone(phone)
        # 2.输入验证码
        self.login_handle.input_code(code)
        # 3.点击登录
        self.login_handle.click_login_btn()
