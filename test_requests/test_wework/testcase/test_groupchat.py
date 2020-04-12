from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestWeWork:

    @classmethod
    def setup_class(cls):
        cls.groupchat = GroupChat()

    def test_groupchat_get(self):
        r = self.groupchat.list()
        assert r['errcode'] == 0

    def test_groupchat_get_status(self):
        r = self.groupchat.list(offset=0, limit=10, status_filter=1)
        assert r["errcode"] == 0

    def test_groupchat_detail(self):
        r = self.groupchat.list(offset=0, limit=10)
        assert r['errcode'] == 0

        chat_id = r['group_chat_list'][0]['chat_id']
        r = self.groupchat.get(chat_id)
        assert r['errcode'] == 0
        assert len(r['group_chat']['member_list']) > 0
