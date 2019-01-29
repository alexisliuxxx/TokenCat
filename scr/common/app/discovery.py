from Controller.mains import Pointer


class DApps(object):
    pass


class News(object):
    def __init__(self):
        Pointer.discovery_page()
        Pointer.devices(
            text=u"资讯",
            className="android.widget.TextView").click()

    @staticmethod
    def share_news():
        """分享资讯 直接掉用了我的模块的 分享tokencat功能，并使用次功能实现分享资讯"""
        Pointer.discovery_page()
        Recommends = __import__("scr.common.app.me.Recommend", fromlist=True)
        # from scr.common.app.me import Recommend
        Recommends().recommend_friends_to_earn_points(
            select="resourceId",
            xml="com.x.wallet.debug:id/news_share_tv")
        Pointer.devices(resourceId="com.x.wallet.debug:id/tv_cancel").click()


if __name__ == '__main__':
    x = News()
    x.share_news()
