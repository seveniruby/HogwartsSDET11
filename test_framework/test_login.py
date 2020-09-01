import pytest

from test_framework.demo_page import DemoPage


class TestLogin:
    def setup_class(self):
        self.demo = DemoPage()
        self.demo.start()

    def teardown_class(self):
        self.demo.stop()

    #todo：测试数据的数据驱动
    @pytest.mark.parametrize('username, password', [
        ("user1", 'pasword1'),
        ('user2', 'password2')
    ])
    def test_login(self, username, password):
        #todo: 测试步骤的数据驱动
        self.demo.login(username, password)
        assert 1 == 1

    @pytest.mark.parametrize('keyword', [
        'alibaba',
        # 'baidu',
        # 'jd'
    ])
    def test_search(self, keyword):
        self.demo.search(keyword)
