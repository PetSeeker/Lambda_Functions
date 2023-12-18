import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            #'Location': 'https://es-deti-petseeker1.auth.eu-north-1.amazoncognito.com/login?client_id=6v6kkovri0s114olnbbqe4e2iq&response_type=code&scope=email+openid+phone&redirect_uri=http%3A%2F%2Flocalhost%3A3000%2F'
            'Location': 'https://es-deti-petseeker1.auth.eu-north-1.amazoncognito.com/login?client_id=6v6kkovri0s114olnbbqe4e2iq&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Fmain.dzgh2fc7t2w9u.amplifyapp.com%2F'
        },
        'body': json.dumps({'message': 'Redirect URL sent in headers'}),
    }