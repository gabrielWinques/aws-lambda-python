from lambda_function import lambda_handler

def test_lambda_returns_status_200():
    event = {}
    context = {}

    response = lambda_handler(event, context)

    assert response["statusCode"] == 200


def test_lambda_returns_correct_body():
    event = {}
    context = {}

    response = lambda_handler(event, context)

    assert response["body"] == "Teste branch protection"