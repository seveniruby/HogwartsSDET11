import pytest

from test_framework.demo_page import DemoPage
from test_framework.utils import Utils


class TestLogin:
    testcase_file='test_search.yaml'
    po_file='page_demo.yaml'

    data = Utils.from_file(testcase_file)

    def setup_class(self):
        self.demo = DemoPage(self.po_file)
        self.demo.start()

    def setup(self):
        pass

    def teardown(self):
        self.demo.back()

    def teardown_class(self):
        self.demo.stop()

    # todo：测试数据的数据驱动
    @pytest.mark.parametrize('username, password', [
        ("user1", 'pasword1'),
        ('user2', 'password2')
    ])
    def test_login(self, username, password):
        # todo: 测试步骤的数据驱动
        self.demo.login(username, password)
        assert 1 == 1

    # @pytest.mark.parametrize('keyword', [
    #     'alibaba',
    #     # 'baidu',
    #     # 'jd'
    # ])

    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search(self, keyword):
        self.demo.search(keyword)

