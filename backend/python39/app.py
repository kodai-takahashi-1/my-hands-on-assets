import json


def get_hello_world(event,context):
    text = "hello"
    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"},"body": json.dumps(text)}

def post_hello_world(event,context):
    posted_data = json.loads(event["body"])
    text = posted_data["text"]
    text=text[::-1]
    return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"},"body": json.dumps(text)}
