from lambda_function import lambda_handler
import json


def test_handler_ok():
    event = {"body": json.dumps({"a": 7, "b": 2})}
    response = lambda_handler(event, None)
    body = json.loads(response["body"])
    assert response["statusCode"] == 200
    assert body["resultado"] == 9


def test_handler_error_tipo():
    event = {"body": json.dumps({"a": "cinco", "b": 3})}
    response = lambda_handler(event, None)
    body = json.loads(response["body"])
    assert response["statusCode"] == 400
    assert "numéricos" in body["error"]
