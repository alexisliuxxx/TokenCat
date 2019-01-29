import unittest
from scr.common.app.me import *


class Case1Wallet(unittest.TestCase):
    @staticmethod
    def test1():
        test_private_key = "5K9q8iuBd2yQx414jSPxPLFGY63KoLMJ55GvFWiPYGacExg7nDE"
        WalletManager.import_eos_wallet(private_key=test_private_key)       # private_key为必须参数

    @staticmethod
    def test2():
        WalletManager.create_eos_wallet(account_name="test",
                                        invitation_code="1234")


class Case2Cloud(unittest.TestCase):
    @staticmethod
    def test3():
        CloudWallet.login()


class Case3PurchaseRecord(unittest.TestCase):
    @staticmethod
    def test4():
        PurchaseRecord.purchase_record()


class Case4MonetaryUnit(unittest.TestCase):
    @staticmethod
    def test1():
        MonetaryUnit.switch()


class Case5ServiceAgreement(unittest.TestCase):
    @staticmethod
    def test1():
        ServiceAgreement.check_agreement()


class Case6Recommend(unittest.TestCase):
    Recommend = Recommend()

    def test1(self):
        self.Recommend.recommend_tokencat_to_friends()

    def test2(self):
        self.Recommend.recommend_friends_to_earn_points()


if __name__ == '__main__':
    unittest.main(verbosity=2)
