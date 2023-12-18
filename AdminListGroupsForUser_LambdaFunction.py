import json
import boto3


def lambda_handler(event, context):
    cognito = boto3.client('cognito-idp')

    # Extract the user's Cognito username or other identifier from the request
    username = event.get('username')
    
    try:
        # Call the adminListGroupsForUser operation
        response = cognito.admin_list_groups_for_user(
            Username=username,
            UserPoolId="eu-north-1_fN4Xf9LZl"
        )

        # Extract group information from the response
        groups = [group['GroupName'] for group in response['Groups']]
        
        if groups:
            return {
                'statusCode': 200,
                'body': groups
            }
        else:
            return {
                'statusCode': 404,
                'body': 'No groups found for the user'
            }
    except Exception as e:
        print(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    
