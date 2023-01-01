import os
import json


def lambda_handler(event, context):
    message = "Hello world"
    json_region = os.environ["AWS_REGION"]
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"Region ": json_region, "Message": message}),
    }
