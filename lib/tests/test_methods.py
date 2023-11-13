from tests.base import BaseTestCase

from payze.types.params import AddCardDataParam, VerifyCardDataParam, RefundParam, ExtraAttribute, StatusCheckParam


class Account2CardTestCase(BaseTestCase):
    def test_add_card(self):
        response = self.account2card.add_card(
            params=AddCardDataParam(
                source="Card",
                amount="1",
                currency="USD",
                language="EN",
                tokenize_card=True
            )
        )

        print(response)

    def test_verify_card(self):
        response = self.account2card.verify_card(
            params=VerifyCardDataParam(
                number="8600000000000007",
                card_holder="xxx",
                expire_date="04/26",
                transaction_id="trx-id"
            )
        )

        print(response)

    def test_account2card(self):
        response = self.account2card.account2card(
            params=RefundParam(
                source="Wallet",
                amount=1,
                currency="UZS",
                language="EN",
                token="card-token",
                extra_attributes=[
                    ExtraAttribute(
                        key="order_id",
                        value="1721",
                        description="it's order"
                    ).to_dict()
                ]
            )
        )

        print(response)

    def test_status_check(self):
        response = self.account2card.status_check(
            params=StatusCheckParam(
                check_id="check-id"
            )
        )

        print(response)
