import requests
import boto3

def lambda_handler(event, context):
    client = boto3.client('cognito-idp', region_name='eu-north-1')
    
    user_data = event['request']['userAttributes']  # Extract user data from Cognito event
    username = event['userName']
    
    try:
        response = client.admin_add_user_to_group(
            UserPoolId='eu-north-1_fN4Xf9LZl',
            Username=username,
            GroupName='Client'
        )
        print(f'User {username} added to group Client successfully')
    except Exception as e:
        print(f'Error adding user to group: {str(e)}')
    
    # Send form data to the Profile Management API
    profile_api_url = 'https://gqt5g3f1h4.execute-api.eu-north-1.amazonaws.com/v1/profile'
    
    profile_payload = {
        'username': event['userName'],
        'email': user_data['email']
    }
    
    try:
        profile_response = requests.post(profile_api_url, data=profile_payload)
        print('Form Data API Response:', profile_response.json())
    except requests.RequestException as e:
        print('Error making Form Data API request:', e)

    # Send JSON data to the Notifications API
    notifications_api_url = 'https://gqt5g3f1h4.execute-api.eu-north-1.amazonaws.com/v1/notifications/verify-and-add-email'
    notifications_payload = {
        'email': user_data['email']
    }

    try:
        notifications_response = requests.post(notifications_api_url, json=notifications_payload)
        print('JSON Data API Response:', notifications_response.json())
    except requests.RequestException as e:
        print('Error making JSON Data API request:', e)
  
    # Continue with the Cognito signup process
    return event
