import pytest

from utils import DriverUtils

@pytest.mark.run(order=100)
class TestBegin:

    def test_begin(self):
        # 关闭浏览器开关 修改__mp_key的值为False
        DriverUtils.change_mis_key(False)