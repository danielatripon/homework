import unittest
from unittest import TestCase
# from DanielaTriponHomeworkWeek4 import validate_pin
from DanielaTriponHwWeek4Simple import validate_pin1, validate_pin2, validate_amount1, validate_amount2


class TestValidatePinAndAmount(TestCase):
    def test_validate_pin(self):
        actual = 1234
        expected = validate_pin1(pin=1234)
        self.assertEqual(actual, expected)

    def test_validate_pin_exception(self):
        wrong_pin = 1222
        with self.assertRaises(ValueError) as exc:
            validate_pin1(pin=wrong_pin)
        self.assertEqual(
            str(exc.exception),
            "Incorrect pin."
        )

    def test_validate_pin_another_exception(self):
        wrong_pin = 12345
        with self.assertRaises(ValueError) as exc:
            validate_pin2(pin=wrong_pin)
        self.assertEqual(
            str(exc.exception),
            "Your pin must be 4 digits long"
        )

    def test_validate_amount_exception(self):
        big_amount = 200
        with self.assertRaises(ValueError) as exc:
            validate_amount1(amount=big_amount)
        self.assertEqual(
            str(exc.exception),
            'Not enough funds. Please withdraw £100 or less'
        )

    def test_remaining_balance_exception(self):
        rem_balance = 110
        with self.assertRaises(ValueError) as exc:
            validate_amount2(amount=rem_balance)
        self.assertEqual(
            str(exc.exception),
            'Insufficient funds. Try a different amount'
        )


if __name__ == '__main__':
    unittest.main()
