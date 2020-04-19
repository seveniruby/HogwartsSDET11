import pytest
from jsonpath import jsonpath

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.tag import Tag


class TestTag:
    data = BaseApi.yaml_load("test_tag.data.yaml")
    steps = BaseApi.yaml_load("test_tag.step.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        cls.reset()

    @classmethod
    def init(cls):
        cls.data = cls.tag.yaml_load("test_tag.data.yaml")

    def test_get(self):
        r = self.tag.get()

        assert r['errcode'] == 0
        print(self.tag.jsonpath("$..tag[?(@.name!='')]"))

    def test_add(self):
        r = self.tag.add("demo1")
        assert r['errcode'] == 0

    # @pytest.mark.parametrize("name", [
    #     "demo1", "demo2", "中文测试", "中文_1", "123", " ", "*", "👿", ""
    # ])
    @pytest.mark.parametrize("name", data["test_delete"])
    def test_delete(self, name):
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


    @pytest.mark.parametrize("name", data["test_delete"][0:1])
    def test_delete_steps(self, name):
        self.tag.params={"name": name}
        self.tag.steps_run(self.steps['test_delete'])

    def teardown(self):
        # 在你的用例执行被强行kill的时候，teardown有可能会得不到执行
        self.reset()

    @classmethod
    def reset(cls):
        cls.tag.get()
        for name in ["demo1", "demo2"]:
            x = cls.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
            if isinstance(x, list) and len(x) > 0:
                cls.tag.delete(tag_id=[x[0]['id']])

    def test_xxx(self):
        self.tag.xxx()
