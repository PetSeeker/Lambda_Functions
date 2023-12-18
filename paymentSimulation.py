import json
import stripe
import os

stripe.api_key = os.environ.get('STRIPE_API_KEY')

DEFAULT_CARD_TOKEN = 'tok_visa'
DEFAULT_CURRENCY = 'EUR'

def create_or_get_customer(email):
    
    existing_customers = stripe.Customer.list(email=email)
    
    if existing_customers.data:
        
        return existing_customers.data[0].id
    
    customer = stripe.Customer.create(
        email=email,
        source=DEFAULT_CARD_TOKEN
    )
    
    return customer.id

def lambda_handler(event, context):
    # TODO implement
    
    try:
        email = event['email']
        amount = event['amount']

        # Create a new customer for each request
        customer_id = create_or_get_customer(email)

        # Create a charge using the customer ID
        charge = stripe.Charge.create(
            amount=amount*100,
            currency=DEFAULT_CURRENCY,
            customer=customer_id
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Payment successful', 'charge': charge})
        }

    except stripe.error.StripeError as e:
        
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

    except Exception as e:
      
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
