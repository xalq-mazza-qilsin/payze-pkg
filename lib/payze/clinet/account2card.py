"""
Payze Account2Card implementation.
"""
import requests

from payze.types import request, response, params as params_classes, atttributes

from payze.utils.decorator import error_catcher


class PayzeAccount2CardAPI:
    """
    PayzeAccount2CardAPI provides account2card API functionality.
    """
    def __init__(self, attributes: atttributes.PayzeConfigOPS):
        self.url = attributes.url
        self.url_mobile_cards = attributes.url_mobile_cards
        self.web_hook_gateway = attributes.web_hook_gateway
        self.error_redirect_gateway = attributes.error_redirect_gateway
        self.success_redirect_gateway = attributes.success_redirect_gateway

        self.headers: dict = {
            "Authorization": f"{attributes.key}:{attributes.secret}",
            # for verify card
            "Content-Type": "application/x-www-form-urlencoded"
        }

    @error_catcher
    def _send_request(self, method, data=None, json_data=None, url=None, params=None): # noqa
        if url is None:
            url = self.url
            self.headers["Content-Type"] = "application/json"

        return requests.request(
            method=method,
            url=url,
            data=data,
            json=json_data,
            headers=self.headers,
            params=params,
            timeout=20
        )

    def add_card(self, params: params_classes.AddCardDataParam) -> response.ResponseAddCard:
        """
        that's used for getting the transaction id of adding card.
        """
        json_data = request.RequestAddCardCreate(
            source=params.source,
            amount=params.amount,
            currency=params.currency,
            language=params.language,
            idempotency_key=params.idempotency_key,
            wallet_payment=request.WalletPayment(
                tokenize_card=params.tokenize_card
            ),
            hooks=request.Hooks(
                web_hook_gateway=self.web_hook_gateway,
                success_redirect_gateway=self.success_redirect_gateway,
                error_redirect_gateway=self.error_redirect_gateway
            ),
            extra_attributes=params.extra_attributes
        ).to_dict()

        resp = self._send_request(
            method="PUT",
            json_data=json_data,
        )

        return response.ResponseAddCard(**resp)

    def verify_card(self, params: params_classes.VerifyCardDataParam) -> response.ResponseVerifyCard:
        """
        that's used for verify card token.
        """
        json_data = request.RequestVerifyCardData(
            number=params.number,
            card_holder=params.card_holder,
            expire_date=params.expire_date,
            transaction_id=params.transaction_id
        ).to_form()

        resp = self._send_request(
            method="POST",
            url=self.url_mobile_cards,
            data=json_data
        )

        return response.ResponseVerifyCard(**resp)

    def account2card(self, params: params_classes.RefundParam):
        """
        that's used account2card method (refund)
        """
        json_data = request.RequestRefund(
            source=params.source,
            amount=params.amount,
            language=params.language,
            currency=params.currency,
            token=params.token,
            idempotency_key=params.idempotency_key,
            extra_attributes=params.extra_attributes,
            hooks=request.Hooks(
                web_hook_gateway=self.web_hook_gateway,
                success_redirect_gateway=self.success_redirect_gateway,
                error_redirect_gateway=self.error_redirect_gateway
            )
        ).to_dict()

        resp = self._send_request(
            method="PUT",
            json_data=json_data
        )
    
        return response.ResponseRefund(**resp)

    def status_check(self, params: params_classes.StatusCheckParam) -> response.ResponseStatusCheck:
        """
        check transition status.
        """
        self.url = self.url + "/query/token-based"

        params = request.RequestStatusCheck(
            check_id=params.check_id
        ).to_query_param()

        resp = self._send_request(
            method="GET",
            params=params
        )

        return response.ResponseStatusCheck(**resp)
