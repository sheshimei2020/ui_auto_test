import pytest

from utils import DriverUtils

@pytest.mark.run(order=99)
class TestEnd:

    def test_end(self):
        DriverUtils.change_mp_key(True)
        DriverUtils.quit_mp_driver()