from paypalrestsdk import Payments, Payouts, Billing, BillingAgreement
from paypalrestsdk import PayPalEnvironment, PayPalAPI
class PayPalSDK:
    def __init__(self):
        self.environment = PayPalEnvironment(
            client_id=settings.PAYPAL_CLIENT_ID,
            client_secret=settings.PAYPAL_SECRET_KEY
        )
