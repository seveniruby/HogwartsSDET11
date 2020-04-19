import pytest
from jsonpath import jsonpath

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.tag import Tag


class TestDDD:
    #todo: 单文件改成多文件
    data = BaseApi.yaml_load("test_tag.all.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()
        cls.reset()


    @pytest.mark.parametrize("name", data["data"][0:1])
    def test_delete_steps(self, name):
        self.tag.params={"name": name}
        self.tag.steps_run(self.data['steps'])

    @classmethod
    def reset(cls):
        cls.tag.get()
        for name in ["demo1", "demo2"]:
            x = cls.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
            if isinstance(x, list) and len(x) > 0:
                cls.tag.delete(tag_id=[x[0]['id']])
