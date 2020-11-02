from django.test import TestCase
from monolith.classes import Bmi
from decimal import *


# Create your tests here.

class BMITestCase(TestCase):

    def test_bmi_cases(self):
        first_case = Bmi(height=Decimal('1.75'), weight=Decimal('85'))
        first_result = Decimal('27.76')
        self.assertEqual(first_case.bmi(), first_result)
        second_case = Bmi(height=Decimal('1.75'), weight=Decimal('85'))
        self.assertEqual(first_case.bmi(), second_case.bmi())
        third_case = Bmi(height=Decimal('1.85'), weight=Decimal('77'))
        third_result = Decimal('22.5')
        self.assertEqual(third_case.bmi(), third_result)


