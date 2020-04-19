import json

import requests

from test_requests.test_wework.api.wework import WeWork


class GroupChat(WeWork):
    secret = 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'

    def list(self, offset=0, limit=1000, **kwargs):
        data = {"offset": offset, "limit": limit}
        print(kwargs)
        print(data)
        data.update(kwargs)
        print(data)
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json=data
        )
        #todo: 自动加解密
        #todo：多环境支持，根据配置可以一套case测试多套环境，需要修改host
        self.format(r)
        return r.json()

    def get(self, chat_id):
        detail_url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        r = requests.post(
            detail_url,
            params={'access_token': self.get_token(self.secret)},
            json={"chat_id": chat_id}
        )
        self.format(r)
        return r.json()
