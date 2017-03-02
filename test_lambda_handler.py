import unittest

import lambda_handler


class TestLambda_handler(unittest.TestCase):
    def test_lambda_handler_no_params(self):
        response = lambda_handler.lambda_handler({}, {})
        assert response['statusCode'] == '400'

    def test_lambda_handler_no_code(self):
        response = lambda_handler.lambda_handler({
            'code': 'hello'
        }, {})
        assert response['statusCode'] == '400'

    def test_lambda_handler_no_game(self):
        response = lambda_handler.lambda_handler({
            'game': 'world'
        }, {})
        assert response['statusCode'] == '400'

    # def test_lambda_handler_real(self):
    #     response = lambda_handler.lambda_handler({
    #         'game': 'test',
    #         'code': 'PRV1'
    #     }, {})


if __name__ == '__main__':
    unittest.main()
