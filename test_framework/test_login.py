import pytest

from test_framework.base_page import BasePage
from test_framework.demo_page import DemoPage
from test_framework.common_page import CommonPage
from test_framework.utils import Utils


class TestLogin:
    testcase_file='test_search.yaml'
    po_file='page_demo.yaml'

    data = Utils.from_file(testcase_file)

    def setup_class(self):
        self.app=BasePage()
        self.app.start()

    def setup(self):
        pass

    # def teardown(self):
    #     self.demo.back()

    def teardown_class(self):
        self.app.stop()

    # todo：测试数据的数据驱动
    @pytest.mark.parametrize('username, password', [
        ("user1", 'pasword1'),
        ('user2', 'password2')
    ])
    def test_login(self, username, password):
        self.demo = DemoPage(self.po_file)
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
        self.demo = DemoPage(self.po_file)
        self.demo.search(keyword)
        self.demo.back()

    #用common page代替
    @pytest.mark.parametrize(data['keys'], data['values'])
    def test_search_common(self, keyword):
        demo=CommonPage(self.po_file)
        demo.search(keyword=keyword)
        demo.back()

    def test_login(self):
        po_file="page_login.yaml"
        login=CommonPage(po_file)
        # login.start()
        #借助于__getattr__方法实现任意方法代理
        #login.xxxxx => login.__getattr__
        #login.login_by_password => print
        #print('15600530000', '111111')
        # login.login_by_password('15600530000', '111111')

        login.login_by_password(username='15600530000', password='111111')

