from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.mp.base_page import BasePage, BaseHandle

# 对象库层: 将所有测试用例所需要在该页面操作的元素全部定义对应是实例方法
from utils import DriverUtils, select_option


class PubArtPage(BasePage):

    # 在初始化方法中定义元素的实例属性,并且赋值,值为定义方式及定位方式的值
    def __init__(self):
        super().__init__()
        # 文章标题
        self.art_title = (By.CSS_SELECTOR,"[placeholder*='名称']")
        # 文章内容 在iframe里面,要切换
        # iframe
        self.content_iframe = (By.CSS_SELECTOR,"#publishTinymce_ifr")
        # 文章内容
        self.art_content = (By.CSS_SELECTOR,"body")
        # 封面
        self.art_cover = (By.XPATH,"//*[text()='自动']")
        # 频道
        self.channel = (By.CSS_SELECTOR,"[placeholder*='请选择']")
        # 频道的选项
        self.channel_opt = (By.XPATH,"//*[text()='区块链']")
        # 发表
        self.pub_btn = (By.XPATH,"//*[text()='发表']")

    def find_art_title(self):
        return self.find_ele(self.art_title)

    def find_content_iframe(self):
        return self.find_ele(self.content_iframe)

    def find_art_content(self):
        return self.find_ele(self.art_content)

    def find_art_cover(self):
        return self.find_ele(self.art_cover)

    def find_channel(self):
        return self.find_ele(self.channel)

    def find_channel_opt(self):
        return self.find_ele(self.channel_opt)

    def find_pub_btn(self):
        return self.find_ele(self.pub_btn)



# 操作层: 通过调用对象库层的实例方法拿到元素对象,定义对应的操作方法
class PubArtHandle(BaseHandle):

    def __init__(self):
        self.pub_art_page = PubArtPage()

    # 输入文章标题
    def input_art_title(self,title):
        self.input_text(self.pub_art_page.find_art_title(),title)

    # 输入文章内容
    def input_art_content(self,content):
        # iframe切换
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_art_page.find_content_iframe())
        # 输入内容
        self.input_text(self.pub_art_page.find_art_content(),content)
        # 返回默认页面
        DriverUtils.get_mp_driver().switch_to.default_content()

    # 选择封面
    def choose_cover(self):
        self.pub_art_page.find_art_cover().click()

    # 选择频道
    def choose_channel(self,option_name):
        select_option(DriverUtils.get_mp_driver(),"请选择",option_name)
    # 点击发表
    def click_pub_btn(self):
        self.pub_art_page.find_pub_btn().click()


# 业务层: 调用多个操作层的实例方法就可以组织成对应的大业务方法
class PubArtProxy:

    def __init__(self):
        self.pub_art_handle = PubArtHandle()

    # 发表文章
    def test_pub_artical(self,title,content,option_name):
        # 1.输入标题
        self.pub_art_handle.input_art_title(title)
        # 2.输入内容
        self.pub_art_handle.input_art_content(content)
        # 3.选择封面
        self.pub_art_handle.choose_cover()
        # 4.选择频道
        self.pub_art_handle.choose_channel(option_name)
        # 5.点击发表
        self.pub_art_handle.click_pub_btn()


