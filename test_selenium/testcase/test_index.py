from test_selenium.page.index import Index


class TestIndex:

    def setup(self):
        self.index = Index()

    def test_register(self):
        # self.driver.find_element(By.LINK_TEXT, "立即注册").click()

        # self.driver.find_element(By.ID, "corp_name").send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, "submit_btn").click()

        self.index.goto_register().register("霍格沃兹测试学院")

    def test_login(self):
        # self.index.goto_login()
        # login=Login(self.driver)

        register_page = self.index.goto_login().goto_registry().register("测吧（北京）科技有限公司")
        print(register_page.get_error_message())
        print("|".join(register_page.get_error_message()))
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
