import json

from probability import calculate_probability

def handle(request):
    print("Received request:", request)
    inputs = json.loads(request.get('body') or '{}')
    result = calculate_probability(inputs)
    return {
            'statusCode': 200,
            'body': json.dumps(result),
    }
