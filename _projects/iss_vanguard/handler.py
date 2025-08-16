import base64
import json

from probability import calculate_probability

def handle(request, context=None):
    print("Received request:", request)
    body = request.get('body', '{}')
    if request.get('isBase64Encoded'):
        body = base64.b64decode(body).decode('utf-8')
    inputs = json.loads(body)
    result = calculate_probability(inputs)
    return {
            'statusCode': 200,
            'body': json.dumps(result),
    }
