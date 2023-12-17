import json
import requests

def lambda_handler(event, context):
    USER_INFO_URL = "https://es-deti-petseeker1.auth.eu-north-1.amazoncognito.com/oauth2/userInfo"
    # Get the access token from the event request
    access_token = event.get('access_token')

    
    if access_token is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Access token is missing'})
        }

    headers = {
        "Authorization": "Bearer " + access_token,
    }
    
    try:
    #    # Make a POST request to the Cognito token endpoint
        response = requests.get(USER_INFO_URL, headers=headers)

        # Return the response data
        return {
            'statusCode': 200,
            'body': json.dumps(response.json())
        }
    except Exception as e:
        print('User Info request failed:', str(e))

        # Return an error response
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'User Info request failed'})
        }

