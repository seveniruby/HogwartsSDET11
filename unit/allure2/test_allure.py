import pytest
import allure
from allure import attachment_type


# @pytest.mark.parametrize("x", [1, 2, 3])
# @pytest.mark.parametrize("y", [4, 5, 6])
@pytest.mark.parametrize("x, y", [
    (1, 2),
    (3, 3),
    (4, 7)
])
def test_x(x, y):
    allure.attach("title", "content", attachment_type=attachment_type.TEXT)
    # allure.attach(open("/Users/seveniruby/Dropbox/sihanjishu/startup/霍格沃兹测试学院/banner/定向班/定向班.png").read(),
    #               attachment_type=attachment_type.JPG
    #               )

    allure.attach("{ a: 1, b: 2}", attachment_type=attachment_type.JSON)
    allure.attach('<html><body>'
                  '<img class="attachment__media" height="100%"'
                  'src="https://www.testing-studio.com/wp-content/uploads/2019/11/%E5%AD%A6%E9%99%A2%E5%AE%98%E7%BD%91-banner%E6%A9%99%E8%89%B2%E7%89%88.jpg">'
                  '</body></html>',
                  attachment_type=attachment_type.HTML)
    allure.attach.file(
        "/Users/seveniruby/Dropbox/sihanjishu/startup/霍格沃兹测试学院/banner/定向班/定向班.png",
        # "https://www.testing-studio.com/wp-content/uploads/2019/11/%E5%AD%A6%E9%99%A2%E5%AE%98%E7%BD%91-banner%E6%A9%99%E8%89%B2%E7%89%88.jpg",
        attachment_type=attachment_type.JPG
    )


    allure.attach.file('/Users/seveniruby/Documents/Zoom/2020-01-05 10.01.05 11期测开课程 645587896/zoom_1.mp4',
                       attachment_type=attachment_type.MP4)
    assert x == y + 3
