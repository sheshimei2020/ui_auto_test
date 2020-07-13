"""
审核文章
"""
import time

from selenium.webdriver.common.by import By

from base.mis.base_page import BasePage, BaseHandle



from utils import select_option, DriverUtils


# 对象库层
class Audit_page(BasePage):

    def __init__(self):
        super().__init__()

        # 文章名称输入框
        self.artical_title = (By.CSS_SELECTOR,"[placeholder*='文章']")
        # 查询按钮
        self.search_btn = (By.XPATH,"//*[text()='查询']")
        # 通过按钮
        self.pass_btn = (By.XPATH,"//*[text()='通过']")
        # 确认按钮
        self.confirm_btn = (By.CSS_SELECTOR,".el-button--primary")

    def find_artical_title(self):
        return self.find_ele(self.artical_title)

    def find_search_btn(self):
        return self.find_ele(self.search_btn)

    def find_pass_btn(self):
        return self.find_ele(self.pass_btn)

    def find_confirm_btn(self):
        return self.find_ele(self.confirm_btn)


# 操作层
class AuditHandle(BaseHandle):

    def __init__(self):
        self.audit_page = Audit_page()

    # 文章名称输入
    def input_art_title(self,art_title):
        self.input_text(self.audit_page.find_artical_title(),art_title)

    # 选择文章状态
    def check_art_status(self,status):
        select_option(DriverUtils.get_mis_driver(),"请选择状态",status)

    # 点击搜索按钮
    def click_search_btn(self):
        self.audit_page.find_search_btn().click()

    # 点击通过按钮
    def click_pass_btn(self):
        self.audit_page.find_pass_btn().click()

    # 点击确定按钮
    def click_confirm_btn(self):
        self.audit_page.find_confirm_btn().click()


# 业务层
class AuditProxy:

    def __init__(self):
        self.audit_handle = AuditHandle()

    # 审核文章
    def test_audit_art(self,art_title):
        # 1.输入文章标题
        self.audit_handle.input_art_title(art_title)
        # 2.选择待审核状态
        self.audit_handle.check_art_status("待审核")
        time.sleep(5)
        # 3.点击查询
        self.audit_handle.click_search_btn()
        time.sleep(3)
        # 4.点击通过按钮
        self.audit_handle.click_pass_btn()
        time.sleep(3)
        # 5.点击确定按钮
        self.audit_handle.click_confirm_btn()
        time.sleep(3)
        # 6.选择审核通过状态
        self.audit_handle.check_art_status("审核通过")
        # 7.点击查询按钮
        self.audit_handle.click_search_btn()