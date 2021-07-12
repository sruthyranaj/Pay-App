import stripe
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
# False if not in os.environ
stripe.api_key = env('STRIPE_SECRET_KEY')


class StripeConfig():
    def __init__(self):
        pass

    def pay_invoice(self, invoice_number): 
        res = stripe.Invoice.pay("invoice_number")
        print(res)
