import unittest
import mock
import lambda_handler

class TestLambda_handler(unittest.TestCase):
    def test_lambda_handler(self):
        lambda_handler.lambda_handler("hello", "world")
        self.fail()

if __name__ == '__main__':
    unittest.main()