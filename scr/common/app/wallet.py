from Controller.mains import Pointer
from scr.common.app.me import CloudWallet


class GetWalletInfo(object):
    pass


class CloudWallets(object):
    def __init__(self):
        if Pointer.devices(text="请登录").exists:
            Pointer.devices(text="云端钱包").click()        # 进入
            CloudWallet.login()     # 如果没有登录，将进行登录
        Pointer.wallet_page()   # 登录完成后跳转到Wallet_page

    def get_cloud_wallet_info(self):
        pass


class LocalWallet(object):
    pass
