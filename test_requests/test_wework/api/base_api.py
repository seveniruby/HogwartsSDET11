import json
import logging

import requests
import yaml
from jsonpath import jsonpath
from requests import Request


class BaseApi:
    params = {}
    data={}

    @classmethod
    def format(cls, r):
        cls.r = r
        # print(json.dumps(r.json(), indent=2))
        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None, **kwargs):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

    # 封装yaml文件的加载
    @classmethod
    def yaml_load(cls, path) -> list:
        with open(path) as f:
            return yaml.safe_load(f)

    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, req: dict):

        req['params']['access_token'] = self.get_token(self.secret)
        print(req)

        #模板内容替换
        # todo: 使用format
        raw = yaml.dump(req)
        for key, value in self.params.items():
            raw=raw.replace(f"${{{key}}}", repr(value))
            print("replace")
        req = yaml.safe_load(raw)

        print(req)

        r = requests.request(
            req['method'],
            url=req['url'],
            params=req['params'],
            json=req['json']
        )
        self.format(r)
        return r.json()

    # todo: 封装类似HttpRunner这样的数据驱动框架
    def steps_run(self, steps: list):

        for step in steps:
            print(step)

            # 模板内容替换
            # todo: 使用format
            raw = yaml.dump(step)
            for key, value in self.params.items():
                raw = raw.replace(f"${{{key}}}", repr(value))
                print("replace")
                print(raw)
            step = yaml.safe_load(raw)

            if isinstance(step, dict):
                if "method" in step.keys():
                    method=step['method'].split('.')[-1]
                    #todo: 用装饰器精简参数
                    getattr(self, method)(**step)
                if "extract" in step.keys():
                    self.data[step["extract"]]=getattr(self, 'jsonpath')(**step)
                    print("extract")
                    print(self.data[step["extract"]])

                if "assertion" in step.keys():
                    assertion=step["assertion"]
                    if isinstance(assertion, str):
                        assert eval(assertion)
                    if assertion[1]=="eq":
                        assert assertion[0] == assertion[2]





        #
        # req['params']['access_token'] = self.get_token(self.secret)
        # print(req)
        #

        #
        # print(req)
        #
        # r = requests.request(
        #     req['method'],
        #     url=req['url'],
        #     params=req['params'],
        #     json=req['json']
        # )
        # self.format(r)
        # return r.json()