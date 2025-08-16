import base64
import json

from probability import calculate_probability

def handle(request, context=None):
    print("Received request:", request)
    if request['requestContext']['http']['method'] == 'OPTIONS':
        return {
            'statusCode': 204,
            'headers': {
                'Access-Control-Allow-Origin': 'https://purple4reina.github.io/',
                'Access-Control-Allow-Methods': 'OPTIONS, POST',
                'Access-Control-Allow-Headers': 'Content-Type',
            }
        }

    body = request.get('body', '{}')
    if request.get('isBase64Encoded'):
        body = base64.b64decode(body).decode('utf-8')
    inputs = json.loads(body)
    result = calculate_probability(inputs)

    return {
            'statusCode': 200,
            'body': json.dumps(result),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': 'https://purple4reina.github.io/',
            },
    }
