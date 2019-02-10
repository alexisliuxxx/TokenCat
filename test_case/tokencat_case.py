# -*- coding:utf-8 -*-

from scr.common.app.tokcat import NotLoggedIn
from scr.common.app.tokcat import HasLogged
import unittest


class Case1TokenCat(unittest.TestCase):

    @staticmethod
    def test1():
        NotLoggedIn.upper_chain()
        NotLoggedIn.get_ict()
        NotLoggedIn.sharing_information()
        NotLoggedIn.banner_img()
        NotLoggedIn.create_wallets()
        NotLoggedIn.daily_checkin()
        NotLoggedIn.first_login()
        NotLoggedIn.invite_friends()
        NotLoggedIn.play_dapp_1()
        NotLoggedIn.play_lucky_cat_10()
        NotLoggedIn.play_token_cat_10()

    @staticmethod
    def test2():
        has = HasLogged()
        has.upper_chain()
