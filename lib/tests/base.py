import logging

from unittest import TestCase

from environs import Env

from payze.clinet.account2card import PayzeAccount2CardAPI

env = Env()
env.read_env()


class BaseTestCase(TestCase):
    # pylint: disable=missing-class-docstring
    key = env.str("KEY")
    secret = env.str("SECRET")
    url = env.str("URL")
    url_mobile_cards = env.str("URL_MOBILE_CARDS")
    web_hook_getaway = env.str("WEB_HOOK_GETAWAY")
    error_redirect_getaway = env.str("ERROR_REDIRECT_GETAWAY")
    success_redirect_getaway = env.str("SUCCESS_REDIRECT_GETAWAY")

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        logging.disable(logging.CRITICAL)

        cls.account2card = PayzeAccount2CardAPI(
            key=cls.key,
            secret=cls.secret,
            url=cls.url,
            url_mobile_cards=cls.url_mobile_cards,
            web_hook_gateway=cls.web_hook_getaway,
            error_redirect_gateway=cls.error_redirect_getaway,
            success_redirect_gateway=cls.success_redirect_getaway
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        logging.disable(logging.NOTSET)
