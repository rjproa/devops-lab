import json


def lambda_handler(event, context):
    try:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)

        a = body.get("a")
        b = body.get("b")

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Los valores deben ser numéricos")

        result = a + b
        return {
            "statusCode": 200,
            "body": json.dumps({"resultado": result})
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
