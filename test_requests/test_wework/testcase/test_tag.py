from jsonpath import jsonpath

from test_requests.test_wework.api.tag import Tag


class TestTag:
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        cls.reset()

    def test_get(self):
        r = self.tag.get()

        assert r['errcode'] == 0
        print(self.tag.jsonpath("$..tag[?(@.name!='')]"))
        print(self.tag.jsonpath("$..tag[?(@.name=='demo1')]")[0]['id'])

    def test_add(self):
        r = self.tag.add("demo1")
        assert r['errcode'] == 0

    def test_delete(self):
        name = "demo2"

        # 如果有就删除
        r = self.tag.get()
        x = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete(tag_id=[x[0]['id']])

        # 环境干净后开始测试
        r = self.tag.get()
        path = "$..tag[?(@.name!='')]"
        size = len(self.tag.jsonpath(path))

        # 添加新标签
        self.tag.add(name)
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size + 1
        tag_id = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]['id']
        print(tag_id)
        # 删除新标签
        self.tag.delete(tag_id=[tag_id])

        # 断言
        r = self.tag.get()
        assert len(self.tag.jsonpath(path)) == size

    # def setup(self):
    #     #删除测试组
    #     #遍历删除测试数据
    #     self.reset()

    def teardown(self):
        #在你的用例执行被强行kill的时候，teardown有可能会得不到执行
        self.reset()

    @classmethod
    def reset(cls):
        for name in ["demo1", "demo2"]:
            x = cls.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
            if isinstance(x, list) and len(x) > 0:
                cls.tag.delete(tag_id=[x[0]['id']])





