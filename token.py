import json
import base64
import requests

def lambda_handler(event, context):
    CLIENT_ID = '6v6kkovri0s114olnbbqe4e2iq'  # Your Cognito Client ID
    CLIENT_SECRET = '1tsofl5910rj87at1mku4p0vu13vrupm7lrp80492plnhhrt5vep'  # Your Cognito Client Secret
    TOKEN_ENDPOINT = 'https://es-deti-petseeker1.auth.eu-north-1.amazoncognito.com/oauth2/token'  # Cognito token endpoint URL

    # Parse input data from the event
    code = event.get('code')
    
    # Construct the request body for the token endpoint
    token_data = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'code': code,
        #'redirect_uri': 'http://localhost:3000/',  # Your redirect URI http://localhost:3000/
        'redirect_uri': 'https://main.dzgh2fc7t2w9u.amplifyapp.com/',
    }

    
    # Convert the client_id and client_secret to Base64 for the Authorization header
    client_credentials = f'{CLIENT_ID}:{CLIENT_SECRET}'.encode()
    base64_credentials = base64.b64encode(client_credentials).decode()

    # Set up the headers with the Authorization header
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {base64_credentials}',
    }

    try:
    #    # Make a POST request to the Cognito token endpoint
        response = requests.post(TOKEN_ENDPOINT, data=token_data, headers=headers)
    
        # Return the response data
        return {
            'statusCode': 200,
            'body': json.dumps(response.json())
        }
    except Exception as e:
        print('Token request failed:', str(e))

        # Return an error response
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Token request failed'})
        }

