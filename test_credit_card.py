from unittest import TestCase

from assignments.credit_card import CreditCard


class TestCreditCard(TestCase):
    def test_even_sum_calculator(self):
        credit_card = '5399831619690403'
        credit = CreditCard(credit_card)
        number = credit.even_sum_calculator()
        self.assertEqual(24, number)

    def test_odd_sum_calculator(self):
        credit_card = '5399831619690403'
        credit = CreditCard(credit_card)
        number = credit.odd_number_calculator()
        self.assertEqual(46, number)

    def test_validate(self):
        credit_card = '5399831619690403'
        credit = CreditCard(credit_card)
        reply = credit.validate()
        self.assertEqual("Valid", reply)

    def test_card_type_validator(self):
        credit_card = '5399831619690403'
        credit = CreditCard(credit_card)
        reply = credit.card_type_validator()
        self.assertEqual("Master card", reply)

    def test_card_length(self):
        credit_card = '5399831619690403'
        credit = CreditCard(credit_card)
        number = credit.card_length()
        self.assertEqual(16, number)

