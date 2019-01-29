from Controller.mains import Pointer
import time


class CloudWallet(object):
    """ 云钱包登录模块 """
    @staticmethod
    def login(
            phone_number=13267122772,
            verification_code=input("verification_code:"),
            invitation_code=123456):
        """
        登录云钱包
        :param phone_number:    手机号（登录所需的账号）
        :param verification_code:   短信验证码
        :param invitation_code:     邀请码，首次使用邀请码可获得额外积分
        """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_user_account").click()
        Pointer.devices(text="请输入手机号码").set_text(phone_number)
        Pointer.devices(text="请输入验证码").set_text(verification_code)
        Pointer.devices(text='填写好友邀请码领积分').set_text(invitation_code)
        Pointer.devices.press('back')      # 关闭输入键盘的操作
        Pointer.devices(resourceId="com.x.wallet.debug:id/checkbox").click()
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_login").click()


class MonetaryUnit(object):
    """ 切换货币单位 """
    @staticmethod
    def switch():
        """ 切换货币单位 """
        country_type = ['CHF', 'CNY', 'EUR', 'GBP',
                        'HKD', 'INR', 'JPY', 'KRW',
                        'NZD', 'PLN', 'RUB', 'SGD', 'THB', 'USD']
        for i in country_type:
            Pointer.devices.implicitly_wait(3)
            Pointer.devices(
                resourceId="com.x.wallet.debug:id/ccpv_change_currency_pref").click()
            if i in ['SGD', 'THB', 'USD']:
                time.sleep(1)
                Pointer.devices(scrollable=True).scroll(steps=80)
                time.sleep(1)
            Pointer.devices(text=i).click()
            Pointer.devices.toast.get_message(5.0, default="ERROR")


class PurchaseRecord(object):
    """ 检查交易记录 """
    @staticmethod
    def purchase_record():
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_trading_recording").click()
        tips = Pointer.devices(text="若未收到邀请码，请加客服微信：axhahaxh").get_text()
        assert tips == "若未收到邀请码，请加客服微信：axhahaxh"


class Recommend(object):
    """ 推荐tokencat"""
    @staticmethod
    def recommend_tokencat_to_friends():
        """ 推荐tokencat给好友 """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_share_app").click()
        Pointer.devices(text="文件传输助手").click()
        Pointer.devices(text="分享").click()
        Pointer.devices(text="返回通证猫开发版").click()

    @staticmethod
    def recommend_friends_to_earn_points(xml=u"邀请好友赚积分", select="text"):
        """ 我的界面右上角分享tokencat """
        mode = [
            "com.x.wallet.debug:id/tv_friend_wechat",       # 微信好友
            "com.x.wallet.debug:id/tv_friend_circle",       # 朋友圈
            "com.x.wallet.debug:id/tv_save_local"           # 保存本地
        ]
        for i in mode:
            if select == "text":
                Pointer.devices(text=xml).click()
            else:
                Pointer.devices(resourceId=xml).click()
            Pointer.devices(resourceId=i).click()
            if i == mode[0]:
                Pointer.devices(
                    resourceId="com.tencent.mm:id/au7").send_keys("文件传输助手")
                Pointer.devices(resourceId='com.tencent.mm:id/lp').click()
                Pointer.devices(resourceId="com.tencent.mm:id/an3").click()
                Pointer.devices(resourceId="com.tencent.mm:id/an2").click()
            elif i == mode[1]:
                Pointer.devices(resourceId="com.tencent.mm:id/hg").click()
            elif i == mode[2]:
                toast = Pointer.devices.toast.get_message(10)
                print(toast)


class ServiceAgreement(object):
    """ 检查服务协议跳转是否正常"""
    @staticmethod
    def check_agreement():
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_service_aggrement").click()
        text = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_title").get_text()
        Pointer.devices.press("back")
        print(text)
        return text


