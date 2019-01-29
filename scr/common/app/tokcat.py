from Controller.mains import Pointer
import time


class NotLoggedIn(object):
    """ 检查未登陆情况下的各个功能是否正常 """

    def __init__(self):
        """ 检测云账户是否登录，如果已经登录云账户，则退出登录 """
        Pointer.me_page()
        if Pointer.devices(text="请登录").exists:
            Pointer.devices(
                resourceId="com.x.wallet.debug:id/tv_user_account").click()
            Pointer.devices(
                resourceId="com.x.wallet.debug:id/btn_logout").click()
        Pointer.tokencat_page()

    @staticmethod
    def banner_img():
        Pointer.devices(resourceId="com.x.wallet.debug:id/img").click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def get_ict():
        """ 检查ict数量 """
        total = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_total").get_text()
        assert total == "0 ICT"

    @staticmethod
    def upper_chain():
        """ ICT上链(提现操作) """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_withdraw").click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def points_details():
        """ 检查交易明细 """
        Pointer.devices(resourceId="com.x.wallet.debug:id/tv_details").click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def invite_friends():
        """ 邀请好友"""
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_go").click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def daily_checkin():
        """ 每日签到 """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_go",
            text=u"去签到").click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def play_dapp_1():
        """ 首次玩dapp """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_go",
            text=u"去完成").click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def play_token_cat_10():
        """ 每日玩10次通证猫转盘 """
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_go", text=u"去完成",
                        className="android.widget.Button", instance=1).click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.tokencat_page()
        assert title == "通证猫专区"

    @staticmethod
    def sharing_information():
        """ 每日分享资讯，此处会上拉屏幕 """
        Pointer.devices(scrollable=True).scroll(steps=20)
        time.sleep(3)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_go",
            text=u"去分享").click()
        date = Pointer.devices(
            resourceId="com.x.wallet.debug:id/news_date_tv").get_text()
        Pointer.tokencat_page()
        print(date)

    @staticmethod
    def create_wallets():
        """ 导入/创建钱包"""
        Pointer.devices.click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def first_login():
        """ 首次登录 """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_go",
            text=u"去登录").click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"

    @staticmethod
    def play_lucky_cat_10():
        """ 玩10次luckycat """
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_go", text=u"去完成",
                        className="android.widget.Button", instance=3).click()
        title = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press('back')
        assert title == "登录"


class HasLogged(object):
    """ 验证登录云钱包后的功能是否正常 """
    cloud_account_total = ""
    cloud_wallet_total = ""

    def __init__(self):
        import re
        """ 检测是否已登录云钱包为"""
        Pointer.me_page()
        if Pointer.devices(text="请登录").exists:
            from scr.common.app.me import CloudWallet
            cloud = CloudWallet()
            cloud.login()
        Pointer.tokencat_page()
        # 获取云账户ICT
        cloud_account_total = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_total").get_text()
        self.cloud_account_total = int(
            re.findall(r"\d+", cloud_account_total)[0])
        Pointer.wallet_page()
        # 获取云钱包ICT
        self.cloud_wallet_total = Pointer.devices(
            resourceId="com.x.wallet.debug:id/balance_tv").get_text()
        Pointer.tokencat_page()

    def upper_chain(self, number=1, password="123456"):
        """ 提现操作,包括全部提现以及自定义数量 """
        # 验证是否跳转到提现界面
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_withdraw").click()
        assert Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text() == "提现"
        # 验证全部提现是否正常
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_all_with_draw").click()
        upper_all = Pointer.devices(
            resourceId="com.x.wallet.debug:id/et_num").get_text()
        print(upper_all, self.cloud_account_total)
        assert int(self.cloud_account_total) == int(upper_all)
        handling_fee = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_des").get_text()
        print(handling_fee)
        # 自定义提现ICT数量
        Pointer.devices(resourceId="com.x.wallet.debug:id/et_num").clear_text()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/et_num").send_keys(number)
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_logout").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/password_et").send_keys(password)
        Pointer.devices(resourceId="com.x.wallet.debug:id/confirm_btn").click()
        toast = Pointer.devices.toast.get_message(5)
        assert toast == "完成"

    @staticmethod
    def points_details():
        Pointer.devices(resourceId="com.x.wallet.debug:id/tv_details").click()
        title = Pointer.devices(
            resourceID="com.x.wallet.debug:id/tv_title").get_text()
        assert title == "积分明细"

    @staticmethod
    def invite_friends():
        # 微信好友
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_friend_wechat").click()
        Pointer.devices(resourceId="com.tencent.mm:id/au7").send_keys("文件传输助手")
        Pointer.devices(resourceId="com.tencent.mm:id/lp").click()
        Pointer.devices(resourceId="com.tencent.mm:id/an3").click()
        Pointer.devices(resourceId="com.tencent.mm:id/an2").click()
        # 微信朋友圈
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_friend_circle").click()
        Pointer.devices(resourceId="com.tencent.mm:id/hg").click()
        # 保存本地
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_save_local").click()
        msg = Pointer.toast.get_toast(0.5)
        print(msg)

    def daily_checkin(self):
        """ 每日签到 """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_go",
            text=u"去签到").click()
        if Pointer.devices(
                resourceId="com.x.wallet.debug:id/btn_go",
                text=u"已完成").exists:
            self.cloud_account_total += 1

    @staticmethod
    def play_dapp_1():
        """每日首次玩dapp"""
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_go",
            text=u"去完成").click()
        if Pointer.devices(
                resourceId="com.x.wallet.debug:id/tv_no_account").exists:
            from scr.common.app.me import WalletManager
            Pointer.devices(text="招财猫 LuckyCat").click()
            Pointer.devices(
                resourceId="com.x.wallet.debug:id/btn_sure").click()
            WalletManager().import_eos_wallet(private_key="siyao")
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_sure").click()
        # 跳转到luckycat
        assert Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text() == "招财猫 LuckyCat"

    @staticmethod
    def play_token_cat_10():
        """ 玩10次tokenCat """
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_go", text=u"去完成",
                        className="android.widget.Button", instance=1).click()
        assert Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text() == "通证猫专区"
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ll_root",
            className="android.widget.RelativeLayout").click()  # 进入通证猫转盘
        Pointer.back_home_pages()

    @staticmethod
    def sharing_information():
        Pointer.devices(scrollable=True).scroll(steps=20)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/btn_go",
            text=u"去分享").click()
        Pointer.devices()


if __name__ == '__main__':
    # x = NotLoggedIn()
    # x.sharing_information()
    y = HasLogged()
    y.play_token_cat_10()
