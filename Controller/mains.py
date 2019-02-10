# -*- coding:utf-8 -*-


import os
import time
import uiautomator2
import warnings


class BasePages(object):
    def __init__(self):
        """ 检查设备是否正常连接，如果设备是首次运行，
        将会进行初始化操作，如需清空app缓存，将clear改为True """
        warnings.filterwarnings("ignore")  # 忽略异常
        clear = False           # 清空app缓存
        try:
            self.devices = uiautomator2.connect_usb()
            # self.devices.app_stop("com.x.wallet.debug")

            if clear:
                self.devices.app_clear("com.x.wallet.debug")
            self.devices.app_start("com.x.wallet.debug")
            if clear:
                # 允许权限
                self.devices.implicitly_wait(5)
                self.devices(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
                self.devices(resourceId="com.android.packageinstaller:id/permission_allow_button").click()
            print(self.devices.device_info)
        except RuntimeError as e:
            error = e.args[0]
            if error == 'device agent responds with an error code 502':
                print("初始化设备...")
                os.system("python -m uiautomator2 init")        # 设备首次运行需要初始化
            if error == "Can't find any android device/emulator":
                os.popen("adb connect 127.0.0.1:7555")
            else:
                print(e)
                # TODO: 后需出现异常将重新处理

    def back_home_pages(self):
        """ 返回到首页（最顶层目录） """
        while True:
            if self.devices(resourceId="com.x.wallet.debug:id/navigation_me").exists:
                break
            else:
                self.devices.press('back')
                time.sleep(3)

    def me_page(self):
        """ 进入我的模块 """
        self.back_home_pages()
        self.devices(resourceId="com.x.wallet.debug:id/navigation_me").click()

    def tokencat_page(self):
        """ 进入积分模块 """
        self.back_home_pages()
        self.devices(resourceId="com.x.wallet.debug:id/navigation_integration_center").click()

    def wallet_page(self):
        """ 进入钱包模块 """
        self.back_home_pages()
        self.devices(resourceId="com.x.wallet.debug:id/navigation_account").click()

    def discovery_page(self):
        """ 进入发现模块 """
        self.back_home_pages()
        self.devices(resourceId="com.x.wallet.debug:id/navigation_news").click()

    def restart_app(self, clear=False):
        """ 重新启动app, 默认不清空缓存 """
        self.devices.app_stop("com.x.wallet.debug")
        if clear:
            self.devices.app_clear("com.x.wallet.debug")
        self.devices.app_start("com.x.waller.debug")


Pointer = BasePages()