class WalletManager(Pointer):
    """ 钱包管理模块 """

    def __init__(self):
        Pointer.me_page()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_manage_wallet").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_eos_account").click()

    @staticmethod
    def import_eos_wallet(private_key, set_password="123456", confirm_password="123456"):
        """
        导入eos钱包
        :param private_key:     eos私钥
        :param set_password:    设置密码
        :param confirm_password:    确认密码
        """
        Pointer.devices.implicitly_wait(3)
        Pointer.devices(text='导入EOS钱包').click()
        Pointer.devices.implicitly_wait(3)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/key_et").send_keys(private_key)
        Pointer.devices.implicitly_wait(3)
        Pointer.devices(text='导入私钥').click()
        Pointer.devices.implicitly_wait(50)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/set_password_view").send_keys(set_password)
        # Pointer.devices.press("back")
        Pointer.devices.implicitly_wait(3)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/comfirm_password_view").send_keys(confirm_password)
        Pointer.devices.press("back")
        Pointer.devices(resourceId="com.x.wallet.debug:id/checkbox").click()
        Pointer.devices.implicitly_wait(3)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/create_account_btn").click()
        time.sleep(1)
        Pointer.devices(resourceId="com.x.wallet.debug:id/iv_back").click()
        time.sleep(1)
        management_wallet_name = Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_account_name").get_text(3)
        print(management_wallet_name)
        time.sleep(1)
        Pointer.devices(resourceId="com.x.wallet.debug:id/iv_back").click()
        time.sleep(1)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/navigation_account").click()
        time.sleep(1)
        Pointer.devices(text="本地钱包").click()
        Pointer.devices.implicitly_wait(3)
        home_wallet_names = Pointer.devices(
            resourceId="com.x.wallet.debug:id/account_name_tv").get_text()
        assert management_wallet_name == home_wallet_names

    @staticmethod
    def create_eos_wallet(account_name, set_password="123456", confirm_password="123456",
                          invitation_code=input("invitation_code:")):
        """
        创建eos账户
        :param account_name:   账户名唯一，12位，英文，数字1-6
        :param set_password:    设置密码
        :param confirm_password:    配置钱包密码
        :param invitation_code:     邀请码（激活码）
        """
        Pointer.me_page()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/rl_wallet_manager").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_eos_account").click()
        Pointer.devices(resourceId="com.x.wallet.debug:id/create_eos").click()
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_alerady").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/et_eos_account_name").send_keys(account_name)
        Pointer.devices.press("back")
        Pointer.devices(resourceId="com.x.wallet.debug:id/btn_next").click()
        Pointer.devices.implicitly_wait(10)
        Pointer.devices(text="请输入激活码").send_keys(invitation_code)
        Pointer.devices(text="请设置钱包密码").send_keys(set_password)
        Pointer.devices.press("back")
        Pointer.devices(text="请再次输入密码").send_keys(confirm_password)
        Pointer.devices.press("back")
        Pointer.devices(resourceId="com.x.wallet.debug:id/checkbox").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/create_account_btn").click()
        # TODO: 创建成功后的流程暂时跳过
        # Pointer.devices(resourceId="com.x.wallet.debug:id/iv_back").click()
        # time.sleep(2)
        # Pointer.devices(resourceId="com.x.wallet.debug:id/iv_back").click()
        # time.sleep(2)
        # Pointer.devices(resourceId="com.x.wallet.debug:id/iv_back").click()

    @staticmethod
    def change_password(old_password="123456", new_password="1234567", confirm_password="1234567"):
        """
        修改本地钱包密码
        :param old_password: 旧密码（原密码）
        :param new_password:    新密码
        :param confirm_password:    确认密码
        """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_manage_wallet").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_wallet_name").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_change_password_tv").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/current_password_et").send_keys(old_password)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/new_password_et").send_keys(new_password)
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/confirm_new_password_et").send_keys(confirm_password)
        Pointer.devices(resourceId="com.x.wallet.debug:id/confirm_btn").click()

    @staticmethod
    def export_private_key(password="zxc123.."):
        """ 导出eos钱包私钥 """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_manage_wallet").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_wallet_name").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_import_private_key").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/password_et").send_keys(password)
        Pointer.devices(resourceId="com.x.wallet.debug:id/confirm_btn").click()

    @staticmethod
    def delete_wallet(password="zxc123.."):
        """
        删除钱包密码
        :param password:
        :return:
        """
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/ccpv_manage_wallet").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/tv_wallet_name").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/delete_account_tv").click()
        Pointer.devices(
            resourceId="com.x.wallet.debug:id/password_et").send_keys(password)
        Pointer.devices(resourceId="com.x.wallet.debug:id/confirm_btn").click()


if __name__ == '__main__':
    Recommend.recommend_friends_to_earn_points()
