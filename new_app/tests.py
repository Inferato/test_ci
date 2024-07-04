from django.test import TestCase
from .views import do_math


class TestMath(TestCase):

    def test_correct(self):
        a = 5
        b = 2
        result = do_math(a,b)
        self.assertEqual(result, 7)

    def test_wrong(self):
        a = 5
        b = 2
        result = do_math(a,b)
        self.assertEqual(result, 8)
