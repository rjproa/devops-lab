from main import handler
import json


def test_handler_ok():
    event = {"body": json.dumps({"a": 5, "b": 3})}
    response = handler(event, None)
    body = json.loads(response["body"])
    assert response["statusCode"] == 200
    assert body["resultado"] == 7


def test_handler_error_tipo():
    event = {"body": json.dumps({"a": "cinco", "b": 3})}
    response = handler(event, None)
    body = json.loads(response["body"])
    assert response["statusCode"] == 400
    assert "numéricos" in body["error"]
