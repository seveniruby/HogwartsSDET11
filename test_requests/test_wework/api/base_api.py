import json
import logging

import yaml
from jsonpath import jsonpath
from requests import Request


class BaseApi:
    @classmethod
    def format(cls, r):
        cls.r=r
        # print(json.dumps(r.json(), indent=2))
        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None):
        if r is None:
            r=self.r.json()
        return jsonpath(r, path)

    #todo: 封装类似HttpRunner这样的数据驱动框架
    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            request: Request = None
            for step in steps:
                logging.info(step)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{%s}" % key, self._params[key])
                        element.send_keys(content)