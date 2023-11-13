"""
payze class attributes
"""
from dataclasses import dataclass


@dataclass
class PayzeConfigOPS:
    """
    base attributes
    """
    url: str
    key: str
    secret: str
    url_mobile_cards: str
    web_hook_gateway: str
    error_redirect_gateway: str
    success_redirect_gateway: str

    def to_dict(self):
        """
        dict representation.
        """
        return {
            "url": self.url,
            "key": self.key,
            "secret": self.secret,
            "url_mobile_cards": self.url_mobile_cards,
            "web_hook_getaway": self.web_hook_gateway,
            "error_redirect_getaway": self.error_redirect_gateway,
            "success_redirect_getaway": self.success_redirect_gateway
        }
