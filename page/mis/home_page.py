from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle


# 对象库层
class HomePage(BasePage):

    def __init__(self):
        super().__init__()

        # 信息管理
        self.info_manage = (By.CSS_SELECTOR,".fa-shopping-basket")
        # 内容审核
        self.content_audit = (By.XPATH,"//*[contains(text(),'内容审核')]")

    def find_info_manage(self):
        return self.find_ele(self.info_manage)

    def find_content_audit(self):
        return self.find_ele(self.content_audit)


# 操作层
class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    # 点击信息管理
    def click_info_manage_btn(self):
        self.home_page.find_info_manage().click()

    # 点击内容审核
    def click_content_audit_btn(self):
        self.home_page.find_content_audit().click()


# 业务层
class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    def to_audit_page(self):
        self.home_handle.click_info_manage_btn()
        self.home_handle.click_content_audit_btn()