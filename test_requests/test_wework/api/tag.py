import requests

from test_requests.test_wework.api.base_api import BaseApi
from test_requests.test_wework.api.wework import WeWork


class Tag(WeWork):
    secret = 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'

    def get(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list?"
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json={"tag_id": []}
        )
        self.format(r)
        return r.json()

    def add(self, name, **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json={
                'group_id': 'etQKd-CgAAiicdm3Ew0TWxCkRNNDc7Wg',
                "tag":
                    [
                        {
                            "name": name
                        }
                    ]
            }
        )
        self.format(r)
        return r.json()

    def update(self):
        pass

    def delete(self, tag_id=[], group_id=[]):
        url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag'
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json={
                'group_id': group_id,
                "tag_id": tag_id
            }
        )
        self.format(r)
        return r.json()
